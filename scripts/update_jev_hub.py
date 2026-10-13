#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
awesome-jev-hub 低频周更新脚本
================================
职责：
  1. 刷新所有已收录项目的 GitHub 实测元数据（star / fork / 语言 / 协议 / 时间 / 归档状态）
  2. 发现近 N 天新出现的 Jev 相关开源项目，按置信度分流
     - 高置信（名称/描述命中 Jev/TypeSafe/System One/decision model 等）→ 自动收录
       （写入 data/new_projects.json + README 的 NEW_DISCOVERIES 段）
     - 低置信 → 写入 data/candidates.json 待人工复核，不进 README
  3. 重渲 jev-collection.html（刷新 star 数字）
  4. 生成 weekly_report.md
  5. 可选 git commit + push（需 --push）

Rate-limit 友好：
  - 全部走 `gh api`（已登录 token，限额 5000/hr，非未认证 60/hr 的 IP 限制）
  - 串行请求，每次间隔 SLEEP 秒；遇 403/429 走指数退避（封顶 60s，最多 5 次）
  - search 单独限额 30/min（认证），单次拉 100 条足够

用法：
  python3 update_jev_hub.py [--push] [--dry-run] [--days 7]
"""
import subprocess, json, os, sys, time, datetime, re, shutil

BASE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(BASE)
DATA = os.path.join(REPO, "data")
SELF_FULL = "supermanc417-alt/awesome-jev-hub"
SLEEP = 0.4          # 两次 API 调用之间的间隔（秒）
SEARCH_PER_PAGE = 100
MIN_STARS = 3        # 新项目最低 star 门槛，过滤纯噪声

HIGH_KW = ["jev", "typesafe", "system one", "systemone", "decision model",
           "ai function", "system one model", "small model decision"]

def log(*a):
    print("[update]", *a, flush=True)

def gh_api(path, tries=5):
    """带重试/退避的 gh api 调用。返回 dict。"""
    for i in range(tries):
        try:
            p = subprocess.run(["gh", "api", path], capture_output=True, text=True, timeout=30)
            if p.returncode != 0:
                err = p.stderr.lower()
                if "rate limit" in err or p.returncode in (403, 429):
                    wait = min(2 ** i * 5, 60)
                    log(f"  rate-limited ({p.returncode}), sleep {wait}s")
                    time.sleep(wait)
                    continue
                # 404 等其他错误直接抛出
                raise RuntimeError(f"gh api {path} -> {p.returncode}: {p.stderr.strip()[:200]}")
            return json.loads(p.stdout)
        except RuntimeError:
            raise
        except Exception as e:
            if i == tries - 1:
                raise
            time.sleep(min(2 ** i * 3, 30))
    raise RuntimeError(f"gh api {path} exhausted retries")

def refresh_repo(full):
    """拉取单个仓库的完整元数据，规整成与 jev_data.json 同构的 dict。
    遇 404（仓库已删除/改名/私有）返回 exists=False 的最小标记，交由主循环合并旧值。"""
    try:
        d = gh_api("repos/" + full)
    except RuntimeError as e:
        if "Not Found" in str(e):
            return {"full_name": full, "exists": False, "archived": True}
        raise
    lic = (d.get("license") or {}).get("spdx_id") or "未声明"
    return {
        "full_name": d["full_name"], "exists": True, "id": d["id"],
        "html_url": d["html_url"], "description": d.get("description") or "",
        "stargazers_count": d["stargazers_count"], "forks_count": d["forks_count"],
        "language": d.get("language") or "未知", "topics": d.get("topics") or [],
        "homepage": d.get("homepage") or "", "created_at": d["created_at"],
        "pushed_at": d["pushed_at"], "open_issues_count": d["open_issues_count"],
        "license": lic, "archived": d.get("archived", False),
        "owner": d["owner"]["login"], "repo": d["name"],
    }

def load_json(path):
    if os.path.exists(path):
        with open(path, encoding="utf-8") as f:
            return json.load(f)
    return {}

def save_json(path, obj):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(obj, f, ensure_ascii=False, indent=2)

def main():
    args = sys.argv[1:]
    push = "--push" in args
    dry = "--dry-run" in args
    days = 7
    for a in args:
        if a.startswith("--days="):
            days = int(a.split("=")[1])

    today = datetime.date.today()
    cutoff = (today - datetime.timedelta(days=days)).isoformat()
    log(f"更新窗口: 最近 {days} 天 (>= {cutoff})  push={push} dry={dry}")

    # ---------- 1. 加载并刷新已收录 ----------
    f1 = os.path.join(DATA, "jev_data.json")
    f2 = os.path.join(DATA, "jev_data2.json")
    d1 = load_json(f1)
    d2 = load_json(f2)
    collected = {}
    for k, v in {**d1, **d2}.items():
        collected[k] = v

    log(f"已收录项目: {len(collected)} 个，开始刷新元数据...")
    stars_before = {}
    for full, old in collected.items():
        try:
            new = refresh_repo(full)
            stars_before[full] = old.get("stargazers_count", 0)
            # 写回原属文件
            target = d1 if full in d1 else d2
            if new.get("exists") is False:
                old.update(new)  # 标记失效，保留历史 star/描述
                target[full] = old
                log(f"  仓库失效(404): {full} 已标记 exists=False")
            else:
                target[full] = new
            time.sleep(SLEEP)
        except Exception as e:
            log(f"  ! 刷新失败 {full}: {e}")

    # 保存刷新后的元数据
    save_json(f1, d1)
    save_json(f2, d2)
    save_json(os.path.join(DATA, "jev_data.json.bak"), d1)
    save_json(os.path.join(DATA, "jev_data2.json.bak"), d2)
    log("元数据刷新完成，已写回 jev_data*.json")

    # ---------- 2. 发现新项目（持久化累积，避免窗口浮动丢失） ----------
    existing_new = load_json(os.path.join(DATA, "new_projects.json"))
    # 先刷新历史已收录的新项目（保持收录，只更新 star / 失效标记）
    for full, old in list(existing_new.items()):
        try:
            m = refresh_repo(full)
            existing_new[full] = m if m.get("exists") is not False else {**old, **m}
            time.sleep(SLEEP)
        except Exception as e:
            log(f"  ! 刷新已收录新项目失败 {full}: {e}")
    collected_keys = set(collected.keys()) | set(existing_new.keys())

    new_review, weekly_new = [], []
    q = f"jev in:name,description,readme pushed:>={cutoff}"
    spath = f"search/repositories?q={q.replace(' ', '+')}&sort=updated&order=desc&per_page={SEARCH_PER_PAGE}"
    try:
        res = gh_api(spath)
        items = res.get("items", [])
        log(f"search 命中 {len(items)} 条候选")
        for it in items:
            full = it["full_name"]
            if full == SELF_FULL or full in collected_keys:
                continue
            if it.get("fork") or it.get("archived"):
                continue
            stars = it["stargazers_count"]
            if stars < MIN_STARS:
                continue
            blob = (it["name"] + " " + (it.get("description") or "")).lower()
            if any(k in blob for k in HIGH_KW):
                try:
                    meta = refresh_repo(full)
                    if meta.get("exists") is False:
                        continue
                    meta["discovered_at"] = today.isoformat()
                    meta["confidence"] = "high"
                    existing_new[full] = meta
                    weekly_new.append(full)
                except Exception as e:
                    log(f"  ! 新项目刷新失败 {full}: {e}")
            else:
                new_review.append({
                    "full_name": full, "html_url": it["html_url"],
                    "description": it.get("description") or "",
                    "stargazers_count": stars, "language": it.get("language") or "未知",
                    "pushed_at": it["pushed_at"], "created_at": it["created_at"],
                })
            time.sleep(SLEEP)
    except Exception as e:
        log(f"  ! search 失败: {e}")

    new_projects = existing_new
    save_json(os.path.join(DATA, "new_projects.json"), new_projects)
    save_json(os.path.join(DATA, "candidates.json"),
              {"review": new_review, "updated_at": today.isoformat()})
    log(f"新发现: 累积收录 {len(new_projects)} 个 (本周新增 {len(weekly_new)}), 待审 {len(new_review)} 个")

    # ---------- 3. 更新 README 新发现段 ----------
    readme_path = os.path.join(REPO, "README.md")
    with open(readme_path, encoding="utf-8") as f:
        rm = f.read()
    if new_projects:
        lines = ["_由每周自动更新脚本（`scripts/update_jev_hub.py`）经 GitHub API 实测发现，尚未做中文精排。如发现已归档或失效，欢迎提 issue / PR。_\n"]
        for full, m in sorted(new_projects.items(), key=lambda x: -x[1]["stargazers_count"]):
            lines.append(f"- [{full}]({m['html_url']}) *(⭐ {m['stargazers_count']:,})* — {m['description']}")
        if new_review:
            lines.append(f"\n_另有 {len(new_review)} 个低置信候选在 `data/candidates.json` 待人工复核。_")
        body = "\n".join(lines)
    else:
        body = "_由每周自动更新脚本（`scripts/update_jev_hub.py`）经 GitHub API 实测发现，尚未做中文精排。如发现已归档或失效，欢迎提 issue / PR。_\n"
    rm = re.sub(r"<!-- NEW_DISCOVERIES_START -->.*?<!-- NEW_DISCOVERIES_END -->",
                f"<!-- NEW_DISCOVERIES_START -->\n## 近期新发现\n\n{body}\n<!-- NEW_DISCOVERIES_END -->",
                rm, flags=re.S)
    with open(readme_path, "w", encoding="utf-8") as f:
        f.write(rm)

    # ---------- 4. 重渲 jev-collection.html ----------
    try:
        log("重渲 jev-collection.html ...")
        subprocess.run(["python3", os.path.join(BASE, "build_unified.py")],
                       cwd=REPO, capture_output=True, text=True, timeout=120, check=True)
    except Exception as e:
        log(f"  ! build_unified 失败: {e}")

    # ---------- 5. 周报 ----------
    changed = []
    for full, before in stars_before.items():
        after = collected[full].get("stargazers_count", 0)
        if after != before:
            changed.append((full, before, after))
    changed.sort(key=lambda x: -(x[2] - x[1]))
    report = []
    report.append(f"# Jev Hub 周更新报告 · {today.isoformat()}\n")
    report.append(f"## 收录数据刷新\n- 刷新项目数: {len(collected)}\n- Star 有变动: {len(changed)} 个\n")
    for full, b, a in changed[:15]:
        delta = a - b
        report.append(f"  - {full}: {b:,} → {a:,} ({'+' if delta>0 else ''}{delta:,})")
    report.append(f"\n## 本周新入选（高置信，已收录）\n- 数量: {len(weekly_new)}\n")
    for full in weekly_new:
        m = new_projects[full]
        report.append(f"  - {full} *(⭐ {m['stargazers_count']:,})* — {m['description']}")
    report.append(f"\n## 待审候选（低置信，未收录）\n- 数量: {len(new_review)}\n")
    for r in new_review[:15]:
        report.append(f"  - {r['full_name']} *(⭐ {r['stargazers_count']:,})* — {r['description']}")
    report_path = os.path.join(REPO, "weekly_report.md")
    with open(report_path, "w", encoding="utf-8") as f:
        f.write("\n".join(report) + "\n")
    log(f"周报已写: {report_path}")

    # ---------- 6. 提交推送 ----------
    if push and not dry:
        files = ["data/jev_data.json", "data/jev_data2.json", "data/new_projects.json",
                 "data/candidates.json", "jev-collection.html", "README.md", "weekly_report.md"]
        msg = f"chore: weekly jev hub update {today.isoformat()} (+{len(new_projects)} new)"
        # 仅 add 指定文件，避免误带 screenshots 等
        add = subprocess.run(["git", "add"] + files, cwd=REPO, capture_output=True, text=True)
        if add.returncode != 0:
            log(f"  ! git add 失败: {add.stderr}")
            return
        st = subprocess.run(["git", "status", "--porcelain"], cwd=REPO, capture_output=True, text=True)
        if not st.stdout.strip():
            log("无变更，跳过 commit")
            return
        cm = subprocess.run(["git", "commit", "-m", msg], cwd=REPO, capture_output=True, text=True)
        log(f"commit: {cm.stdout.strip() or cm.stderr.strip()}")
        # 用 gh token 注入远端 url，不依赖环境 git credential helper
        tok = subprocess.run(["gh", "auth", "token"], capture_output=True, text=True).stdout.strip()
        if tok:
            url = f"https://x-access-token:{tok}@github.com/supermanc417-alt/awesome-jev-hub.git"
            ps = subprocess.run(["git", "push", url], cwd=REPO, capture_output=True, text=True)
        else:
            ps = subprocess.run(["git", "push"], cwd=REPO, capture_output=True, text=True)
        log(f"push: {ps.stdout.strip() or ps.stderr.strip()}")
    else:
        log("（dry-run / 未加 --push，跳过 commit+push）")

if __name__ == "__main__":
    main()

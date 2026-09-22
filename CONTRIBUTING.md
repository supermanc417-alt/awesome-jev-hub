# Contributing to Awesome Jev Hub

感谢你为 Jev 生态补充项目。本仓库遵循 [awesome](https://awesome.re) 的策展精神：客观、可核验、机器友好。

> 本仓库为双语仓库：`README.md`（中文）+ `README_EN.md`（英文）。新增项目请**两个文件同步更新**。

## 如何新增一个项目

1. 在 `README_EN.md` 的对应分类下，按**单行**格式追加（描述取官方 `description` 原文）：

   ```markdown
   - [owner/repo](https://github.com/owner/repo) *(⭐ 123 · Python)* — Official one-line description from the repo.
   ```

2. 在 `README.md` 同一分类下追加中文条目：用**中文一句话忠实转述**官方描述（不虚构、不夸大）。
3. 归入**最合适的单一分类**（跨类时选最直接的应用域，避免重复）。
4. 同步把项目加入 `data/jev_data.json`（首批）或 `data/jev_data2.json`（扩张批），字段含 `full_name / html_url / description / stargazers_count / language / license / topics`；中文描述同步登记到 `scripts/build_unified.py` 的 `CN` 字典。
5. 如需更新可视化收藏篇，运行 `python scripts/build_unified.py` 重新生成 `jev-collection.html`。

## 收录标准

- 仓库**真实存在且公开**，GitHub API 可核验。
- 与 Jev / TypeSafe System One 模型（typed decisions、Choice/Score/Noul）直接相关。
- 非纯营销、无公开代码或无法核验的项目不收录。
- 社区清单（awesome list）请加到「社区精选清单 / Community Lists」一节，不要混入应用项目。

## 提交方式

- 直接提交 Pull Request；或在仓库开 issue 提供仓库链接 + 分类建议。
- 批量新增请保持每条独立、便于 review。

> 策展 ≠ 背书。本仓库仅做整理聚合，不代表对任一项目的质量或安全性背书。

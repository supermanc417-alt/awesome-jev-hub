# Contributing to Awesome Jev Hub

感谢你为 Jev 生态补充项目。本仓库遵循 [awesome](https://awesome.re) 的策展精神：客观、可核验、机器友好。

## 如何新增一个项目

1. 在 `README.md` 的对应方向分类下，按**单行**格式追加一条：

   ```markdown
   - [owner/repo](https://github.com/owner/repo) *(⭐ 123 · Python)* — Official one-line description from the repo.
   ```

2. 描述取自该仓库的官方 `description`，**不要改写、不要翻译**（保持可核验）。
3. 归入**最合适的单一分类**（跨类时选最直接的应用域，避免重复）。
4. 同步把项目加入 `data/jev_data.json`（首批）或 `data/jev_data2.json`（扩张批），字段含 `full_name / html_url / description / stargazers_count / language / license / topics`。
5. 如需更新可视化收藏篇，运行 `python scripts/build_unified.py` 重新生成 `jev-collection.html`。

## 收录标准

- 仓库**真实存在且公开**，GitHub API 可核验。
- 与 Jev / TypeSafe System One 模型（typed decisions、Choice/Score/Noul）直接相关。
- 非纯营销、无公开代码或无法核验的项目不收录。
- 社区清单（awesome list）请加到「社区精选清单」一节，不要混入应用项目。

## 提交方式

- 直接提交 Pull Request；或在仓库开 issue 提供仓库链接 + 分类建议。
- 批量新增请保持每条独立、便于 review。

> 策展 ≠ 背书。本仓库仅做整理聚合，不代表对任一项目的质量或安全性背书。

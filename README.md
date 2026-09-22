[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)
[![License: CC0-1.0](https://img.shields.io/badge/license-CC0_1.0-blue.svg)](LICENSE)
[![Projects](https://img.shields.io/badge/projects-51-blue.svg)](#生态项目)
[![GitHub stars](https://img.shields.io/github/stars/supermanc417-alt/awesome-jev-hub?style=social)](https://github.com/supermanc417-alt/awesome-jev-hub)

[English](README_EN.md) | 简体中文

# Awesome Jev Hub

> 一份持续维护的 **Jev / TypeSafe「System One」模型生态档案**：概念、实战项目、社区清单、数据卡与官方仓库截图。

**规模**：51 个应用项目 · 12 个方向 · 10 个社区清单 · 生态累计 ⭐ 80,428（应用 76,190 + 社区清单 4,238）

Jev 是 [TypeSafe AI](https://typesafe.ai) 的「System One」模型（概念见下方「什么是 Jev」）。本仓库把社区里基于它的实战项目按用途整理成可检索的干货档案，并附官方仓库截图。

## Contents

[什么是 Jev](#什么是-jev)
  - [浏览器与桌面自动化](#浏览器与桌面自动化)
  - [代码与上下文管理](#代码与上下文管理)
  - [集成与工具箱](#集成与工具箱)
  - [路由、技能与 Agent 调度](#路由、技能与-agent-调度)
  - [生成式 UI](#生成式-ui)
  - [Agent 框架与 Harness](#agent-框架与-harness)
  - [记忆层与运行时感知](#记忆层与运行时感知)
  - [开源复刻与兼容 Runtime](#开源复刻与兼容-runtime)
  - [交易与金融](#交易与金融)
  - [游戏、机器人与移动](#游戏、机器人与移动)
  - [搜索、数据与行业应用](#搜索、数据与行业应用)
  - [产品与创业](#产品与创业)
[社区精选清单](#社区精选清单)
[文档与数据](#文档与数据)
[收录说明](#收录说明)
[Contributing](#contributing)
[License](#license)

## 什么是 Jev

Jev 是 [TypeSafe AI](https://typesafe.ai) 的「System One」模型，定位 **fast / cheap / typed judgments**——它几乎从不直接生成内容，只负责「判断与路由」：

- **核心原语只有三个**：`Choice`（选）、`Score`（打分）、`Noul`（跳过）
- **为什么爆火**：便宜到每步可调、延迟低到能做实时决策（jev-trader 单步约 81ms）、带类型好接工程、Agent 长上下文瘦身刚需
- **官方 slogan**：`i. am. speed.`

统一范式：**Jev 只当廉价低延迟的判断/路由层**——观察 → 判断做什么/点哪/选哪个组件 → 把执行交给大模型或既有系统。把「每步都调贵模型」降为「必要时才调」。

> 🆕 标记 = 本仓库 2026-09-22 扩张批次新增的 30 个项目。

## 生态项目

按方向归并后的 51 个应用项目，描述已全部译为中文（忠实于各仓库官方说明）。星标与语言为 GitHub API 实测快照（2026-09-22）。

### 浏览器与桌面自动化

- [browser-use/jev-ultrafast](https://github.com/browser-use/jev-ultrafast) *(⭐ 16,795 · Python)* — Browser Use 做的高速浏览器 Agent。Jev 每步只判断「做什么、点哪个元素」，要打字才调小模型。Google Flights 搜一次航班约 7 秒。
- [lahfir/agent-desktop](https://github.com/lahfir/agent-desktop) *(⭐ 1,451 · Rust)* — 桌面自动化。读系统无障碍树，判断下一步该点哪个按钮、菜单或输入框。
- [wy-coliney/jev-browser-use](https://github.com/wy-coliney/jev-browser-use) *(⭐ 341 · JavaScript)* 🆕 — 比普通 browser-use 快 5–10 倍：Jev 点、Codex 想并校验，在 EZCollegeApp 实战打磨。
- [milind-soni/tiptour-macos](https://github.com/milind-soni/tiptour-macos) *(⭐ 644 · Swift)* 🆕 — 开源的本地电脑操控，macOS 上快速、本地化的 computer use，Jev 判断下一步操作。

### 代码与上下文管理

- [tamaratran/fast-jev-compaction](https://github.com/tamaratran/fast-jev-compaction) *(⭐ 6,097 · TypeScript)* — 给 Claude Code 做上下文压缩。每次工具调用先让 Jev 判断还有没有用，没用的删掉，留下来的原文不重写。
- [0xNatoshi/jev-codex-router](https://github.com/0xNatoshi/jev-codex-router) *(⭐ 188 · JavaScript)* — 先让 Jev 判断这一轮编程任务有多难，再决定模型档位、推理深度和速度模式。
- [GhalebDweikat/Winnow](https://github.com/GhalebDweikat/winnow) *(⭐ 60 · Python)* — 给 Claude Code 做上下文垃圾回收。Read / Bash / Grep 吐一大堆时，Jev 先判断哪些真和当前任务有关。
- [devagrawal09/jev-review](https://github.com/devagrawal09/jev-review) *(⭐ 511 · TypeScript)* — 代码审查前先过一遍 Jev，把高风险改动挑出来，再交给更贵的大模型或人。带本地看板。
- [ellipsis-dev/blink](https://github.com/ellipsis-dev/blink) *(⭐ 56 · TypeScript)* — 把 Jev 当代码库导航器。每走到一层目录，就判断哪些文件和当前问题最相关，再继续往下找。
- [qkal/Canny](https://github.com/qkal/Canny) *(⭐ 31 · TypeScript)* — 防 Coding Agent 嘴硬说自己做完了。看工具输出、代码 diff 和测试结果，再判断完成声明靠不靠谱。

### 集成与工具箱

- [itsmostafa/typesafe-mcp](https://github.com/itsmostafa/typesafe-mcp) *(⭐ 235 · Go)* — 把 Jev 接进 Claude Code、Claude Desktop、Codex 和 Pi，随时做 Choice / Score / Noul。
- [jkudish/jev-mcp](https://github.com/jkudish/jev-mcp) *(⭐ 255 · JavaScript)* — 现成的 Agent 判断工具箱：事实核验、内容筛查、语义排序、分类和信息提取。
- [sharziki/semdecide](https://github.com/sharziki/semdecide) *(⭐ 32 · Python)* — 把 Jev 做成命令行。Shell 里直接分类、打分、过滤，适合接爬虫、CI 和数据流水线。
- [kushals256/jevcache](https://github.com/kushals256/jevcache) *(⭐ 9 · TypeScript)* — OpenAI 兼容代理。用 Jev 判断意图是否与上次相同，命中就复用缓存、未命中才调用并缓存。

### 路由、技能与 Agent 调度

- [gargpratyush/jev-router](https://github.com/gargpratyush/jev-router) *(⭐ 320 · JavaScript)* 🆕 — 在 Claude Code 里把任务路由到最便宜的模型：Jev 判难度、选档位省钱。
- [kerpopule/hermes-jev-skills](https://github.com/kerpopule/hermes-jev-skills) *(⭐ 411 · Python)* 🆕 — 给 Hermes Agent（也支持 Claude Code / Codex）的 Jev 技能集：路由、记忆、压缩、技能选择、电脑与浏览器操作。
- [wuyoscar/jev-skill](https://github.com/wuyoscar/jev-skill) *(⭐ 397 · Python)* 🆕 — Jev 用例、workflow 与 Agent 技能的合集，想找「Jev 能干什么」直接翻。

### 生成式 UI

- [vercel-labs/json-render](https://github.com/vercel-labs/json-render) *(⭐ 17,997 · TypeScript)* — Vercel Labs 的生成式 UI 框架。Jev 不逐 token 写 JSON，只负责选组件、属性和布局。

### Agent 框架与 Harness

- [dealerdefi/Jevmind](https://github.com/dealerdefi/Jevmind) *(⭐ 164 · Python)* 🆕 — Agent 的「一个脑子、九只手」：把决策从散文抽成带信心的 typed 答案，过代码门、写进账本、再学习校准。本地毫秒级，必要时切 Jev。
- [HarnessRouter/SystemOneHarness](https://github.com/HarnessRouter/SystemOneHarness) *(⭐ 95 · Python)* 🆕 — System One 模型的 harness：观察→编译动作空间→信心门控→执行→记录，每步一次调用、无生成动作。
- [thruwire/foreman](https://github.com/thruwire/foreman) *(⭐ 483 · Python)* 🆕 — 软件工厂「工头」：基于 Jev 调度与质检代码生成流程。
- [pulseaiclub/phi](https://github.com/pulseaiclub/phi) *(⭐ 493 · Go)* 🆕 — coding agent：RPC 插件、子 Agent、hashline 编辑、MCP，Jev 充当其中的判断/路由。
- [notque/vexjoy-agent](https://github.com/notque/vexjoy-agent) *(⭐ 423 · Python)* 🆕 — VexJoy Agent：Jev 智能路由——把自然语言请求路由到对的专家 Agent，并用评审/测试/学习循环把关。
- [dabit3/jev-experiments](https://github.com/dabit3/jev-experiments) *(⭐ 362 · TypeScript)* 🆕 — 10 个 Jev 延迟向 demo 合集（commit-sentry、inbox-blitz、jev-dispatch 等），每个带 README + 截图。

### 记忆层与运行时感知

- [Asymptote-Labs/agent-beacon](https://github.com/Asymptote-Labs/agent-beacon) *(⭐ 945 · Go)* 🆕 — 跨 harness 的「自进化记忆层」，把 Agent 在不同框架间的经验与判断沉淀成可复用记忆。
- [kitfunso/hippo-memory](https://github.com/kitfunso/hippo-memory) *(⭐ 752 · TypeScript)* 🆕 — 仿生记忆：衰减、回忆强化与巩固。零依赖、SQLite、MCP；可选接 Jev 做重排。
- [reticlehq/reticle](https://github.com/reticlehq/reticle) *(⭐ 810 · TypeScript)* 🆕 — 给 Web / 桌面应用加「机器原生运行时感知」，让 Agent 理解它构建的东西到底跑成什么样。

### 开源复刻与兼容 Runtime

- [jaredpalmer/kev](https://github.com/jaredpalmer/kev) *(⭐ 2,799 · Python)* 🆕 — Jev-like 决策模型家族，基于 Qwen3.5 自己训练、本地可跑。证明「小模型做带类型的判断」不依赖 Jev 一家。
- [TianyuCodings/NanoJev](https://github.com/TianyuCodings/NanoJev) *(⭐ 1,889 · Python)* 🆕 — Jev 的 nano 复刻：并行决策 + 动态候选 + 端到端训练流水线，教学与自托管两用。
- [wfzyx/von](https://github.com/wfzyx/von) *(⭐ 393 · Python)* 🆕 — 开源的 System One 决策模型：sub-15ms、非自回归、本地可跑，作为 TypeSafe Jev 的 drop-in 替代。
- [razorback16/openjev](https://github.com/razorback16/openjev) *(⭐ 289 · Python)* 🆕 — 开源、Jev 兼容的 System One 决策服务器，基于 DiffusionGemma。
- [ekzhang/openjev-sglang](https://github.com/ekzhang/openjev-sglang) *(⭐ 259 · Python)* 🆕 — 基于开源模型的 Jev 兼容 API 端点（prefill-only），把 Jev 调用切到本地后端。
- [Rizzo-AI-Academy/rizzo-flow](https://github.com/Rizzo-AI-Academy/rizzo-flow) *(⭐ 258 · Python)* 🆕 — 对 Jev 的本地化开源实现：从 LLM 拿 typed 决策，不生成任何 token。
- [featherless-ai/simple-jev](https://github.com/featherless-ai/simple-jev) *(⭐ 463 · Python)* 🆕 — 把任意开源模型变成 classifier / jev 端点，一行配置让普通模型吐 typed 判断。

### 交易与金融

- [jarrodwatts/jev-trader](https://github.com/jarrodwatts/jev-trader) *(⭐ 1,915 · TypeScript)* — Monad 测试网上做高频做市。Jev 根据价差和成交方向判断下一步买还是卖，模型延迟约 81ms。
- [irfndi/prism-liquidity-agent](https://github.com/irfndi/prism-liquidity-agent) *(⭐ 71 · TypeScript)* — 不直接让 Jev 下单。它判断 toxic flow、市场压力、均值回归之类的状态，再交给原来的策略。
- [OpenByteInc/QuantDinger](https://github.com/OpenByteInc/QuantDinger) *(⭐ 11,970 · Python)* 🆕 — 开源 AI 交易操作系统。把 Jev 接进策略研究、回测与下单，覆盖加密货币 / 股票 / 外汇，自带多租户 SaaS 骨架。

### 游戏、机器人与移动

- [fhshaik/typesafe-mario](https://github.com/fhshaik/typesafe-mario) *(⭐ 341 · Python)* — 让 Jev 玩《超级马里奥》。不看截图，直接读模拟器 RAM 里的结构化状态，再决定跑、跳、躲。
- [RomanSlack/jev-drone](https://github.com/RomanSlack/jev-drone) *(⭐ 122 · Python)* — 拿 Jev 控无人机。底层飞控继续负责稳定和安全，Jev 只做爬升、刹车、穿越障碍这类上层判断。
- [emrickgarrett/OneVOneJev](https://github.com/emrickgarrett/OneVOneJev) *(⭐ 20 · TypeScript)* — 浏览器里的 1v1 FPS。每个决策 tick 都要判断走位、视角、瞄准、开火和跳跃。
- [rmalde/minecraft-agent](https://github.com/rmalde/minecraft-agent) *(⭐ 491 · JavaScript)* 🆕 — Minecraft 智能体：Astra 规划器 + JEV 控制器，带原生录制、已测路线与运行校验。
- [droidrun/mobile-jev](https://github.com/droidrun/mobile-jev) *(⭐ 336 · JavaScript)* 🆕 — 移动端 Agent：把 Jev 的判断层搬进 Android / iOS 自动化，决定下一步点哪。

### 搜索、数据与行业应用

- [jexp/neo4jev](https://github.com/jexp/neo4jev) *(⭐ 84 · Jupyter Notebook)* — 把 Jev 塞进知识图谱。每走到一个节点，判断下一条最值得走的边，再一路找下去。
- [AkashPriyadarshii/jev-curate](https://github.com/AkashPriyadarshii/jev-curate) *(⭐ 22 · Rust)* — 拿 Jev 筛训练数据。JSONL / Parquet 先做质量、相关性和风险判断，再决定哪些进后面的训练。
- [superagents-lab/jev-search](https://github.com/superagents-lab/jev-search) *(⭐ 391 · TypeScript)* 🆕 — 用 Jev 做网页搜索：源选择、查询理解与相关性排序，基于 Search1API。
- [realZachi/pg-jev](https://github.com/realZachi/pg-jev) *(⭐ 292 · Shell)* 🆕 — Postgres 扩展：用自然语言问表，Jev 把问题转成 SQL / 意图判断。
- [kyotofin/tax-doc-classifier](https://github.com/kyotofin/tax-doc-classifier) *(⭐ 361 · TypeScript)* 🆕 — 税务文档页分类器：基于 Jev 决策，261 张 IRS 表单上严格准确率 100%，每页约 $0.001。
- [jev-chat/jev-chat-jarvis](https://github.com/jev-chat/jev-chat-jarvis) *(⭐ 2,034 · Kotlin)* 🆕 — 装在手机上的「对话副驾」：在微信 / QQ / X / 飞书里读懂对方，给候选回复、一键填入，发不发由你。
- [samuelfaj/distill](https://github.com/samuelfaj/distill) *(⭐ 682 · Rust)* 🆕 — 让 Agent「用更少的 token 干更多的活」，把长上下文里的判断与摘要用 Jev 式决策压缩。
- [sutro-sh/jev-align](https://github.com/sutro-sh/jev-align) *(⭐ 271 · Python)* 🆕 — 用人类反馈 + Jev + GEPA 校准「AI Functions」，把你想要的决策行为对齐出来。

### 产品与创业

- [monteduro/killmyidea](https://github.com/monteduro/killmyidea) *(⭐ 80 · TypeScript)* — 输入一个创业点子，Jev 从多个维度打分，最后给你 KILL、FIX 或 SHIP。

## 社区精选清单

想跟进生态全貌、找客户端 / SDK / 框架，直接逛这几个社区清单（按 ⭐ 排序）。多个作者各自维护了同名 `awesome-jev` 清单，属生态碎片化，按需取用即可。

- [yibie/awesome-jev](https://github.com/yibie/awesome-jev) *(⭐ 1,105)* — 社区维护的 Jev 公开项目 / 集成 / 讨论总清单，按 Infra·SDK·集成分类，含大量客户端与框架链接。
- [Anil-matcha/awesome-jev-by-typesafe](https://github.com/Anil-matcha/awesome-jev-by-typesafe) *(⭐ 776)* — 有证据支撑的用例、模式、提示词与起步代码，偏「怎么把 Jev 用对」。
- [v-modal/awesome-jev-tools](https://github.com/v-modal/awesome-jev-tools) *(⭐ 632)* — 为 Jev 打造的精选工具清单，导航向。
- [AbdelStark/awesome-typesafe-jev](https://github.com/AbdelStark/awesome-typesafe-jev) *(⭐ 432)* — 源码支撑的 Jev 田野指南：SDK、在线 demo、Agent 工具与独立评测。
- [logicrw/awesome-jev-projects](https://github.com/logicrw/awesome-jev-projects) *(⭐ 342)* — 源码支撑的生态雷达，自动 GitHub 同步，发现新项目用。
- [cobanov/awesome-jev](https://github.com/cobanov/awesome-jev) *(⭐ 318)* — 社区目录式清单，已收录 155+ 源审项目，按场景分组。
- [AnotiaWang/awesome-jev](https://github.com/AnotiaWang/awesome-jev) *(⭐ 271)* — 精选的 Jev / TypeSafe System One 应用、库与资源。
- [heyjunpenn/awesome-jev](https://github.com/heyjunpenn/awesome-jev) *(⭐ 260)* — 社区维护的 Jev / System One 应用、库、资源目录。
- [kraayenjon/awesome-jev](https://github.com/kraayenjon/awesome-jev) *(⭐ 100)* — Jev 用例、项目、SDK 与资源清单（含 madewithjev 上的游戏 demo）。
- [robokrunch/awesome-jev](https://github.com/robokrunch/awesome-jev) *(⭐ 2)* — 由 RoboKrunch 维护，含真实延迟/账单实测标注。

## 文档与数据

- **`jev-collection.html`** — 完整可视化收藏篇：概念卡 + 6 张重点详解资料卡 + 51 张全景资料卡（含官方截图画廊）。在线版见 [GitHub Pages](https://supermanc417-alt.github.io/awesome-jev-hub/jev-collection.html)。
- **`data/jev_data.json`** / **`data/jev_data2.json`** — 各项目 GitHub 实测元数据（Star / 语言 / 协议 / topics / 时间）。
- **`screenshots/`** — 51 个仓库的 GitHub 实拍截图（无头 Chrome 直截，本地化）。
- **`scripts/build_unified.py`** — 由数据 JSON 生成 `jev-collection.html` 的脚本。

## 收录说明

- 51 个应用仓库 + 10 个社区清单均经 GitHub API 实测存在（快照于 2026-09-22），Star / 语言 / 协议为当日数据；中文条目描述忠实转述自各仓库官方 `description` 与社区清单上下文，未做虚构。
- Jev 即 TypeSafe AI 的 System One 模型（官方 slogan "i. am. speed."），相关能力以 [官方文档](https://typesafe.ai) 为准。
- 本仓库为「聚合型 hub」，不替代上游社区清单；如发现项目已归档 / 失效，欢迎提交 issue 或 PR。

## Contributing

欢迎补充新的 Jev 生态项目。请先阅读 [CONTRIBUTING.md](CONTRIBUTING.md)。要点：

- 一个项目一条单行条目；中文 README 用中文一句话描述（忠实于仓库官方说明），英文 README（README_EN.md）用官方 `description` 原文。
- 归入最合适的**单一**方向分类（跨类时选最直接的应用域），双语 README 同步更新。
- 提交前确认仓库真实存在且仍在维护；新仓库请附 GitHub 链接。
- 不收录纯营销、无公开代码或无法核验的项目。

## License

本仓库内容（列表与说明文字）以 [CC0 1.0](LICENSE) 公有领域 dedication 发布。仓库截图为其对应开源项目的界面缩略图，版权归原仓库所有；如使用请遵循原项目许可。

[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)
[![License: CC0-1.0](https://img.shields.io/badge/license-CC0_1.0-blue.svg)](LICENSE)
[![Projects](https://img.shields.io/badge/projects-51-blue.svg)](https://github.com/supermanc417-alt/awesome-jev-hub#生态项目)
[![GitHub stars](https://img.shields.io/github/stars/supermanc417-alt/awesome-jev-hub?style=social)](https://github.com/supermanc417-alt/awesome-jev-hub)

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

按方向归并后的 51 个应用项目。星标与语言为 GitHub API 实测快照（2026-09-22）。

### 浏览器与桌面自动化

- [browser-use/jev-ultrafast](https://github.com/browser-use/jev-ultrafast) *(⭐ 16,795 · Python)* — Fastest and cheapest web agent
- [lahfir/agent-desktop](https://github.com/lahfir/agent-desktop) *(⭐ 1,451 · Rust)* — Agent Desktop gives any agent reliable computer use on the desktop. Built with Rust, it sees any app's real UI structure through OS accessibility trees and operates it — refs stay stable and actions stay safe to retry, instead of guessing from pixels.
- [wy-coliney/jev-browser-use](https://github.com/wy-coliney/jev-browser-use) *(⭐ 341 · JavaScript)* 🆕 — 5–10x faster browser operations: Jev clicks, Codex thinks and verifies. Built at EZCollegeApp.
- [milind-soni/tiptour-macos](https://github.com/milind-soni/tiptour-macos) *(⭐ 644 · Swift)* 🆕 — Open-Source fast local computer use

### 代码与上下文管理

- [tamaratran/fast-jev-compaction](https://github.com/tamaratran/fast-jev-compaction) *(⭐ 6,097 · TypeScript)* — Claude Code plugin that replaces the compaction summary with Jev decisions: every tool call and result is scored in one fast request, stale ones are dropped or truncated, everything kept stays verbatim.
- [0xNatoshi/jev-codex-router](https://github.com/0xNatoshi/jev-codex-router) *(⭐ 188 · JavaScript)* — Per-turn model & reasoning routing for Codex, driven by Jev (TypeSafe System One): picks the model, thinking depth and speed mode for every turn.
- [GhalebDweikat/Winnow](https://github.com/GhalebDweikat/winnow) *(⭐ 60 · Python)* — A calibrated context sieve for Claude Code: every tool result is judged by a System One model before it enters context.
- [devagrawal09/jev-review](https://github.com/devagrawal09/jev-review) *(⭐ 511 · TypeScript)* — A staged code-review workflow and local dashboard built with TypeSafe Jev.
- [ellipsis-dev/blink](https://github.com/ellipsis-dev/blink) *(⭐ 56 · TypeScript)* — Codebase search powered by Jev from @typesafe-ai
- [qkal/Canny](https://github.com/qkal/Canny) *(⭐ 31 · TypeScript)* — Stops AI coding agents from claiming work is done without evidence. Deterministic hooks decide, TypeSafe's Jev advises. Append-only ledger, zero runtime dependencies.

### 集成与工具箱

- [itsmostafa/typesafe-mcp](https://github.com/itsmostafa/typesafe-mcp) *(⭐ 235 · Go)* — mcp connector to give your AI agent direct access to typesafe ai's jev model
- [jkudish/jev-mcp](https://github.com/jkudish/jev-mcp) *(⭐ 255 · JavaScript)* — Fast, cheap, typed judgments from TypeSafe's Jev model, as MCP tools.
- [sharziki/semdecide](https://github.com/sharziki/semdecide) *(⭐ 32 · Python)* — Typed semantic decisions for Unix pipelines and CI, powered by TypeSafe AI Jev.
- [kushals256/jevcache](https://github.com/kushals256/jevcache) *(⭐ 9 · TypeScript)* — Skip expensive LLM calls when TypeSafe Jev says same intent. OpenAI-compatible local cache proxy — npx @kushalicious/jevcache

### 路由、技能与 Agent 调度

- [gargpratyush/jev-router](https://github.com/gargpratyush/jev-router) *(⭐ 320 · JavaScript)* 🆕 — Route to the cheapest model in claude code for your task using jev-router
- [kerpopule/hermes-jev-skills](https://github.com/kerpopule/hermes-jev-skills) *(⭐ 411 · Python)* 🆕 — Jev-powered model routing, memory, compaction, skill selection, computer and browser use for Hermes agents (also Claude Code and Codex)
- [wuyoscar/jev-skill](https://github.com/wuyoscar/jev-skill) *(⭐ 397 · Python)* 🆕 — An awesome collection of Jev use cases, workflows, and agent skills.

### 生成式 UI

- [vercel-labs/json-render](https://github.com/vercel-labs/json-render) *(⭐ 17,997 · TypeScript)* — The Generative UI framework

### Agent 框架与 Harness

- [dealerdefi/Jevmind](https://github.com/dealerdefi/Jevmind) *(⭐ 164 · Python)* 🆕 — （暂无官方描述）
- [HarnessRouter/SystemOneHarness](https://github.com/HarnessRouter/SystemOneHarness) *(⭐ 95 · Python)* 🆕 — The system one Harness for system one models
- [thruwire/foreman](https://github.com/thruwire/foreman) *(⭐ 483 · Python)* 🆕 — Software factory foreman based on TypeSafe's Jev model
- [pulseaiclub/phi](https://github.com/pulseaiclub/phi) *(⭐ 493 · Go)* 🆕 — a coding agent, rpc plugin, sub-agents, hashline edits, and mcp
- [notque/vexjoy-agent](https://github.com/notque/vexjoy-agent) *(⭐ 423 · Python)* 🆕 — VexJoy AI Agent with Jev Intelligent Routing - /do routes plain-English requests to the right specialist agent and gates the work with reviews, tests, and a learning loop.
- [dabit3/jev-experiments](https://github.com/dabit3/jev-experiments) *(⭐ 362 · TypeScript)* 🆕 — （暂无官方描述）

### 记忆层与运行时感知

- [Asymptote-Labs/agent-beacon](https://github.com/Asymptote-Labs/agent-beacon) *(⭐ 945 · Go)* 🆕 — The cross-harness self-improving memory layer for AI agents.
- [kitfunso/hippo-memory](https://github.com/kitfunso/hippo-memory) *(⭐ 752 · TypeScript)* 🆕 — Biologically-inspired memory for AI agents. Decay, retrieval strengthening, consolidation. Zero runtime deps, SQLite, MCP. Benchmarked retrieval with an opt-in TypeSafe Jev reranker.
- [reticlehq/reticle](https://github.com/reticlehq/reticle) *(⭐ 810 · TypeScript)* 🆕 — AI agents can generate code, but still struggle to understand what they build. Reticle brings Jev-style machine-native runtime perception to web & desktop applications.

### 开源复刻与兼容 Runtime

- [jaredpalmer/kev](https://github.com/jaredpalmer/kev) *(⭐ 2,799 · Python)* 🆕 — tiny Jev-like family of decision models built on top of Qwen3.5 you can train and run on your own
- [TianyuCodings/NanoJev](https://github.com/TianyuCodings/NanoJev) *(⭐ 1,889 · Python)* 🆕 — A nano replica of Jev: parallel decisions, dynamic candidates, and an end-to-end training pipeline.
- [wfzyx/von](https://github.com/wfzyx/von) *(⭐ 393 · Python)* 🆕 — The open-source System One decision model. Sub-15ms, non-autoregressive, local drop-in alternative to TypeSafe Jev.
- [razorback16/openjev](https://github.com/razorback16/openjev) *(⭐ 289 · Python)* 🆕 — Open, Jev-compatible System One decision server on DiffusionGemma
- [ekzhang/openjev-sglang](https://github.com/ekzhang/openjev-sglang) *(⭐ 259 · Python)* 🆕 — Jev-compatible API endpoint based on open models (prefill-only)
- [Rizzo-AI-Academy/rizzo-flow](https://github.com/Rizzo-AI-Academy/rizzo-flow) *(⭐ 258 · Python)* 🆕 — The open, local take on Jev: typed decisions from an LLM, without generating a single token
- [featherless-ai/simple-jev](https://github.com/featherless-ai/simple-jev) *(⭐ 463 · Python)* 🆕 — Turn any open model into a classifier/jev endpoint

### 交易与金融

- [jarrodwatts/jev-trader](https://github.com/jarrodwatts/jev-trader) *(⭐ 1,915 · TypeScript)* — One AI trade decision every Monad block. Jev on Kuru MON-USDC.
- [irfndi/prism-liquidity-agent](https://github.com/irfndi/prism-liquidity-agent) *(⭐ 71 · TypeScript)* — Autonomous LP trading agent - auto-rebalancing with backtested strategies - Currently support Meteora DLMM
- [OpenByteInc/QuantDinger](https://github.com/OpenByteInc/QuantDinger) *(⭐ 11,970 · Python)* 🆕 — Open-source AI Trading OS, agent trading, and vibe trading, with Jev System One integration. Research, build Python strategies, backtest, and paper/live trade across crypto, stocks, and forex. Launch your own multi-tenant trading SaaS with built-in user management, billing, payments, and settlement.

### 游戏、机器人与移动

- [fhshaik/typesafe-mario](https://github.com/fhshaik/typesafe-mario) *(⭐ 341 · Python)* — A TypeSafe/Jev agent that plays Super Mario Bros. from structured emulator state.
- [RomanSlack/jev-drone](https://github.com/RomanSlack/jev-drone) *(⭐ 122 · Python)* — Camera-only autonomous drone in MuJoCo with a small judgment model (TypeSafe Jev) in the loop at 2.5Hz
- [emrickgarrett/OneVOneJev](https://github.com/emrickgarrett/OneVOneJev) *(⭐ 20 · TypeScript)* — 1v1 Jev quickscope arena — Three.js + TypeSafe System One
- [rmalde/minecraft-agent](https://github.com/rmalde/minecraft-agent) *(⭐ 491 · JavaScript)* 🆕 — Astra planner and JEV controller for Minecraft, with native recording, tested routes, and run verification.
- [droidrun/mobile-jev](https://github.com/droidrun/mobile-jev) *(⭐ 336 · JavaScript)* 🆕 — （暂无官方描述）

### 搜索、数据与行业应用

- [jexp/neo4jev](https://github.com/jexp/neo4jev) *(⭐ 84 · Jupyter Notebook)* — Typesafe.ai System One Model Jev navigating a Neo4j graph by using a classifier over neighbouring relationships
- [AkashPriyadarshii/jev-curate](https://github.com/AkashPriyadarshii/jev-curate) *(⭐ 22 · Rust)* — High-throughput synthetic and pretraining dataset sifter for TypeSafe Jev. Rust streaming core, Parquet and JSONL I/O, typed Choice/Score/Noul judgments, speculative fan-out, 24.0 rows/sec measured.
- [superagents-lab/jev-search](https://github.com/superagents-lab/jev-search) *(⭐ 391 · TypeScript)* 🆕 — Search the web with TypeSafe's Jev: source selection, query understanding and relevance ranking. Built with Search1API.
- [realZachi/pg-jev](https://github.com/realZachi/pg-jev) *(⭐ 292 · Shell)* 🆕 — Ask your Postgres tables questions in plain language. A PostgreSQL extension powered by TypeSafe's Jev.
- [kyotofin/tax-doc-classifier](https://github.com/kyotofin/tax-doc-classifier) *(⭐ 361 · TypeScript)* 🆕 — Tax document page classifier built on Jev decisions. 100% strict accuracy across 261 IRS forms, ~$0.001 per page.
- [jev-chat/jev-chat-jarvis](https://github.com/jev-chat/jev-chat-jarvis) *(⭐ 2,034 · Kotlin)* 🆕 — 装在手机上的对话副驾：在微信 / QQ / X / 飞书里读懂对方、给出候选回复、一键填入输入框，发不发由你。非侵入，只读屏幕，不 hook 不改包。
- [samuelfaj/distill](https://github.com/samuelfaj/distill) *(⭐ 682 · Rust)* 🆕 — Get FAR MORE done with FAR FEWER tokens 🔥
- [sutro-sh/jev-align](https://github.com/sutro-sh/jev-align) *(⭐ 271 · Python)* 🆕 — Build calibrated AI Functions from human feedback using Jev and GEPA.

### 产品与创业

- [monteduro/killmyidea](https://github.com/monteduro/killmyidea) *(⭐ 80 · TypeScript)* — Describe your startup idea. Jev decides: kill it, fix it or ship it.

## 社区精选清单

想跟进生态全貌、找客户端 / SDK / 框架，直接逛这几个社区清单（按 ⭐ 排序，均为 GitHub 仓库）。注意：多个作者各自维护了同名 `awesome-jev` 清单，属生态碎片化，按需取用即可。

- [yibie/awesome-jev](https://github.com/yibie/awesome-jev) *(⭐ 1,105)* — A curated list of public projects, integrations, and discussions built on Jev — TypeSafe AI's System One model for typed decisions.
- [Anil-matcha/awesome-jev-by-typesafe](https://github.com/Anil-matcha/awesome-jev-by-typesafe) *(⭐ 776)* — Evidence-backed use cases, patterns, prompts, and starter code for TypeSafe Jev — a System One model for fast, typed, confidence-aware decisions in software.
- [v-modal/awesome-jev-tools](https://github.com/v-modal/awesome-jev-tools) *(⭐ 632)* — A curated list of tools  built for Jev — TypeSafe AI's System One model for typed decisions.
- [AbdelStark/awesome-typesafe-jev](https://github.com/AbdelStark/awesome-typesafe-jev) *(⭐ 432)* — Awesome Jev: a source-backed field guide to TypeSafe's System One model, with SDKs, live demos, agent tools, and independent evaluations.
- [logicrw/awesome-jev-projects](https://github.com/logicrw/awesome-jev-projects) *(⭐ 342)* — Awesome Jev: source-backed open-source ecosystem radar, plain-language project discovery, and automatic GitHub sync
- [cobanov/awesome-jev](https://github.com/cobanov/awesome-jev) *(⭐ 318)* — A curated, source-backed list of projects built with Jev, TypeSafe AI's System One model for typed decisions.
- [AnotiaWang/awesome-jev](https://github.com/AnotiaWang/awesome-jev) *(⭐ 271)* — A curated list of awesome Jev / TypeSafe System One applications, libraries, and resources.
- [heyjunpenn/awesome-jev](https://github.com/heyjunpenn/awesome-jev) *(⭐ 260)* — A verified, community-maintained catalog of 640 open-source projects built with Jev.
- [kraayenjon/awesome-jev](https://github.com/kraayenjon/awesome-jev) *(⭐ 100)* — A curated list of Jev use cases, projects, SDKs, and resources. Jev is TypeSafe AI's System One model for fast, typed decisions in software — Choice, Score, and Noul with calibrated probabilities.
- [robokrunch/awesome-jev](https://github.com/robokrunch/awesome-jev) *(⭐ 2)* — A curated list of resources for Jev — TypeSafe AI's System One decision model. Maintained by RoboKrunch.

## 文档与数据

- **`jev-collection.html`** — 完整可视化收藏篇：概念卡 + 6 张重点详解资料卡 + 51 张全景资料卡（含官方截图画廊）。在线版见 [GitHub Pages](https://supermanc417-alt.github.io/awesome-jev-hub/jev-collection.html)。
- **`data/jev_data.json`** / **`data/jev_data2.json`** — 各项目 GitHub 实测元数据（Star / 语言 / 协议 / topics / 时间）。
- **`screenshots/`** — 51 个仓库的 GitHub 实拍截图（无头 Chrome 直截，本地化）。
- **`scripts/build_unified.py`** — 由数据 JSON 生成 `jev-collection.html` 的脚本。

## 收录说明

- 51 个应用仓库 + 10 个社区清单均经 GitHub API 实测存在（快照于 2026-09-22），Star / 语言 / 协议为实时数据；条目描述取自各仓库的官方 `description`，未做改写。
- Jev 即 TypeSafe AI 的 System One 模型（官方 slogan "i. am. speed."），相关能力以 [官方文档](https://typesafe.ai) 为准。
- 本仓库为「聚合型 hub」，不替代上游社区清单；如发现项目已归档 / 失效，欢迎提交 issue 或 PR。

## Contributing

欢迎补充新的 Jev 生态项目。请先阅读 [CONTRIBUTING.md](CONTRIBUTING.md)。要点：

- 一个项目一条 `- [owner/repo](url) *(⭐ N · Lang)* — 官方描述。` ，保持单行、描述取自仓库官方 `description`。
- 归入最合适的**单一**方向分类（跨类时选最直接的应用域）。
- 提交前确认仓库真实存在且仍在维护；新仓库请附 GitHub 链接。
- 不收录纯营销、无公开代码或无法核验的项目。

## License

本仓库内容（列表与说明文字）以 [CC0 1.0](LICENSE) 公有领域 dedication 发布。仓库截图为其对应开源项目的界面缩略图，版权归原仓库所有；如使用请遵循原项目许可。

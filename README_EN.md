English | [简体中文](README.md)

[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)
[![License: CC0-1.0](https://img.shields.io/badge/license-CC0_1.0-blue.svg)](LICENSE)
[![Projects](https://img.shields.io/badge/projects-51-blue.svg)](#projects)
[![GitHub stars](https://img.shields.io/github/stars/supermanc417-alt/awesome-jev-hub?style=social)](https://github.com/supermanc417-alt/awesome-jev-hub)

# Awesome Jev Hub

> A continuously maintained **hub for the Jev / TypeSafe "System One" model ecosystem**: concepts, real-world projects, community lists, data cards, and official repo screenshots.

**Scale**: 51 app projects · 12 categories · 10 community lists · 80,428 total ⭐ (apps 76,190 + lists 4,238)

Jev is the "System One" model from [TypeSafe AI](https://typesafe.ai). This repo curates community projects built on top of it into a searchable, verifiable archive — with official repo screenshots.

## Contents

[What is Jev](#what-is-jev)
  - [Browser & Desktop Automation](#browser--desktop-automation)
  - [Code & Context Management](#code--context-management)
  - [Integrations & Toolkits](#integrations--toolkits)
  - [Routing, Skills & Agent Orchestration](#routing-skills--agent-orchestration)
  - [Generative UI](#generative-ui)
  - [Agent Frameworks & Harnesses](#agent-frameworks--harnesses)
  - [Memory & Runtime Awareness](#memory--runtime-awareness)
  - [Open-Source Replicas & Compatible Runtimes](#open-source-replicas--compatible-runtimes)
  - [Trading & Finance](#trading--finance)
  - [Gaming, Robotics & Mobile](#gaming-robotics--mobile)
  - [Search, Data & Industry Apps](#search-data--industry-apps)
  - [Products & Startups](#products--startups)
[Community Lists](#community-lists)
[Docs & Data](#docs--data)
[Inclusion Notes](#inclusion-notes)
[Contributing](#contributing)
[License](#license)

## What is Jev

Jev is the "System One" model from [TypeSafe AI](https://typesafe.ai), positioned as **fast / cheap / typed judgments** — it almost never generates content; it only *judges and routes*:

- **Three core primitives**: `Choice` (pick one), `Score` (rate it), `Noul` (skip — not worth it)
- **Why it exploded**: cheap enough to call at every step, fast enough for real-time decisions (~81ms per step in jev-trader), typed outputs that are easy to wire into engineering, and a perfect fix for the Agent long-context cost problem
- **Official slogan**: `i. am. speed.`

The shared pattern: **Jev acts as the cheap, low-latency judgment/routing layer** — observe → decide what to do / where to click / which component → hand execution to a large model or the underlying system. This turns "call an expensive model every step" into "call it only when needed".

> 🆕 marks the 30 projects added in the 2026-09-22 expansion batch.

## Projects

51 app projects grouped by category. Descriptions are quoted from each repo's official `description`. Stars/languages are a GitHub API snapshot (2026-09-22).

### Browser & Desktop Automation

- [browser-use/jev-ultrafast](https://github.com/browser-use/jev-ultrafast) *(⭐ 16,795 · Python)* — Fastest and cheapest web agent
- [lahfir/agent-desktop](https://github.com/lahfir/agent-desktop) *(⭐ 1,451 · Rust)* — Agent Desktop gives any agent reliable computer use on the desktop. Built with Rust, it sees any app's real UI structure through OS accessibility trees and operates it — refs stay stable and actions stay safe to retry, instead of guessing from pixels.
- [wy-coliney/jev-browser-use](https://github.com/wy-coliney/jev-browser-use) *(⭐ 341 · JavaScript)* 🆕 — 5–10x faster browser operations: Jev clicks, Codex thinks and verifies. Built at EZCollegeApp.
- [milind-soni/tiptour-macos](https://github.com/milind-soni/tiptour-macos) *(⭐ 644 · Swift)* 🆕 — Open-Source fast local computer use

### Code & Context Management

- [tamaratran/fast-jev-compaction](https://github.com/tamaratran/fast-jev-compaction) *(⭐ 6,097 · TypeScript)* — Claude Code plugin that replaces the compaction summary with Jev decisions: every tool call and result is scored in one fast request, stale ones are dropped or truncated, everything kept stays verbatim.
- [0xNatoshi/jev-codex-router](https://github.com/0xNatoshi/jev-codex-router) *(⭐ 188 · JavaScript)* — Per-turn model & reasoning routing for Codex, driven by Jev (TypeSafe System One): picks the model, thinking depth and speed mode for every turn.
- [GhalebDweikat/Winnow](https://github.com/GhalebDweikat/winnow) *(⭐ 60 · Python)* — A calibrated context sieve for Claude Code: every tool result is judged by a System One model before it enters context.
- [devagrawal09/jev-review](https://github.com/devagrawal09/jev-review) *(⭐ 511 · TypeScript)* — A staged code-review workflow and local dashboard built with TypeSafe Jev.
- [ellipsis-dev/blink](https://github.com/ellipsis-dev/blink) *(⭐ 56 · TypeScript)* — Codebase search powered by Jev from @typesafe-ai
- [qkal/Canny](https://github.com/qkal/Canny) *(⭐ 31 · TypeScript)* — Stops AI coding agents from claiming work is done without evidence. Deterministic hooks decide, TypeSafe's Jev advises. Append-only ledger, zero runtime dependencies.

### Integrations & Toolkits

- [itsmostafa/typesafe-mcp](https://github.com/itsmostafa/typesafe-mcp) *(⭐ 235 · Go)* — mcp connector to give your AI agent direct access to typesafe ai's jev model
- [jkudish/jev-mcp](https://github.com/jkudish/jev-mcp) *(⭐ 255 · JavaScript)* — Fast, cheap, typed judgments from TypeSafe's Jev model, as MCP tools.
- [sharziki/semdecide](https://github.com/sharziki/semdecide) *(⭐ 32 · Python)* — Typed semantic decisions for Unix pipelines and CI, powered by TypeSafe AI Jev.
- [kushals256/jevcache](https://github.com/kushals256/jevcache) *(⭐ 9 · TypeScript)* — Skip expensive LLM calls when TypeSafe Jev says same intent. OpenAI-compatible local cache proxy — npx @kushalicious/jevcache

### Routing, Skills & Agent Orchestration

- [gargpratyush/jev-router](https://github.com/gargpratyush/jev-router) *(⭐ 320 · JavaScript)* 🆕 — Route to the cheapest model in claude code for your task using jev-router
- [kerpopule/hermes-jev-skills](https://github.com/kerpopule/hermes-jev-skills) *(⭐ 411 · Python)* 🆕 — Jev-powered model routing, memory, compaction, skill selection, computer and browser use for Hermes agents (also Claude Code and Codex)
- [wuyoscar/jev-skill](https://github.com/wuyoscar/jev-skill) *(⭐ 397 · Python)* 🆕 — An awesome collection of Jev use cases, workflows, and agent skills.

### Generative UI

- [vercel-labs/json-render](https://github.com/vercel-labs/json-render) *(⭐ 17,997 · TypeScript)* — The Generative UI framework

### Agent Frameworks & Harnesses

- [dealerdefi/Jevmind](https://github.com/dealerdefi/Jevmind) *(⭐ 164 · Python)* 🆕 — No official description.
- [HarnessRouter/SystemOneHarness](https://github.com/HarnessRouter/SystemOneHarness) *(⭐ 95 · Python)* 🆕 — The system one Harness for system one models
- [thruwire/foreman](https://github.com/thruwire/foreman) *(⭐ 483 · Python)* 🆕 — Software factory foreman based on TypeSafe's Jev model
- [pulseaiclub/phi](https://github.com/pulseaiclub/phi) *(⭐ 493 · Go)* 🆕 — a coding agent, rpc plugin, sub-agents, hashline edits, and mcp
- [notque/vexjoy-agent](https://github.com/notque/vexjoy-agent) *(⭐ 423 · Python)* 🆕 — VexJoy AI Agent with Jev Intelligent Routing - /do routes plain-English requests to the right specialist agent and gates the work with reviews, tests, and a learning loop.
- [dabit3/jev-experiments](https://github.com/dabit3/jev-experiments) *(⭐ 362 · TypeScript)* 🆕 — No official description.

### Memory & Runtime Awareness

- [Asymptote-Labs/agent-beacon](https://github.com/Asymptote-Labs/agent-beacon) *(⭐ 945 · Go)* 🆕 — The cross-harness self-improving memory layer for AI agents.
- [kitfunso/hippo-memory](https://github.com/kitfunso/hippo-memory) *(⭐ 752 · TypeScript)* 🆕 — Biologically-inspired memory for AI agents. Decay, retrieval strengthening, consolidation. Zero runtime deps, SQLite, MCP. Benchmarked retrieval with an opt-in TypeSafe Jev reranker.
- [reticlehq/reticle](https://github.com/reticlehq/reticle) *(⭐ 810 · TypeScript)* 🆕 — AI agents can generate code, but still struggle to understand what they build. Reticle brings Jev-style machine-native runtime perception to web & desktop applications.

### Open-Source Replicas & Compatible Runtimes

- [jaredpalmer/kev](https://github.com/jaredpalmer/kev) *(⭐ 2,799 · Python)* 🆕 — tiny Jev-like family of decision models built on top of Qwen3.5 you can train and run on your own
- [TianyuCodings/NanoJev](https://github.com/TianyuCodings/NanoJev) *(⭐ 1,889 · Python)* 🆕 — A nano replica of Jev: parallel decisions, dynamic candidates, and an end-to-end training pipeline.
- [wfzyx/von](https://github.com/wfzyx/von) *(⭐ 393 · Python)* 🆕 — The open-source System One decision model. Sub-15ms, non-autoregressive, local drop-in alternative to TypeSafe Jev.
- [razorback16/openjev](https://github.com/razorback16/openjev) *(⭐ 289 · Python)* 🆕 — Open, Jev-compatible System One decision server on DiffusionGemma
- [ekzhang/openjev-sglang](https://github.com/ekzhang/openjev-sglang) *(⭐ 259 · Python)* 🆕 — Jev-compatible API endpoint based on open models (prefill-only)
- [Rizzo-AI-Academy/rizzo-flow](https://github.com/Rizzo-AI-Academy/rizzo-flow) *(⭐ 258 · Python)* 🆕 — The open, local take on Jev: typed decisions from an LLM, without generating a single token
- [featherless-ai/simple-jev](https://github.com/featherless-ai/simple-jev) *(⭐ 463 · Python)* 🆕 — Turn any open model into a classifier/jev endpoint

### Trading & Finance

- [jarrodwatts/jev-trader](https://github.com/jarrodwatts/jev-trader) *(⭐ 1,915 · TypeScript)* — One AI trade decision every Monad block. Jev on Kuru MON-USDC.
- [irfndi/prism-liquidity-agent](https://github.com/irfndi/prism-liquidity-agent) *(⭐ 71 · TypeScript)* — Autonomous LP trading agent - auto-rebalancing with backtested strategies - Currently support Meteora DLMM
- [OpenByteInc/QuantDinger](https://github.com/OpenByteInc/QuantDinger) *(⭐ 11,970 · Python)* 🆕 — Open-source AI Trading OS, agent trading, and vibe trading, with Jev System One integration. Research, build Python strategies, backtest, and paper/live trade across crypto, stocks, and forex. Launch your own multi-tenant trading SaaS with built-in user management, billing, payments, and settlement.

### Gaming, Robotics & Mobile

- [fhshaik/typesafe-mario](https://github.com/fhshaik/typesafe-mario) *(⭐ 341 · Python)* — A TypeSafe/Jev agent that plays Super Mario Bros. from structured emulator state.
- [RomanSlack/jev-drone](https://github.com/RomanSlack/jev-drone) *(⭐ 122 · Python)* — Camera-only autonomous drone in MuJoCo with a small judgment model (TypeSafe Jev) in the loop at 2.5Hz
- [emrickgarrett/OneVOneJev](https://github.com/emrickgarrett/OneVOneJev) *(⭐ 20 · TypeScript)* — 1v1 Jev quickscope arena — Three.js + TypeSafe System One
- [rmalde/minecraft-agent](https://github.com/rmalde/minecraft-agent) *(⭐ 491 · JavaScript)* 🆕 — Astra planner and JEV controller for Minecraft, with native recording, tested routes, and run verification.
- [droidrun/mobile-jev](https://github.com/droidrun/mobile-jev) *(⭐ 336 · JavaScript)* 🆕 — No official description.

### Search, Data & Industry Apps

- [jexp/neo4jev](https://github.com/jexp/neo4jev) *(⭐ 84 · Jupyter Notebook)* — Typesafe.ai System One Model Jev navigating a Neo4j graph by using a classifier over neighbouring relationships
- [AkashPriyadarshii/jev-curate](https://github.com/AkashPriyadarshii/jev-curate) *(⭐ 22 · Rust)* — High-throughput synthetic and pretraining dataset sifter for TypeSafe Jev. Rust streaming core, Parquet and JSONL I/O, typed Choice/Score/Noul judgments, speculative fan-out, 24.0 rows/sec measured.
- [superagents-lab/jev-search](https://github.com/superagents-lab/jev-search) *(⭐ 391 · TypeScript)* 🆕 — Search the web with TypeSafe's Jev: source selection, query understanding and relevance ranking. Built with Search1API.
- [realZachi/pg-jev](https://github.com/realZachi/pg-jev) *(⭐ 292 · Shell)* 🆕 — Ask your Postgres tables questions in plain language. A PostgreSQL extension powered by TypeSafe's Jev.
- [kyotofin/tax-doc-classifier](https://github.com/kyotofin/tax-doc-classifier) *(⭐ 361 · TypeScript)* 🆕 — Tax document page classifier built on Jev decisions. 100% strict accuracy across 261 IRS forms, ~$0.001 per page.
- [jev-chat/jev-chat-jarvis](https://github.com/jev-chat/jev-chat-jarvis) *(⭐ 2,034 · Kotlin)* 🆕 — 装在手机上的对话副驾：在微信 / QQ / X / 飞书里读懂对方、给出候选回复、一键填入输入框，发不发由你。非侵入，只读屏幕，不 hook 不改包。
- [samuelfaj/distill](https://github.com/samuelfaj/distill) *(⭐ 682 · Rust)* 🆕 — Get FAR MORE done with FAR FEWER tokens 🔥
- [sutro-sh/jev-align](https://github.com/sutro-sh/jev-align) *(⭐ 271 · Python)* 🆕 — Build calibrated AI Functions from human feedback using Jev and GEPA.

### Products & Startups

- [monteduro/killmyidea](https://github.com/monteduro/killmyidea) *(⭐ 80 · TypeScript)* — Describe your startup idea. Jev decides: kill it, fix it or ship it.

## Community Lists

To keep up with the ecosystem, these community-curated lists (sorted by ⭐) are the fastest path. Note: several independently maintained lists share the name `awesome-jev` — ecosystem fragmentation, pick what fits.

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

## Docs & Data

- **`jev-collection.html`** — The full visual collection: concept cards + 6 featured deep-dive cards + 51 panoramic data cards (with official screenshot gallery). Live version on [GitHub Pages](https://supermanc417-alt.github.io/awesome-jev-hub/jev-collection.html).
- **`data/jev_data.json`** / **`data/jev_data2.json`** — GitHub-verified metadata per project (stars / language / license / topics / timestamps).
- **`screenshots/`** — 51 headless-Chrome screenshots of the repo pages.
- **`scripts/build_unified.py`** — Script that regenerates `jev-collection.html` from the data JSON.

## Inclusion Notes

- All 51 app repos + 10 community lists were verified to exist via the GitHub API (snapshot 2026-09-22); stars / languages / licenses are from that day.
- Jev is the System One model by TypeSafe AI (slogan "i. am. speed."); capabilities per the [official docs](https://typesafe.ai).
- This is a curation hub and does not replace upstream community lists. Found an archived / dead project? Open an issue or PR.

## Contributing

New Jev ecosystem projects are welcome. Please read [CONTRIBUTING.md](CONTRIBUTING.md) first. Key rules:

- One single-line entry per project; `README_EN.md` uses the official `description` verbatim, the Chinese `README.md` uses a faithful Chinese one-liner.
- Pick the **single** most fitting category; keep both language READMEs in sync.
- Verify the repo exists and is maintained before submitting.
- No pure marketing, closed-source, or unverifiable projects.

## License

This repository's content (lists and prose) is released under [CC0 1.0](LICENSE) (public domain). Screenshots are thumbnails of the respective open-source projects; their rights remain with the original repos.

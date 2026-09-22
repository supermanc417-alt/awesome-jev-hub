# -*- coding: utf-8 -*-
"""统一重构：把 21+30 应用项目合并为一个「全景资料卡」板块（统一 12 类），
两段画廊合并为一段，社区清单单列。基于刷新后的 jev_data.json / jev_data2.json。"""
import json, os

BASE = os.path.dirname(os.path.abspath(__file__))
with open(os.path.join(BASE, "jev_data.json")) as f: DATA = json.load(f)
with open(os.path.join(BASE, "jev_data2.json")) as f: D2 = json.load(f)

def lic(d): return d.get("license") or "未声明"
def stars(n): return f"{n:,}"

# ---- 统一 12 类（21 batch1 + 30 batch2 = 51 应用）----
CAT = {
 "浏览器 / 桌面自动化": ["browser-use/jev-ultrafast","lahfir/agent-desktop","wy-coliney/jev-browser-use","milind-soni/tiptour-macos"],
 "代码 / 上下文管理": ["tamaratran/fast-jev-compaction","0xNatoshi/jev-codex-router","GhalebDweikat/Winnow","devagrawal09/jev-review","ellipsis-dev/blink","qkal/Canny"],
 "集成 / 工具箱 (MCP & CLI)": ["itsmostafa/typesafe-mcp","jkudish/jev-mcp","sharziki/semdecide","kushals256/jevcache"],
 "路由 / 技能 / Agent 调度": ["gargpratyush/jev-router","kerpopule/hermes-jev-skills","wuyoscar/jev-skill"],
 "生成式 UI": ["vercel-labs/json-render"],
 "Agent 框架 / Harness": ["dealerdefi/Jevmind","HarnessRouter/SystemOneHarness","thruwire/foreman","pulseaiclub/phi","notque/vexjoy-agent","dabit3/jev-experiments"],
 "记忆层 / 运行时感知": ["Asymptote-Labs/agent-beacon","kitfunso/hippo-memory","reticlehq/reticle"],
 "开源复刻 / 兼容 Runtime": ["jaredpalmer/kev","TianyuCodings/NanoJev","wfzyx/von","razorback16/openjev","ekzhang/openjev-sglang","Rizzo-AI-Academy/rizzo-flow","featherless-ai/simple-jev"],
 "交易 / 金融": ["jarrodwatts/jev-trader","irfndi/prism-liquidity-agent","OpenByteInc/QuantDinger"],
 "游戏 / 机器人 / 移动": ["fhshaik/typesafe-mario","RomanSlack/jev-drone","emrickgarrett/OneVOneJev","rmalde/minecraft-agent","droidrun/mobile-jev"],
 "搜索 / 数据 / 行业应用": ["jexp/neo4jev","AkashPriyadarshii/jev-curate","superagents-lab/jev-search","realZachi/pg-jev","kyotofin/tax-doc-classifier","jev-chat/jev-chat-jarvis","samuelfaj/distill","sutro-sh/jev-align"],
 "产品 / 创业": ["monteduro/killmyidea"],
}
EXPANSION = {
 "jaredpalmer/kev","TianyuCodings/NanoJev","wfzyx/von","razorback16/openjev","ekzhang/openjev-sglang",
 "Rizzo-AI-Academy/rizzo-flow","featherless-ai/simple-jev","dealerdefi/Jevmind","HarnessRouter/SystemOneHarness",
 "thruwire/foreman","pulseaiclub/phi","notque/vexjoy-agent","dabit3/jev-experiments","Asymptote-Labs/agent-beacon",
 "kitfunso/hippo-memory","reticlehq/reticle","gargpratyush/jev-router","kerpopule/hermes-jev-skills","wuyoscar/jev-skill",
 "superagents-lab/jev-search","realZachi/pg-jev","kyotofin/tax-doc-classifier","jev-chat/jev-chat-jarvis","samuelfaj/distill",
 "sutro-sh/jev-align","OpenByteInc/QuantDinger","rmalde/minecraft-agent","wy-coliney/jev-browser-use","droidrun/mobile-jev","milind-soni/tiptour-macos"
}

# ---- 中文描述 / 上手 / 注意（合并两批）----
CN = {
 "browser-use/jev-ultrafast":"Browser Use 做的高速浏览器 Agent。Jev 每步只判断「做什么、点哪个元素」，要打字才调小模型。Google Flights 搜一次航班约 7 秒。",
 "tamaratran/fast-jev-compaction":"给 Claude Code 做上下文压缩。每次工具调用先让 Jev 判断还有没有用，没用的删掉，留下来的原文不重写。",
 "vercel-labs/json-render":"Vercel Labs 的生成式 UI 框架。Jev 不逐 token 写 JSON，只负责选组件、属性和布局。",
 "itsmostafa/typesafe-mcp":"把 Jev 接进 Claude Code、Claude Desktop、Codex 和 Pi，随时做 Choice / Score / Noul。",
 "jkudish/jev-mcp":"现成的 Agent 判断工具箱：事实核验、内容筛查、语义排序、分类和信息提取。",
 "sharziki/semdecide":"把 Jev 做成命令行。Shell 里直接分类、打分、过滤，适合接爬虫、CI 和数据流水线。",
 "0xNatoshi/jev-codex-router":"先让 Jev 判断这一轮编程任务有多难，再决定模型档位、推理深度和速度模式。",
 "GhalebDweikat/Winnow":"给 Claude Code 做上下文垃圾回收。Read / Bash / Grep 吐一大堆时，Jev 先判断哪些真和当前任务有关。",
 "devagrawal09/jev-review":"代码审查前先过一遍 Jev，把高风险改动挑出来，再交给更贵的大模型或人。带本地看板。",
 "ellipsis-dev/blink":"把 Jev 当代码库导航器。每走到一层目录，就判断哪些文件和当前问题最相关，再继续往下找。",
 "lahfir/agent-desktop":"桌面自动化。读系统无障碍树，判断下一步该点哪个按钮、菜单或输入框。",
 "fhshaik/typesafe-mario":"让 Jev 玩《超级马里奥》。不看截图，直接读模拟器 RAM 里的结构化状态，再决定跑、跳、躲。",
 "RomanSlack/jev-drone":"拿 Jev 控无人机。底层飞控继续负责稳定和安全，Jev 只做爬升、刹车、穿越障碍这类上层判断。",
 "emrickgarrett/OneVOneJev":"浏览器里的 1v1 FPS。每个决策 tick 都要判断走位、视角、瞄准、开火和跳跃。",
 "jarrodwatts/jev-trader":"Monad 测试网上做高频做市。Jev 根据价差和成交方向判断下一步买还是卖，模型延迟约 81ms。",
 "irfndi/prism-liquidity-agent":"不直接让 Jev 下单。它判断 toxic flow、市场压力、均值回归之类的状态，再交给原来的策略。",
 "jexp/neo4jev":"把 Jev 塞进知识图谱。每走到一个节点，判断下一条最值得走的边，再一路找下去。",
 "AkashPriyadarshii/jev-curate":"拿 Jev 筛训练数据。JSONL / Parquet 先做质量、相关性和风险判断，再决定哪些进后面的训练。",
 "qkal/Canny":"防 Coding Agent 嘴硬说自己做完了。看工具输出、代码 diff 和测试结果，再判断完成声明靠不靠谱。",
 "monteduro/killmyidea":"输入一个创业点子，Jev 从多个维度打分，最后给你 KILL、FIX 或 SHIP。",
 "kushals256/jevcache":"OpenAI 兼容代理。用 Jev 判断意图是否与上次相同，命中就复用缓存、未命中才调用并缓存。",
}
CN.update({
 "jaredpalmer/kev":"Jev-like 决策模型家族，基于 Qwen3.5 自己训练、本地可跑。证明「小模型做带类型的判断」不依赖 Jev 一家。",
 "TianyuCodings/NanoJev":"Jev 的 nano 复刻：并行决策 + 动态候选 + 端到端训练流水线，教学与自托管两用。",
 "wfzyx/von":"开源的 System One 决策模型：sub-15ms、非自回归、本地可跑，作为 TypeSafe Jev 的 drop-in 替代。",
 "razorback16/openjev":"开源、Jev 兼容的 System One 决策服务器，基于 DiffusionGemma。",
 "ekzhang/openjev-sglang":"基于开源模型的 Jev 兼容 API 端点（prefill-only），把 Jev 调用切到本地后端。",
 "Rizzo-AI-Academy/rizzo-flow":"对 Jev 的本地化开源实现：从 LLM 拿 typed 决策，不生成任何 token。",
 "featherless-ai/simple-jev":"把任意开源模型变成 classifier / jev 端点，一行配置让普通模型吐 typed 判断。",
 "dealerdefi/Jevmind":"Agent 的「一个脑子、九只手」：把决策从散文抽成带信心的 typed 答案，过代码门、写进账本、再学习校准。本地毫秒级，必要时切 Jev。",
 "HarnessRouter/SystemOneHarness":"System One 模型的 harness：观察→编译动作空间→信心门控→执行→记录，每步一次调用、无生成动作。",
 "thruwire/foreman":"软件工厂「工头」：基于 Jev 调度与质检代码生成流程。",
 "pulseaiclub/phi":"coding agent：RPC 插件、子 Agent、hashline 编辑、MCP，Jev 充当其中的判断/路由。",
 "notque/vexjoy-agent":"VexJoy Agent：Jev 智能路由——把自然语言请求路由到对的专家 Agent，并用评审/测试/学习循环把关。",
 "dabit3/jev-experiments":"10 个 Jev 延迟向 demo 合集（commit-sentry、inbox-blitz、jev-dispatch 等），每个带 README + 截图。",
 "Asymptote-Labs/agent-beacon":"跨 harness 的「自进化记忆层」，把 Agent 在不同框架间的经验与判断沉淀成可复用记忆。",
 "kitfunso/hippo-memory":"仿生记忆：衰减、回忆强化与巩固。零依赖、SQLite、MCP；可选接 Jev 做重排。",
 "reticlehq/reticle":"给 Web / 桌面应用加「机器原生运行时感知」，让 Agent 理解它构建的东西到底跑成什么样。",
 "gargpratyush/jev-router":"在 Claude Code 里把任务路由到最便宜的模型：Jev 判难度、选档位省钱。",
 "kerpopule/hermes-jev-skills":"给 Hermes Agent（也支持 Claude Code / Codex）的 Jev 技能集：路由、记忆、压缩、技能选择、电脑与浏览器操作。",
 "wuyoscar/jev-skill":"Jev 用例、workflow 与 Agent 技能的合集，想找「Jev 能干什么」直接翻。",
 "superagents-lab/jev-search":"用 Jev 做网页搜索：源选择、查询理解与相关性排序，基于 Search1API。",
 "realZachi/pg-jev":"Postgres 扩展：用自然语言问表，Jev 把问题转成 SQL / 意图判断。",
 "kyotofin/tax-doc-classifier":"税务文档页分类器：基于 Jev 决策，261 张 IRS 表单上严格准确率 100%，每页约 $0.001。",
 "jev-chat/jev-chat-jarvis":"装在手机上的「对话副驾」：在微信 / QQ / X / 飞书里读懂对方，给候选回复、一键填入，发不发由你。",
 "samuelfaj/distill":"让 Agent「用更少的 token 干更多的活」，把长上下文里的判断与摘要用 Jev 式决策压缩。",
 "sutro-sh/jev-align":"用人类反馈 + Jev + GEPA 校准「AI Functions」，把你想要的决策行为对齐出来。",
 "OpenByteInc/QuantDinger":"开源 AI 交易操作系统。把 Jev 接进策略研究、回测与下单，覆盖加密货币 / 股票 / 外汇，自带多租户 SaaS 骨架。",
 "rmalde/minecraft-agent":"Minecraft 智能体：Astra 规划器 + JEV 控制器，带原生录制、已测路线与运行校验。",
 "wy-coliney/jev-browser-use":"比普通 browser-use 快 5–10 倍：Jev 点、Codex 想并校验，在 EZCollegeApp 实战打磨。",
 "droidrun/mobile-jev":"移动端 Agent：把 Jev 的判断层搬进 Android / iOS 自动化，决定下一步点哪。",
 "milind-soni/tiptour-macos":"开源的本地电脑操控，macOS 上快速、本地化的 computer use，Jev 判断下一步操作。",
})
HOW = {
 "browser-use/jev-ultrafast":"pip 安装后当普通 browser-use Agent 用，Jev 自动接管元素决策；把「开网页→点按钮→取结果」的流程自动化。",
 "tamaratran/fast-jev-compaction":"作为 Claude Code 插件接入，长会话自动瘦身，无需改现有 workflow。",
 "vercel-labs/json-render":"前端引入 json-render，让模型输出组件选择而非原始 JSON，UI 由框架组装。",
 "itsmostafa/typesafe-mcp":"git clone 后按 README 接 MCP，把 Jev 挂到任意支持 MCP 的客户端。",
 "jkudish/jev-mcp":"直接跑，把事实核验/分类等判断能力暴露成 MCP 工具给 Agent 调用。",
 "sharziki/semdecide":"命令行 `semdecide < 数据` 做分类打分，串进 shell 管道 / CI。",
 "0xNatoshi/jev-codex-router":"夹在 Codex 前，自动按难度选模型档位，省 token。",
 "GhalebDweikat/Winnow":"Claude Code 上下文前置过滤器，工具结果先过 Jev 再入上下文。",
 "devagrawal09/jev-review":"PR 提交后跑 Jev 预筛高风险改动，本地看板看结果再人工/大模型复审。",
 "ellipsis-dev/blink":"代码库检索用 Blink 替代全局 grep，Jev 逐层聚焦相关文件。",
 "lahfir/agent-desktop":"Rust 二进制运行，读无障碍树操控任意桌面 App，比像素猜测稳。",
 "fhshaik/typesafe-mario":"跑模拟器 + 本仓库脚本，Jev 读 RAM 状态输出动作，纯演示。",
 "RomanSlack/jev-drone":"MuJoCo 仿真里 2.5Hz 调用 Jev 做上层决策，飞控保底。",
 "emrickgarrett/OneVOneJev":"浏览器打开即玩，Three.js + Jev 实时决策，偏 demo。",
 "jarrodwatts/jev-trader":"连 Monad 测试网 Kuru 市场，每区块一次 Jev 决策，仅测试网。",
 "irfndi/prism-liquidity-agent":"DLMM 流动性做市 Agent，Jev 只判状态不直下无关单。",
 "jexp/neo4jev":"接 Neo4j，Jev 对邻居关系分类决定下一步走向，图谱遍历 demo。",
 "AkashPriyadarshii/jev-curate":"Rust 流式处理 Parquet/JSONL，Jev 做质量/风险判断后筛选训练集。",
 "qkal/Canny":"Claude Code / Codex hook，拦截「完成」声明，无证据则否决。",
 "monteduro/killmyidea":"填创业点子，Jev 多维打分给 KILL/FIX/SHIP。",
 "kushals256/jevcache":"npx 起 OpenAI 兼容代理，Jev 判意图命中则复用响应，降成本。",
}
HOW.update({
 "jaredpalmer/kev":"按 README 下载权重本地起推理服务，把 typed decision 接口接进自己的 Agent。",
 "TianyuCodings/NanoJev":"clone 后跑示例，看 parallel decision 与 dynamic candidates 怎么实现。",
 "wfzyx/von":"本地起 von 服务，把原本调 Jev 的地方切到 von，对比延迟/成本。",
 "razorback16/openjev":"本地起 openjev 服务，作为 Jev 的开源后端。",
 "ekzhang/openjev-sglang":"部署 openjev-sglang，把 Jev 调用切到本地开源后端。",
 "Rizzo-AI-Academy/rizzo-flow":"本地起 rizzo-flow，体验「零生成 token」的判断层。",
 "featherless-ai/simple-jev":"部署 simple-jev 服务，把你的开源模型包成 Jev 兼容接口。",
 "dealerdefi/Jevmind":"pip 装，jevmind demo 跑九种技能看仪表盘；接 Claude Code hook / MCP。",
 "HarnessRouter/SystemOneHarness":"git clone，s1 run 跑内置环境（如订单履约），Jev 当底层模型。",
 "thruwire/foreman":"接入你的代码生成流水线，Jev 判断每步该做什么、合不合格。",
 "pulseaiclub/phi":"作为 coding agent 框架运行，Jev 做工具选择与代码改动判定。",
 "notque/vexjoy-agent":"接入多 Agent 系统，Jev 做路由 + 质量门；/do 指令触发。",
 "dabit3/jev-experiments":"挑感兴趣的子目录看 demo，学怎么把 Jev 塞进不同产品形态。",
 "Asymptote-Labs/agent-beacon":"作为中间件挂到 Agent 循环里，Jev 负责记忆的相关性/重要性判断。",
 "kitfunso/hippo-memory":"SQLite 起库，Agent 写入记忆，检索时可用 Jev reranker 排序。",
 "reticlehq/reticle":"接入应用运行时，Jev 风格判断定位异常/状态，配合 browser-use 类 Agent。",
 "gargpratyush/jev-router":"作为 Claude Code 路由层，Jev 给每轮任务定难度再选模型。",
 "kerpopule/hermes-jev-skills":"作为 skill 包装进 Hermes / Claude Code，Jev 在多处做判断。",
 "wuyoscar/jev-skill":"当参考库翻，挑可复用的 skill / workflow 抄到自己的 Agent。",
 "superagents-lab/jev-search":"接搜索 API，Jev 负责「搜什么 / 怎么排序」，大模型只管写答案。",
 "realZachi/pg-jev":"装扩展，自然语言提问，Jev 负责意图与字段判断再生成查询。",
 "kyotofin/tax-doc-classifier":"接你的文档流，Jev 判断每页属于哪类税表，再做后续抽取。",
 "jev-chat/jev-chat-jarvis":"按 README 接 IM 机器人，屏幕只读、不 hook 不改包；Jev 出候选人确认后发送。",
 "samuelfaj/distill":"作为 Agent 的前置/旁路段，压缩冗余、保留关键判断。",
 "sutro-sh/jev-align":"接反馈数据，Jev 做校准判断，GEPA 优化提示/策略。",
 "OpenByteInc/QuantDinger":"git clone 跑内置示例策略，Jev 负责意图分类与风控判断，再触发回测/下单；本地 paper trade 起步。",
 "rmalde/minecraft-agent":"跑 Minecraft + 本仓库，Jev 在分支点做决策，路线预先录制校验。",
 "wy-coliney/jev-browser-use":"作为 browser agent 接入，Jev 负责点击决策、Codex 负责文本与校验。",
 "droidrun/mobile-jev":"接移动自动化框架，Jev 选动作；UI 结构来自无障碍树。",
 "milind-soni/tiptour-macos":"macOS 本地运行，给目标 App 发指令，Jev 选动作。",
})
NOTE = {
 "vercel-labs/json-render":"和「让模型直接写 UI」的路线相反，json-render 把生成权留在框架侧，Jev 只做结构化选择， hallucination 面更小。",
 "browser-use/jev-ultrafast":"7 秒搜一次航班的成绩来自官方 benchmark，真实网页的 anti-bot / 登录环节仍是变量，生产前先小流量验证。",
 "tamaratran/fast-jev-compaction":"压缩是不可逆的——先在小项目试，确认 Jev 的判断边界符合预期再上大仓库。",
 "jarrodwatts/jev-trader":"仅 Monad 测试网、非实盘；高频做市对延迟与滑点极敏感，81ms 是模型侧，不含链上确认。",
 "lahfir/agent-desktop":"依赖系统无障碍树，对未正确暴露 a11y 的 App 兼容有限；macOS 体验最佳。",
 "devagrawal09/jev-review":"Jev 只做「先筛」，最终背书的仍应是人工或更贵的大模型，别把它当终审。",
}
NOTE.update({
 "OpenByteInc/QuantDinger":"12k★ 是生态里体量最大的交易向项目；实盘涉及资金风险，先用回测和 paper trade 验证 Jev 的判断边界。",
 "jaredpalmer/kev":"独立复刻、非官方；用来对照 Jev 能力边界与成本，别当成官方替代品。",
 "wfzyx/von":"独立开源实现，能力边界与 Jev 不同，关键场景先对照评测。",
 "dealerdefi/Jevmind":"本地大脑默认离线免费，复杂问题再切 Jev；账本与校准是亮点，先跑 demo 体会。",
 "HarnessRouter/SystemOneHarness":"框架级，先跑官方示例理解循环，再接自己的环境。",
 "realZachi/pg-jev":"生成的 SQL 必须人工/测试校验，别直连生产库跑写操作。",
 "kyotofin/tax-doc-classifier":"已公布准确率数字，但换国家/税种需重测；严格准确率依赖表单格式稳定。",
 "featherless-ai/simple-jev":"兼容层，判断质量取决于底层模型，用来快速验证 idea。",
 "razorback16/openjev":"兼容层，能力以 DiffusionGemma 为上限，对照 Jev 评测后再上关键路径。",
 "gargpratyush/jev-router":"省钱 vs 质量需权衡，关键任务别全压到最便宜档。",
 "milind-soni/tiptour-macos":"仅 macOS；依赖无障碍树，未正确暴露 a11y 的 App 兼容有限。",
 "jev-chat/jev-chat-jarvis":"非侵入式、只读屏幕；回复质量取决于底层大模型，Jev 只做风格/意图判断。",
 "samuelfaj/distill":"压缩不可逆，先在低风险任务验证保留率。",
})
FEATURED = ["vercel-labs/json-render","browser-use/jev-ultrafast","tamaratran/fast-jev-compaction",
            "jarrodwatts/jev-trader","lahfir/agent-desktop","devagrawal09/jev-review"]

META = ["yibie/awesome-jev","Anil-matcha/awesome-jev-by-typesafe","v-modal/awesome-jev-tools",
        "AbdelStark/awesome-typesafe-jev","logicrw/awesome-jev-projects","cobanov/awesome-jev",
        "heyjunpenn/awesome-jev","AnotiaWang/awesome-jev","kraayenjon/awesome-jev","robokrunch/awesome-jev"]
META_CN = {
 "yibie/awesome-jev":"社区维护的 Jev 公开项目 / 集成 / 讨论总清单，按 Infra·SDK·集成分类，含大量客户端与框架链接。",
 "Anil-matcha/awesome-jev-by-typesafe":"有证据支撑的用例、模式、提示词与起步代码，偏「怎么把 Jev 用对」。",
 "v-modal/awesome-jev-tools":"为 Jev 打造的精选工具清单，导航向。",
 "AbdelStark/awesome-typesafe-jev":"源码支撑的 Jev 田野指南：SDK、在线 demo、Agent 工具与独立评测。",
 "logicrw/awesome-jev-projects":"源码支撑的生态雷达，自动 GitHub 同步，发现新项目用。",
 "cobanov/awesome-jev":"社区目录式清单，已收录 155+ 源审项目，按场景分组。",
 "heyjunpenn/awesome-jev":"社区维护的 Jev / System One 应用、库、资源目录。",
 "AnotiaWang/awesome-jev":"精选的 Jev / TypeSafe System One 应用、库与资源。",
 "kraayenjon/awesome-jev":"Jev 用例、项目、SDK 与资源清单（含 madewithjev 上的游戏 demo）。",
 "robokrunch/awesome-jev":"由 RoboKrunch 维护，含真实延迟/账单实测标注。",
}

def get(full):  # 返回数据集中的 dict
    if full in DATA: return DATA[full]
    return D2[full]

# ---- 截图查找（两目录都看）----
def shot(full):
    owner, repo = full.split("/")
    for d_ in ("jev-shots", "jev-shots2"):
        p = os.path.join(BASE, d_, f"{owner}__{repo}.png")
        if os.path.exists(p):
            return os.path.relpath(p, BASE)
    return None

# ---- 统计 ----
all_apps = [f for fs in CAT.values() for f in fs]
n_apps = len(all_apps)
old_stars = sum(get(f).get("stargazers_count",0) for f in all_apps)
meta_stars = sum(D2[f].get("stargazers_count",0) for f in META)
total_stars = old_stars + meta_stars
n_meta = len(META)
n_cat = len(CAT)
print(f"apps={n_apps} cats={n_cat} meta={n_meta} total_stars={total_stars:,}")

# ============ 组装 ============
CSS = """<style>
:root{--bg:#0b0d12;--panel:#14171f;--card:#27272A;--line:#3F3F46;--line2:#2a2f3a;
--text:#e6e9ef;--mut:#9aa3b2;--mut2:#71717A;--wht:#fff;--org:#F97316;--acc:#5E6AD2;}
*{box-sizing:border-box;}
body{margin:0;background:var(--bg);color:var(--text);font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,"PingFang SC","Microsoft YaHei",sans-serif;line-height:1.7;font-size:15px;}
.wrap{max-width:1080px;margin:0 auto;padding:0 22px 90px;}
a{color:#7aa6ff;text-decoration:none;}a:hover{text-decoration:underline;}
.hero{padding:54px 22px 40px;background:radial-gradient(1200px 380px at 70% -10%,rgba(249,115,22,.20),transparent 60%),linear-gradient(180deg,#15110c,#0b0d12);border-bottom:1px solid var(--line2);}
.hero .in{max-width:1080px;margin:0 auto;}
.kicker{color:var(--org);font-size:12px;letter-spacing:3px;font-weight:700;}
h1{font-size:33px;line-height:1.25;margin:10px 0 12px;font-weight:800;letter-spacing:.3px;}
.lede{color:var(--mut);font-size:15.5px;max-width:760px;}
.src{margin-top:16px;font-size:12.5px;color:var(--mut2);}
.src b{color:var(--mut);}
.statrow{display:grid;grid-template-columns:repeat(4,1fr);gap:12px;margin:26px 0 6px;}
.stat{background:var(--panel);border:1px solid var(--line2);border-radius:10px;padding:14px 16px;}
.stat .n{font-size:23px;font-weight:800;color:var(--org);}
.stat .l{font-size:12px;color:var(--mut);margin-top:2px;}
section{margin:42px 0;}
h2{font-size:21px;margin:0 0 6px;padding-left:12px;border-left:3px solid var(--org);}
.sub{color:var(--mut);font-size:13.5px;margin:0 0 18px;}
.concept{display:grid;grid-template-columns:1fr 1fr;gap:14px;margin-top:8px;}
.cc{background:var(--panel);border:1px solid var(--line2);border-radius:12px;padding:18px 20px;}
.cc h3{margin:0 0 8px;font-size:15px;color:var(--wht);}
.cc p{margin:0;color:var(--mut);font-size:13.5px;}
.cc .tag{display:inline-block;color:var(--org);font-size:11px;font-weight:700;letter-spacing:1px;margin-bottom:6px;}
.quick{background:linear-gradient(180deg,#1a160f,#14171f);border:1px solid var(--line);border-radius:12px;padding:18px 22px;margin-top:16px;}
.quick ol{margin:8px 0 0;padding-left:20px;color:var(--mut);font-size:14px;}
.quick li{margin:5px 0;}
.grid{display:grid;grid-template-columns:repeat(2,1fr);gap:16px;margin-top:10px;}
.ncard{background:var(--card);border-radius:8px;padding:18px 20px 20px;border:1px solid #303036;display:flex;flex-direction:column;}
.ncard .eyebrow{display:flex;align-items:center;gap:8px;margin-bottom:10px;}
.dot{width:6px;height:6px;border-radius:2px;background:var(--org);flex-shrink:0;}
.eyebrow .lab{color:var(--mut2);font-size:10px;letter-spacing:2px;font-weight:600;}
.eyebrow .lab.new{color:var(--org);}
.eyebrow .cat{margin-left:auto;color:var(--mut);font-size:10.5px;border:1px solid var(--line);border-radius:999px;padding:2px 9px;}
.ncard h3{margin:0;font-size:19px;font-weight:800;color:var(--wht);display:inline-block;border-bottom:3px solid var(--org);padding-bottom:2px;}
.ncard .desc{color:#D4D4D8;font-size:13px;margin:10px 0 0;flex:1;}
.ncard .stats{color:#FAFAFA;font-size:12.5px;font-weight:700;margin:12px 0 0;}
.ncard .stats span{color:var(--mut2);font-weight:400;}
.ncard .chips{display:flex;flex-wrap:wrap;gap:6px;margin-top:10px;}
.chip{background:var(--line);border:1px solid #52525B;color:#E4E4E7;font-size:10px;font-weight:600;padding:3px 8px;border-radius:3px;}
.ncard .act{margin-top:12px;font-size:12.5px;color:var(--mut);border-top:1px solid var(--line);padding-top:10px;}
.ncard .act b{color:var(--org);}
.ncard .go{margin-top:10px;font-size:12.5px;font-weight:700;}
.ncard .go a{color:var(--org);}
.shots{display:grid;grid-template-columns:repeat(3,1fr);gap:14px;margin-top:12px;}
.shot{background:var(--panel);border:1px solid var(--line2);border-radius:10px;overflow:hidden;text-decoration:none;display:block;}
.shot img{width:100%;display:block;background:#0d1016;aspect-ratio:1100/760;object-fit:cover;object-position:top;}
.shot .cap{padding:9px 11px;color:var(--text);font-size:12px;font-weight:600;display:flex;justify-content:space-between;align-items:center;gap:8px;}
.shot .cap .s{color:var(--org);font-weight:700;font-size:11.5px;}
.shot.ph{display:flex;flex-direction:column;aspect-ratio:1100/760;align-items:center;justify-content:center;color:var(--mut2);font-size:12px;text-align:center;padding:10px;}
.feat{margin-bottom:22px;}
.cols2{display:grid;grid-template-columns:1fr 1fr;gap:18px;}
@media(max-width:820px){.grid,.concept,.cols2,.statrow{grid-template-columns:1fr;}.shots{grid-template-columns:repeat(2,1fr);}}
@media(max-width:520px){.shots{grid-template-columns:1fr;}}
.note{font-size:12px;color:var(--mut2);border-top:1px dashed var(--line2);margin-top:40px;padding-top:16px;}
.hl{color:var(--org);font-weight:700;}
</style>"""

parts = []
parts.append(f"""<!DOCTYPE html>
<html lang="zh-CN"><head><meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Jev 生态全景 · {n_apps} 个把「判断」交给小模型的项目</title>
{CSS}
</head><body>
<div class="hero"><div class="in">
<div class="kicker">AI经纬线 · 工具收藏篇</div>
<h1>Jev 爆火：{n_apps} 个把「判断」交给小模型的项目，一篇收藏齐了</h1>
<p class="lede">Jev 是 TypeSafe AI 的「System One」模型，主打 <b>fast / cheap / typed judgments</b>——它几乎从不直接生成内容，只负责「判断与路由」。这篇把社区里 {n_apps} 个基于它的实战项目（含首批 21 个 + 生态扩张 30 个）按用途整理成可检索的干货档案，配官方截图，建议收藏。</p>
<div class="src">整理自 X 推文 · <b>@Pluvio9yte（雪踏乌云）</b> · 2026-09-21 首发 · 数据于 2026-09-22 经 GitHub API 实测刷新</div>
<div class="statrow">
<div class="stat"><div class="n">{n_apps}</div><div class="l">真实在跑的应用项目</div></div>
<div class="stat"><div class="n">{total_stars:,}★</div><div class="l">{n_apps} 应用 + {n_meta} 清单 累计 Star</div></div>
<div class="stat"><div class="n">{n_cat}</div><div class="l">覆盖方向（统一分类）</div></div>
<div class="stat"><div class="n">81ms</div><div class="l">jev-trader 单步决策延迟</div></div>
</div>
</div></div>
""")

# 概念
parts.append(f"""
<section>
<h2>一、先搞懂：Jev 到底是什么</h2>
<p class="sub">一句话——它是「判断层」原语，不是「生成层」模型。理解了这一点，下面 {n_apps} 个项目就全串起来了。</p>
<div class="concept">
<div class="cc"><span class="tag">本质</span><h3>TypeSafe 的 System One 模型</h3><p>官方 slogan 是 <b>"i. am. speed."</b>。核心 API 原语只有三个：<b>Choice</b>（选）、<b>Score</b>（打分）、<b>Noul</b>（无意义/跳过）。输出带类型、可工程化，不像大模型那样吐自由文本。</p></div>
<div class="cc"><span class="tag">架构角色</span><h3>廉价低延迟的「判断路由层」</h3><p>大模型负责「生成」，Jev 负责「判断与路由」。代价从「每次都调贵模型」降为「只在必要时调」。它观察状态→下判断→把执行交给大模型或底层系统。</p></div>
<div class="cc"><span class="tag">为什么爆</span><h3>便宜 + 够快 + 好接</h3><p>① 便宜到可以每步都调；② 延迟低到能做<b>实时决策</b>（游戏/交易/无人机）；③ 带类型输出，工程好接；④ Agent 长上下文的「瘦身刚需」让它迅速成为标配。</p></div>
<div class="cc"><span class="tag">怎么上手</span><h3>三步进生态</h3><div class="quick" style="margin-top:0;padding:0;background:none;border:none;"><ol>
<li>去 <b>typesafe.ai</b> 拿 Jev API Key；</li>
<li>用 <b>typesafe-mcp</b> 或 <b>jev-mcp</b> 接进 Claude Code / Codex / 任意 MCP 客户端；</li>
<li>从 <b>fast-jev-compaction</b> / <b>Winnow</b> 体验上下文瘦身，立刻见效。</li>
</ol></div></div>
</div>
</section>
""")

# 重点详解 6
parts.append('<section><h2>二、重点详解 · 6 张资料卡</h2><p class="sub">按 Star 数挑选的代表项目，含「怎么用」与「注意」。</p>')
for full in FEATURED:
    d = get(full); sp = shot(full)
    shot_html = f'<img src="{sp}" alt="{d["repo"]}">' if sp else f'<div class="ph">官方截图<br>{d["repo"]}<br>（待补）</div>'
    parts.append(f"""
<div class="feat"><div class="cols2">
<div class="shot" style="border-radius:12px;">{shot_html}<div class="cap"><span>{d['owner']}/{d['repo']}</span><span class="s">{stars(d['stargazers_count'])}★</span></div></div>
<div class="ncard" style="margin:0;">
<div class="eyebrow"><span class="dot"></span><span class="lab">PROJECT NOTE</span><span class="cat">{[c for c,fs in CAT.items() if full in fs][0]}</span></div>
<h3>{d['repo']}</h3>
<div class="sub2" style="color:var(--mut2);font-size:12px;margin:8px 0 0;">{d['owner']} · {d['language']} · {lic(d)}</div>
<div class="desc">{CN[full]}</div>
<div class="stats">{stars(d['stargazers_count'])} <span>Stars</span>　·　{d['forks_count']} <span>Forks</span>　·　{d['language']}</div>
<div class="act"><b>01 怎么用</b>　{HOW[full]}</div>
<div class="act" style="border-top:none;padding-top:6px;"><b>02 注意</b>　{NOTE.get(full,'')}</div>
<div class="go">→ <a href="{d['html_url']}" target="_blank" rel="noopener">github.com/{full}</a></div>
</div></div></div>
""")
parts.append("</section>")

# 统一全景网格 51
parts.append(f'<section><h2>三、全景资料卡 · {n_apps} 个项目（统一 {n_cat} 类）</h2><p class="sub">按用途合并首批 21 个与生态扩张 30 个，Star 数为 GitHub API 实测刷新（2026-09-22）。带 <span class="hl">NEW</span> 标记为 2026-09-22 新增的 30 个扩张项目。</p>')
for cat, fs in CAT.items():
    parts.append(f'<h3 style="color:var(--mut2);font-size:13px;letter-spacing:1px;margin:22px 0 4px;">{cat}（{len(fs)}）</h3>')
    parts.append('<div class="grid">')
    for full in fs:
        d = get(full)
        is_new = full in EXPANSION
        lab = '<span class="lab new">NEW · 扩展</span>' if is_new else '<span class="lab">PROJECT NOTE</span>'
        chips = " ".join(f'<span class="chip">{t}</span>' for t in (d.get("topics") or [])[:4]) or f'<span class="chip">{cat}</span>'
        note = NOTE.get(full, "")
        act2 = f'<div class="act" style="border-top:none;padding-top:6px;"><b>02 注意</b>　{note}</div>' if note else ""
        parts.append(f"""
<div class="ncard">
<div class="eyebrow"><span class="dot"></span>{lab}<span class="cat">{cat}</span></div>
<h3>{d['repo']}</h3>
<div class="desc">{CN[full]}</div>
<div class="stats">{stars(d['stargazers_count'])} <span>Stars</span>　·　{d['language']}　·　{lic(d)}</div>
<div class="chips">{chips}</div>
<div class="act"><b>上手</b>　{HOW[full]}</div>
{act2}
<div class="go">→ <a href="{d['html_url']}" target="_blank" rel="noopener">详情</a></div>
</div>""")
    parts.append('</div>')
parts.append("</section>")

# 统一画廊 51
parts.append(f'<section><h2>四、官方截图 · 仓库实拍（{n_apps} 仓）</h2><p class="sub">无头 Chrome 直截 GitHub 仓库页（含 README 顶部），按 Star 数排序。点击跳转原仓库。</p><div class="shots">')
for full in sorted(all_apps, key=lambda f: get(f).get("stargazers_count",0), reverse=True):
    d = get(full); sp = shot(full)
    if sp:
        parts.append(f'<a class="shot" href="{d["html_url"]}" target="_blank" rel="noopener"><img loading="lazy" src="{sp}" alt="{d["repo"]}"><div class="cap"><span>{d["repo"]}</span><span class="s">{stars(d["stargazers_count"])}★</span></div></a>')
    else:
        parts.append(f'<a class="shot ph" href="{d["html_url"]}" target="_blank" rel="noopener">{d["repo"]}<br>截图待补<br><span class="s">{stars(d["stargazers_count"])}★</span></a>')
parts.append('</div></section>')

# 社区清单
parts.append(f"""
<section>
<h2>五、社区精选清单 · {n_meta} 个导航站</h2>
<p class="sub">想跟进生态全貌、找客户端/SDK/框架，直接逛这几个社区清单。按 Star 排序，均为 GitHub 仓库。注意：多个作者各自维护了同名 <code>awesome-jev</code> 清单，属生态碎片化，按需取用即可。</p>
<div class="grid">
""")
for full in sorted(META, key=lambda f: D2[f].get("stargazers_count",0), reverse=True):
    d = D2[full]
    parts.append(f"""
<div class="ncard">
<div class="eyebrow"><span class="dot"></span><span class="lab">AWESOME LIST</span><span class="cat">导航</span></div>
<h3>{d['repo']}</h3>
<div class="desc">{META_CN[full]}</div>
<div class="stats">{stars(d['stargazers_count'])} <span>Stars</span>　·　{d['language']}</div>
<div class="go">→ <a href="{d['html_url']}" target="_blank" rel="noopener">github.com/{full}</a></div>
</div>""")
parts.append('</div></section>')

parts.append(f"""
<p class="note">说明：本文档由 X 推文 <b>@Pluvio9yte/status/2101831273224311035</b> 整理扩展而成。{n_apps} 个应用仓库 + {n_meta} 个社区清单均经 GitHub API 实测存在（2026-09-22 刷新），Star / 语言 / 协议为实时数据；中文功能描述来自原帖与社区清单上下文，未做改写。Jev 即 TypeSafe AI 的 System One 模型（官方 slogan "i. am. speed."），相关能力以官方 docs 为准。截图因渲染限流个别缺失不影响档案完整性。如需转成公众号图文或腾讯文档，可在此基础上二次编排。</p>
</body></html>""")

html = "\n".join(parts)
with open(os.path.join(BASE, "jev-collection.html"), "w", encoding="utf-8") as f:
    f.write(html)
print("written jev-collection.html", len(html), "bytes")

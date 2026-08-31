#!/usr/bin/env python3
"""Build the multilingual GitBook-ready documentation tree."""

from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"

LANGS = [
    ("en", "English", "Good Tomorrow Documentation"),
    ("zh", "简体中文", "Good Tomorrow 文档"),
    ("ko", "한국어", "Good Tomorrow 문서"),
    ("ja", "日本語", "Good Tomorrow ドキュメント"),
]

PAGES = [
    ("README.md", "home", {"en": "Good Tomorrow", "zh": "Good Tomorrow", "ko": "Good Tomorrow", "ja": "Good Tomorrow"}),
    ("overview/introduction.md", "overview", {"en": "Overview", "zh": "概览", "ko": "개요", "ja": "概要"}),
    ("protocol/architecture.md", "architecture", {"en": "Protocol Architecture", "zh": "协议架构", "ko": "프로토콜 아키텍처", "ja": "プロトコルアーキテクチャ"}),
    ("protocol/liquidity-infrastructure.md", "liquidity", {"en": "Liquidity Infrastructure", "zh": "流动性基础设施", "ko": "유동성 인프라", "ja": "流動性インフラ"}),
    ("protocol/capital-management.md", "capital", {"en": "Capital Management", "zh": "资本管理", "ko": "자본 관리", "ja": "資本管理"}),
    ("protocol/yield-profit-distribution.md", "yield", {"en": "Yield and Profit Distribution", "zh": "收益与利润分配", "ko": "수익과 이익 분배", "ja": "収益と利益分配"}),
    ("networks/stablecoin-payments-rwa.md", "networks", {"en": "Stablecoins, Payments, and RWA", "zh": "稳定币、支付与 RWA", "ko": "스테이블코인, 결제, RWA", "ja": "ステーブルコイン、決済、RWA"}),
    ("risk/transparency-and-solvency.md", "risk", {"en": "Risk, Solvency, and Transparency", "zh": "风险、偿付能力与透明度", "ko": "리스크, 지급능력, 투명성", "ja": "リスク、支払能力、透明性"}),
    ("governance/token-and-governance.md", "token", {"en": "Token and Governance", "zh": "代币与治理", "ko": "토큰과 거버넌스", "ja": "トークンとガバナンス"}),
    ("roadmap/development-roadmap.md", "roadmap", {"en": "Development Roadmap", "zh": "发展路线图", "ko": "개발 로드맵", "ja": "開発ロードマップ"}),
    ("roadmap/long-term-vision.md", "vision", {"en": "Long-Term Vision", "zh": "长期愿景", "ko": "장기 비전", "ja": "長期ビジョン"}),
    ("reference/references.md", "references", {"en": "References", "zh": "参考文献", "ko": "참고 문헌", "ja": "参考文献"}),
    ("project/glossary.md", "glossary", {"en": "Glossary", "zh": "术语表", "ko": "용어집", "ja": "用語集"}),
    ("project/content-map.md", "content_map", {"en": "Content Map", "zh": "内容映射", "ko": "콘텐츠 맵", "ja": "コンテンツマップ"}),
    ("project/translation-guide.md", "translation_guide", {"en": "Translation Guide", "zh": "翻译指南", "ko": "번역 가이드", "ja": "翻訳ガイド"}),
    ("project/qa-report.md", "qa_report", {"en": "QA Report", "zh": "QA 报告", "ko": "QA 보고서", "ja": "QAレポート"}),
]

CONTENT = {
    "en": {
        "home": """# Good Tomorrow

Good Tomorrow is an onchain liquidity finance infrastructure protocol built on BNB Smart Chain for stablecoins, real-world assets (RWA), and payment ecosystems.

The protocol is designed around a unified capital management framework. User assets that satisfy protocol requirements enter a shared liquidity and asset-liability management system, then may be allocated according to liquidity demand, market rates, risk parameters, and strategy capacity.

Good Tomorrow does not position fixed APY or token emissions as the long-term source of user returns. Its financial model is based on realized financial income. After realized losses, risk reserves, liquidity reserves, and necessary operating costs are deducted, the remaining distributable net profit may be allocated according to protocol rules.

As stablecoin markets, payment networks, regional stablecoins, and RWA modules are connected over time, Good Tomorrow is intended to evolve from a base liquidity protocol into an Onchain Financial Network.

## Language Versions

The documentation is organized in this order:

1. English
2. 简体中文
3. 한국어
4. 日本語

## Documentation Structure

- **Overview** introduces the market background, problem statement, and protocol thesis.
- **Protocol Architecture** explains the liquidity, risk, capital allocation, yield settlement, and profit distribution modules.
- **Capital and Yield** describes how strategy capacity, realized income, and profit allocation work.
- **Financial Networks** covers stablecoin liquidity, payment and settlement liquidity, and RWA capital allocation.
- **Risk and Governance** covers solvency, transparency, token supply, and governance.
- **Roadmap and Vision** explains the phased development path toward onchain financial infrastructure.
""",
        "overview": """# Overview

## Abstract

Decentralized finance has developed a broad set of primitives, including decentralized exchange, lending, stablecoins, asset management, and real-world asset tokenization. Yet the current onchain financial system remains highly fragmented. Stablecoin liquidity is spread across protocols and applications, while DeFi, payments, asset management, and yield products lack a unified mechanism for coordinating capital.

Yield generation in DeFi is also uneven. Some yield comes from real financial activity such as DeFi interest, trading fees, or asset investment income. Other yield comes from protocol token incentives or subsidy mechanisms. Without a unified capital management system, users often struggle to understand how assets are used, how efficiently capital is deployed, and where returns actually originate.

Good Tomorrow addresses this by creating a liquidity-based financial infrastructure protocol on BNB Smart Chain. Its objective is not to maximize nominal yield at any cost, but to coordinate capital across stablecoin liquidity, yield strategies, payments and settlement, and future RWA activities that meet the protocol's admission standards.

## Background

DeFi made it possible for asset trading and liquidity provision to operate through public smart contracts. Decentralized exchanges provide trading and price discovery; lending protocols create capital markets between asset holders and borrowers; stablecoins serve as the base medium for onchain trading and settlement; and RWA tokenization expands the possible allocation scope of onchain capital.

Even though each protocol category solves an important problem, onchain capital still mostly exists in isolated systems. Users can deposit stablecoins into lending markets, provide liquidity, or participate in yield strategies, but the capital management logic behind each venue is typically independent.

As stablecoin supply continues to grow, simply adding more financial products is not enough to solve capital efficiency. The next stage of DeFi is expected to shift from single financial products toward financial infrastructure with stronger liquidity coordination.

## Problem Statement

### Fragmented liquidity

Stablecoins and other onchain assets are distributed across chains, trading markets, protocols, and payment systems. Each protocol usually maintains its own liquidity pool and capital management model. Capital cannot be scheduled across different financial needs, which leaves some assets underutilized while other markets may face liquidity shortages.

Good Tomorrow is designed to create a unified liquidity management framework that lets different financial modules share an underlying capital base under risk controls.

### Opaque sources of yield

APY is an important market signal, but APY alone does not explain where returns come from. User returns may originate from DeFi interest, trading fees, market strategies, token incentives, or other subsidies. If a protocol cannot distinguish between those income sources, users cannot judge whether the yield is sustainable.

Good Tomorrow uses a yield calculation model based on actual financial income and aims to progressively make capital utilization, income sources, and risk reserves transparent onchain.

### Capital scale and strategy capacity mismatch

Capital scale does not automatically improve efficiency. Many financial strategies have capacity limits. A strategy that works well for a small pool may suffer lower returns, higher market impact, or liquidity shortages once capital grows quickly.

Good Tomorrow therefore does not use a static allocation model. Capital allocation can adjust dynamically according to system size, market rates, liquidity demand, and strategy capacity.
""",
        "architecture": """# Protocol Architecture

Good Tomorrow is a liquidity-based onchain financial infrastructure protocol. Its operating flow consists of asset deposits, liquidity management, capital allocation, financial activities, yield settlement, and profit distribution.

![Original Chinese capital flow diagram](../../.gitbook/assets/image1.png)

## Operating Flow

| Stage | Function |
| --- | --- |
| Asset deposit | Eligible user assets enter the protocol. |
| Liquidity management | The system maintains reserves for redemption, settlement, and normal operations. |
| Capital allocation | Available capital is routed by market demand, utilization, risk parameters, and strategy capacity. |
| Financial activities | Capital may support trading, stablecoin liquidity, payments, yield strategies, and qualified future RWA activities. |
| Yield settlement | Realized income is recognized and aggregated. |
| Profit distribution | Distributable profit is allocated after losses, reserves, and costs. |

## Five Core Modules

![Original Chinese system architecture diagram](../../.gitbook/assets/image2.png)

Good Tomorrow's architecture consists of five mutually dependent modules:

| Module | Role |
| --- | --- |
| Liquidity layer | Handles deposits, redemptions, liquidity reserves, and basic capital scheduling. |
| Risk layer | Continuously evaluates protocol assets and external financial activities. |
| Capital allocation layer | Allocates available capital to markets and financial scenarios under protocol rules. |
| Yield settlement layer | Accounts for realized income from different financial activities. |
| Profit distribution layer | Processes and distributes net profit after risk and cost deductions. |

These modules form a shared financial operating framework. User assets first enter the liquidity system, then move into capital allocation only when protocol risk requirements and market conditions permit. Income from different activities is collected into a unified settlement system before final distribution.

Good Tomorrow is not designed to concentrate all capital into a single high-yield strategy. It creates a multilayer capital allocation system where funds with different liquidity needs, risk levels, and use periods can be routed to different financial activities while maintaining a balance among asset safety, liquidity, and capital efficiency.
""",
        "liquidity": """# Liquidity Infrastructure

Good Tomorrow starts from a simple thesis: onchain finance does not lack assets or products; it lacks liquidity infrastructure that can coordinate different financial needs.

Stablecoins, DeFi markets, decentralized exchanges, yield protocols, and RWA products have each developed separately. In most cases, every protocol maintains its own liquidity pool, risk model, and capital usage rules. Capital circulates inside a specific application rather than through a unified capital management system.

## Liquidity as a Managed Resource

Good Tomorrow defines liquidity as a financial resource that can be managed and scheduled, not as a static asset inside a single pool. When a user deposits assets into the protocol, those assets enter a unified asset-liability management framework. The protocol does not pre-commit all funds to one DeFi market or require assets to remain in one yield strategy.

Final capital use depends on the system's current liquidity needs, market rates, risk conditions, strategy capacity, and overall asset scale.

## Capital Layer for Multiple Scenarios

The protocol is intended to become an underlying capital layer for several financial scenarios:

- Stablecoin liquidity
- Payment and settlement
- Yield-oriented products
- Future RWA activities that meet protocol standards

Applications do not need to share the same product logic, but they can obtain capital support through a unified liquidity and risk management framework.

## Liquidity Is Not 100% Utilization

Good Tomorrow does not treat maximum fund utilization as the only goal. For a long-running financial system, 100% utilization may reduce resilience. If all capital is deployed into markets without immediate exit capacity, the protocol may be unable to respond effectively to user redemptions or liquidity shocks.

The target is a dynamic balance among capital utilization, asset liquidity, and risk control. This design allows Good Tomorrow to evolve from a single DeFi product into shared financial infrastructure as more assets and applications connect to the liquidity layer.
""",
        "capital": """# Capital Management

Traditional yield protocols often allocate deposits to a limited number of yield sources according to preset rules. That can work when capital is small, but strategy capacity becomes a constraint as assets under management grow. A strategy that can absorb USD 1 million efficiently cannot necessarily absorb USD 100 million with the same risk and return profile.

Good Tomorrow's capital management model is built on the principle that strategy capacity is limited.

## Allocation Criteria

The protocol does not use the highest displayed APY as the sole allocation signal. Capital allocation must evaluate:

- Expected return
- Market and credit risk
- Asset liquidity
- Exit capacity
- Market depth
- Strategy capacity
- System-wide liquidity demand
- Risk budget

Nominal yields may decline as capital enters a market, and high-yield markets may carry higher credit risk, market risk, or exit risk. Allocation decisions therefore use risk-adjusted realized return as the foundation.

## Dynamic Capacity

Strategy capacity is not permanently fixed. Maximum permitted allocation may change when market depth, asset prices, DeFi demand, or liquidity conditions change. Through preset parameters or later governance mechanisms, the protocol may reduce the capital limit of a strategy or stop new capital from entering when risk conditions require it.

## Scale Effects

As TVL grows, the allocation structure may shift. At a smaller asset scale, Good Tomorrow may access higher-efficiency markets with limited capacity. As the asset base expands, the protocol may increase allocations to larger DeFi markets, high-liquidity stablecoin markets, short-duration financial assets, and other lower-risk assets capable of supporting more capital.

This means Good Tomorrow does not promise to maintain a fixed yield as funds grow. Yield may change with market environment, capital scale, and portfolio composition. That change is not necessarily a decline in protocol efficiency; it is the natural transition from a high-flexibility stage toward scaled asset management.
""",
        "yield": """# Yield and Profit Distribution

Good Tomorrow's yield model is based on actual income. The protocol does not set a permanent fixed APY and does not rely on continuous token emissions to maintain a marketed yield level.

## Income Sources

Future income may include:

- DeFi interest
- Stablecoin liquidity service fees
- Trading and settlement fees
- Realized gains from market strategies
- Cash flows generated by real-world assets
- Other infrastructure service income

These sources have different risk attributes and settlement cycles. Displayed market yields cannot simply be added together.

## Realized Income Principle

At the accounting level, Good Tomorrow distinguishes nominal yield, unrealized gain, and realized income. Only income that has completed settlement and can be confirmed enters the protocol's income accounting system. For example, an increase in the book value of an asset does not automatically become distributable profit. It can become a basis for distribution only after settlement and entry into the protocol asset system.

The protocol may distribute returns only when distributable net income is positive. If income declines during a period or confirmed losses occur, user returns may decrease. The protocol will not create nonexistent income to maintain a promotional yield.

## Profit Allocation

After income recognition, the protocol deducts realized losses, risk reserves, liquidity reserves, and necessary operating costs. The remaining net profit can be distributed according to protocol rules among liquidity providers, the risk reserve system, the protocol treasury, and ecosystem development.

This links user returns directly to actual financial operations rather than to a fixed interest promise.
""",
        "networks": """# Stablecoins, Payments, and RWA

Good Tomorrow is designed to connect several financial networks through one liquidity layer.

## Stablecoin Liquidity Network

Stablecoins are core to Good Tomorrow's infrastructure. Most onchain value exchange, asset settlement, and capital scheduling still depend on stablecoins. As stablecoins expand into payments, cross-border settlement, and enterprise finance, their role will extend beyond crypto trading.

The future stablecoin market may include global USD stablecoins, regulated stablecoins, regional stablecoins, and onchain settlement assets denominated in different currencies. Demand for exchange, clearing, liquidity management, and capital scheduling will continue to grow.

Good Tomorrow does not aim to issue a new stablecoin. It aims to provide underlying liquidity support for different stablecoins. Assets may be routed into trading, DeFi, payments, or other activities according to actual demand.

Different stablecoins are not treated as having identical risk. The protocol may assign risk parameters according to issuance mechanism, reserve structure, redemption capacity, market liquidity, and regulatory environment. Some assets may be suitable only for payment settlement, while others may qualify for both DeFi and capital allocation.

## Payment and Settlement Liquidity

Payments and settlement are a major path for Good Tomorrow's evolution from a DeFi protocol into an onchain financial network. Payment systems require capital to clear and deliver value on time, not just capital with high returns.

Good Tomorrow treats payment and settlement needs as independent liquidity constraints. The protocol must maintain immediately available assets for payments, asset exchange, merchant settlement, and other short-term financial needs.

When payment liquidity is temporarily idle, that capital may enter short-duration, low-risk, or highly liquid markets as long as immediate solvency is not affected. This brings a cash-management logic familiar in traditional finance into stablecoin payment markets.

## RWA and Onchain Capital Allocation

RWA tokenization creates new capital sources and income markets for onchain finance, but RWAs are fundamentally different from native DeFi assets. Their value depends on legal relationships, issuers, custody arrangements, and cash flows in the real world.

RWAs should not be treated simply as higher-yield DeFi products. Before any RWA enters Good Tomorrow's capital system, it must pass independent asset and risk assessment, including credit quality, legal rights, recourse after default, custodian arrangements, cash-flow movement onchain, and exit mechanisms.

RWAs are more suitable for the strategic capital layer than for immediate liquidity reserves. Only after basic liquidity requirements are satisfied, and only when an RWA product's term, risk, and exit mechanism meet protocol requirements, may some capital be allocated to that asset class.

Good Tomorrow will not describe RWA as risk-free yield. Credit, legal structure, custody, liquidity, and regulatory changes can all affect actual returns and principal safety, so RWA exposure must remain subject to strict risk limits.
""",
        "risk": """# Risk, Solvency, and Transparency

For any system that manages user assets, yield is only one part of operation. Long-term viability depends on maintaining solvency during market stress and asset losses.

## Risk Management Layers

Good Tomorrow's risk management operates at three levels:

| Level | Scope |
| --- | --- |
| Asset layer | Maximum deposit size, maximum allocation ratio, and minimum liquidity requirement for each asset. |
| Strategy layer | Risk budget limits for every capital allocation activity. |
| Protocol layer | Continuous monitoring of liquidity, redemption demand, capital utilization, and market volatility. |

When abnormal market conditions occur, the protocol may increase immediate liquidity, slow new capital allocation, or stop entering markets where risk has increased.

## Risk Reserves

The protocol may allocate a portion of actual income to a risk reserve. This reserve is not part of ordinary yield distribution. It is used to address strategy losses, DeFi defaults, failed liquidations, or external protocol risks.

In the short term, reserving capital may reduce immediate user yield. Over the long term, risk buffers are necessary for improving the protocol's ability to continue operating.

## Onchain Transparency and Financial Verification

Good Tomorrow's long-term goal is to build an onchain transparency system aligned with its capital structure. Users should be able to understand:

- How many assets the protocol manages
- How many assets remain liquid
- How much capital has been deployed
- Which activities generated realized income

The protocol aims to progressively establish proof of reserves, proof of capital utilization, and proof of yield.

Proof of reserves shows protocol assets and related reserves. Proof of capital utilization shows how user assets are allocated across financial modules. Proof of yield shows realized income and its main sources. Together, these mechanisms make it clearer whether assets are safely used and whether claimed income is real.

In the long run, transparency should rely less on team reports and more on onchain data, public addresses, and verifiable smart contract states.
""",
        "token": """# Token and Governance

## Native Token

Good Tomorrow is the native ecosystem token of the Good Tomorrow protocol and is planned for deployment on BNB Smart Chain. Total token supply is fixed at **10,000,000 Good Tomorrow**.

The initial token structure is deliberately simple. It does not include traditional multi-round private sales, institutional investor allocations, or complex early unlock schedules. Supply is primarily allocated to initial liquidity, long-term locked release, and ecosystem growth.

![Original Chinese token supply diagram](../../.gitbook/assets/image3.png)

| Allocation Category | Amount | Share of Total Supply |
| --- | ---: | ---: |
| Good Tomorrow/USDC initial liquidity | 9,000,000 | 90% |
| Long-term lockup and release | 900,000 | 9% |
| Market and ecosystem growth | 100,000 | 1% |
| Total | 10,000,000 | 100% |

The 9% long-term lockup allocation remains fully locked for the first 12 months after launch. After the lockup period, it releases linearly over the following 12 months. Under an equal monthly release schedule, the theoretical monthly release from month 13 through month 24 is:

$$
\\frac{900,000}{12}=75,000
$$

The remaining 100,000 tokens may support early user growth, ecosystem partnerships, community building, and other activities related to long-term protocol development.

## Protocol Governance

As Good Tomorrow manages more assets and financial modules, governance becomes an important part of capital management.

Governance is not intended to submit every parameter to short-term community voting. Instead, it should define clear boundaries between decentralized decision-making and professional risk management. General ecosystem matters, such as new partnerships, ecosystem fund use, and protocol feature upgrades, may gradually move to community governance.

Capital allocation ratios, asset risk parameters, and major financial risk events require stronger safeguards because purely short-term voting can create governance attack and market manipulation risks.

Over time, Good Tomorrow may form a governance structure composed of protocol governance, risk management mechanisms, and onchain execution. Token holders may participate in protocol direction, asset admission, and ecosystem development as the governance system matures.
""",
        "roadmap": """# Development Roadmap

Good Tomorrow's development is centered on onchain liquidity. It begins with DeFi capital management and gradually expands into stablecoins, onchain finance, payments and settlement, and RWA liquidity infrastructure.

![Original Chinese roadmap diagram](../../.gitbook/assets/image4.png)

The long-term path is:

**DeFi Liquidity -> Stablecoin Liquidity -> Multi-Asset Capital Network -> Payment and Settlement Liquidity -> RWA Liquidity -> Onchain Financial Infrastructure**

## Phase 1: Liquidity Base Layer

- Establish the base financial protocol architecture.
- Complete asset deposit and redemption mechanisms.
- Build a unified liquidity management system.
- Create foundational risk parameters and asset management framework.
- Deploy the Good Tomorrow/USDC initial liquidity market.
- Complete core smart contract testing and security audits.

Goal: establish the first liquidity infrastructure layer so user assets can enter a unified, transparent, and verifiable onchain capital management system.

## Phase 2: DeFi Capital Network

- Move from single liquidity management into onchain capital allocation.
- Connect mainstream DeFi financial markets.
- Build lending, liquidity, and yield-oriented capital allocation capability.
- Establish dynamic capital utilization models.
- Introduce strategy capacity management and risk budgets.
- Enable capital scheduling across markets.

Target cycle: **Liquidity -> Lending -> Yield -> Redistribution**.

## Phase 3: Stablecoin Liquidity Network

- Expand support for multiple stablecoin assets.
- Establish stablecoin admission and risk-rating mechanisms.
- Connect major USD stablecoin markets.
- Explore regional and regulated stablecoin liquidity demand.
- Build capital scheduling and liquidity support among stablecoins.

Supported directions may include USD stablecoins, regional stablecoins, HKD stablecoins, payment stablecoins, and regulated stablecoins.

## Phase 4: Payment and Settlement Liquidity Infrastructure

- Enter stablecoin payment and onchain settlement markets.
- Build instant liquidity management for payment scenarios.
- Support merchant settlement and capital scheduling.
- Explore cross-border payment and multi-stablecoin settlement.
- Connect payment networks with DeFi liquidity.

Target cycle: **Payment -> Settlement -> Liquidity -> Yield**.

## Phase 5: RWA Liquidity Infrastructure

- Gradually connect RWAs that meet protocol risk standards.
- Build RWA admission, risk assessment, and liquidity management frameworks.
- Explore onchain liquidity needs for treasuries, bonds, funds, notes, and other real-world yield assets.
- Connect stablecoins with real-world assets.
- Support portfolio allocation across different maturities and risk levels.

Target cycle: **Stablecoin Liquidity <-> Onchain Capital <-> Real World Assets**.

## Phase 6: Multi-Ecosystem Liquidity Network

As stablecoins, payment networks, DeFi protocols, and RWA assets connect, Good Tomorrow will develop a unified liquidity network. Financial applications can share liquidity management, capital allocation, stablecoin support, payment and settlement liquidity, RWA access, risk infrastructure, and yield settlement.

## Phase 7: Onchain Financial Infrastructure

Good Tomorrow ultimately aims to establish liquidity finance infrastructure that covers onchain and real-world financial needs. Stablecoins become the value medium, DeFi provides open markets, Good Tomorrow provides unified liquidity and capital management, payment networks provide commercial use cases, and RWA brings real-world assets onchain.
""",
        "vision": """# Long-Term Vision

Good Tomorrow's long-term goal is not to become another single-function DeFi protocol. As stablecoins, DeFi, payments, and real-world assets move further onto blockchains, the deeper question becomes how different assets and financial products can share capital, manage liquidity, and remain stable while scaling.

Good Tomorrow aims to become the capital base layer inside that system.

In the early stages, liquidity infrastructure mainly serves stablecoins and onchain financial markets. As DeFi modules are added, capital begins to generate interest based on real funding demand. As payment and settlement use cases develop, liquidity gains commercial utility. As RWAs are connected, the protocol's allocation scope can extend into broader financial markets.

These modules are not independent. DeFi creates interest demand, payments create settlement demand, stablecoins create exchange and liquidity demand, and RWA provides new allocation directions. Good Tomorrow connects these needs through unified capital and risk management.

Over time, Good Tomorrow is expected to evolve from a liquidity protocol into financial infrastructure and finally into an Onchain Financial Network.

The protocol's ultimate value is not fixed yield. Its value is the creation of a system that can manage onchain capital over the long term, identify real sources of income, and serve multiple financial markets.
""",
        "references": """# References

1. Ethereum Foundation. Introduction to Smart Contracts.
2. Ethereum Foundation. Ethereum Development Documentation.
3. Ethereum Foundation. Smart Contract Security.
4. Binance Academy. What Is DeFi 2.0 and Why Does It Matter?
5. Aave. Introduction to Aave V3.
6. Curve Finance. Curve Documentation.
7. Uniswap Labs. Uniswap Documentation.
8. Circle. USDC — Powering Global Finance.
9. Chainlink. Real-World Assets (RWAs) Explained.
10. Chainlink. Asset Tokenization: What It Is and How It Works.
11. Chainlink. What Is Tokenization?
12. Financial Stability Board (FSB). G20 Roadmap for Enhancing Cross-border Payments.
13. Financial Stability Board (FSB). Targets for Addressing the Four Challenges of Cross-border Payments.
14. BIS Committee on Payments and Market Infrastructures (CPMI). Correspondent Banking.
""",
    },
}

CONTENT["zh"] = {
    "home": """# Good Tomorrow

Good Tomorrow 是构建于 BNB Smart Chain 上的链上流动性金融基础设施协议，面向稳定币、现实世界资产（RWA）与支付生态。

协议以统一资本管理框架为核心。符合协议要求的用户资产进入统一的流动性与资产负债管理体系，并根据流动性需求、市场利率、风险参数和策略容量，被配置至稳定币流动性、收益策略、支付与清结算，以及未来符合准入标准的 RWA 等金融活动。

Good Tomorrow 的设计目标并非维持固定 APY，也不将代币激励作为长期收益的主要来源。协议采用基于实际金融收入的利润结算机制，在扣除已实现损失、风险准备、流动性储备和必要运营成本后，将剩余可分配净利润按照协议规则进行分配。

随着稳定币市场、支付网络、区域性稳定币及 RWA 模块逐步接入，Good Tomorrow 将从基础流动性协议发展为连接不同资产与金融服务的 Onchain Financial Network。
""",
    "overview": """# 概览

## 摘要

去中心化金融已经形成了去中心化交易、借贷、稳定币、资产管理和现实世界资产代币化等金融原语。然而，现有链上金融体系仍然高度碎片化。稳定币流动性分布于不同协议和应用之中，DeFi、支付、资产管理和收益产品之间缺乏统一资本协调机制，大量资产无法根据实际市场需求有效配置。

DeFi 市场中的收益机制也存在明显差异。部分收益来自真实 DeFi 利息、交易手续费和资产投资收益，部分则来自协议代币激励或补贴机制。缺乏统一资本管理体系时，用户很难判断资产用途、资金利用率以及收益的真实来源。

Good Tomorrow 通过统一资本管理框架，将用户资产根据流动性需求、市场利率、风险参数及策略容量，配置至稳定币流动性、收益策略、支付与清结算及未来符合协议标准的 RWA 活动。

## 背景

DeFi 使资产交易和流动性提供能够通过公开智能合约完成。去中心化交易协议提供交易与价格发现；借贷协议建立资本市场；稳定币成为链上交易与结算的基础媒介；RWA 代币化进一步扩展链上资本配置范围。

尽管不同金融协议解决了各自领域的问题，链上资本仍主要以孤立方式存在。用户可以将稳定币存入 DeFi 协议，也可以用于流动性提供或收益策略，但各协议的资本管理通常彼此独立。

随着稳定币规模持续增长，仅增加新金融产品已经难以解决资本效率问题。下一阶段 DeFi 的重点将从单一金融产品转向金融基础设施。

## 问题陈述

### 流动性碎片化

稳定币和其他链上资产分布在不同区块链、交易市场、协议和支付系统中。每个协议通常拥有独立流动性池和资本管理机制。资金无法在不同金融需求之间统一调度，导致部分资产长期低利用率，而部分市场又可能流动性不足。

Good Tomorrow 的目标是建立统一流动性管理框架，使不同金融模块能够在风险控制条件下共享底层资本。

### 收益来源不透明

APY 是 DeFi 市场的重要指标，但 APY 本身无法解释收益来源。用户收益可能来自 DeFi 利息、交易手续费、市场策略，也可能来自代币激励。若协议无法区分收入来源，用户无法准确判断收益的长期可持续性。

Good Tomorrow 采用基于实际金融收入的收益计算方式，并逐步建立资金利用、收入来源和风险准备的链上透明机制。

### 资金规模与策略容量不匹配

资金规模扩大并不会自动提高资本效率。许多金融策略存在容量限制。小规模资金可以进入高效率市场，但资金快速增长后，原有策略可能出现收益下降、市场冲击增加或流动性不足。

因此，Good Tomorrow 不采用静态资本配置模型，而是根据系统规模、市场利率、流动性需求和策略容量动态调整资金配置。
""",
    "architecture": """# 协议架构

Good Tomorrow 是以流动性为基础的链上金融基础设施。协议运行逻辑由资产进入、流动性管理、资本配置、金融活动、收益结算及利润分配构成。

![原始资金流程图](../../.gitbook/assets/image1.png)

## 运行流程

| 阶段 | 作用 |
| --- | --- |
| 资产存入 | 符合条件的用户资产进入协议。 |
| 流动性管理 | 维持赎回、结算和协议正常运行所需储备。 |
| 资本配置 | 根据市场需求、利用率、风险参数和策略容量调度资金。 |
| 金融活动 | 资金可进入交易、稳定币流动性、支付、收益策略和合格 RWA。 |
| 收益结算 | 对已实现收入进行确认和汇总。 |
| 利润分配 | 扣除损失、储备和成本后进行分配。 |

## 五个核心模块

![原始系统架构图](../../.gitbook/assets/image2.png)

| 模块 | 作用 |
| --- | --- |
| 流动性层 | 负责存入、赎回、流动性储备和基础资金调度。 |
| 风险层 | 持续评估协议内部资产和外部金融活动。 |
| 资本配置层 | 按协议规则将可用资金配置至不同市场和金融场景。 |
| 收益结算层 | 统一核算不同金融活动产生的实际收入。 |
| 利润分配层 | 处理收益结算后的实际净利润并进行分配。 |

五个模块并非独立运行，而是共同组成协议的基础金融运行框架。用户资产首先进入流动性体系，并在满足风险要求和市场条件后进入资本配置环节。不同金融活动产生的实际收入进入统一收益结算系统，并在完成风险准备和成本核算后最终分配。

Good Tomorrow 的目标不是将所有资金集中投入某一种高收益策略，而是在统一风险管理框架下建立多层次资本配置体系，在资金安全、流动性和资本效率之间维持合理平衡。
""",
    "liquidity": """# 流动性基础设施

Good Tomorrow 的核心判断是：链上金融市场并不缺乏资产或金融产品，真正缺乏的是能够统一协调不同金融需求的流动性基础设施。

稳定币、DeFi 市场、去中心化交易所、收益协议和 RWA 已分别形成独立发展路径，但其资本大多相互隔离。每个协议维护自己的流动性池、风险模型和资金使用规则，资本通常只能在特定应用内部循环。

## 作为金融资源的流动性

Good Tomorrow 将流动性定义为可以被统一管理和调度的金融资源，而非单一产品中的静态资产。用户资产进入协议后，首先进入统一资产负债管理框架。协议不预先承诺所有资金进入某个 DeFi 市场，也不要求资产始终维持在某一种收益策略中。

资本最终使用方向取决于系统当时的流动性需求、市场利率、风险条件、策略容量和整体资产规模。

## 面向多场景的资本层

在这一框架中，稳定币流动性、支付结算、收益型产品和未来符合标准的 RWA 均可成为资本使用方向。不同应用不需要共享相同产品逻辑，但可以在统一流动性和风险管理框架下获得资本支持。

## 流动性不等于 100% 资金利用率

Good Tomorrow 不将资金利用率最大化视为唯一目标。长期运行的金融系统中，100% 资金利用率不意味着效率最高。如果全部资本都配置至缺乏即时退出能力的市场，协议将难以应对用户赎回或市场流动性变化。

Good Tomorrow 追求的是资本利用率、资产流动性和风险控制之间的动态平衡。随着更多资产和应用接入，流动性层可以逐渐成为不同链上金融模块之间的共同资本基础。
""",
    "capital": """# 资本管理

传统收益协议通常按预设规则将用户存入资产配置至有限收益来源。该模式在资金规模较小时可能高效，但随着管理资产扩大，单一策略容量限制会逐渐显现。一个可承载一百万美元的高收益策略，并不意味着能在相同风险收益条件下承载一亿美元。

Good Tomorrow 的资本管理机制建立在“策略容量有限”的基础上。

## 配置标准

协议不会将市场显示的最高 APY 直接作为唯一依据，而会同时评估收益、风险、流动性、退出能力、市场深度、策略容量、系统流动性需求和风险预算。

名义收益率可能随着资金进入而下降，高收益市场也可能伴随更高信用风险、市场风险或退出风险。因此，资本配置必须以风险调整后的实际收益为基础。

## 动态容量

策略容量并非永久固定。市场深度、资产价格、DeFi 需求和流动性条件变化时，最大允许配置规模也可能调整。协议可通过预设参数或后续治理机制降低某一策略资金上限，必要时停止新增资本进入。

## 规模效应

随着 TVL 增长，资本配置结构将相应变化。资产规模较小时，协议可参与规模有限但资本效率较高的市场；资产规模扩大后，系统会逐步提高大型 DeFi 市场、高流动性稳定币市场、短期限金融资产和其他可承载更大规模资本的低风险资产比例。

因此，Good Tomorrow 不承诺随着资金规模增长而维持固定收益率。收益率可能随市场环境、资本规模和策略组合变化。这并非协议效率下降，而是金融系统从高弹性阶段走向规模化资产管理阶段的自然结果。
""",
    "yield": """# 收益与利润分配

Good Tomorrow 的收益模型建立在实际收入原则之上。协议不设定永久固定 APY，也不通过持续增加代币排放人为维持收益水平。

## 收入来源

协议未来可能形成多个收入来源，包括 DeFi 利息、稳定币流动性服务费用、交易及结算费用、市场策略已实现收益、RWA 现金流及其他基础设施服务收入。不同收入来源具有不同风险属性和结算周期，不能简单将市场显示收益率相加。

## 已实现收入原则

在会计层面，Good Tomorrow 区分名义收益、未实现收益和实际已实现收入。只有已经完成结算并能够确认的收入，才进入协议收入核算体系。例如，资产账面价格上涨并不自动意味着协议获得可分配利润；只有相关收益完成结算并实际进入协议资产体系后，才可能成为利润分配基础。

只有可分配净收入为正时，协议才可能进行收益分配。如果某周期内实际收入下降或系统出现已确认损失，用户收益可能相应减少。协议不会为了维持市场宣传收益率而创造不存在的收入。

## 利润分配

完成收入核算后，协议扣除已实现损失、风险准备、流动性储备和必要运营成本。剩余净利润可按协议规则在资金提供者、风险准备体系、协议金库和生态发展等方向之间分配。

这一结构使用户收益与协议实际经营结果直接联系起来。
""",
    "networks": """# 稳定币、支付与 RWA

Good Tomorrow 通过统一流动性层连接多个金融网络。

## 稳定币流动性网络

稳定币是 Good Tomorrow 流动性基础设施的核心组成部分。当前链上价值交换、资产结算和资金调度仍主要依赖稳定币。随着稳定币进入支付、跨境结算和企业金融，其功能将不再局限于加密资产交易。

未来稳定币市场可能同时存在全球美元稳定币、受监管稳定币、区域性稳定币及不同货币计价的链上结算资产。不同稳定币使用场景扩大后，兑换、清算、流动性管理和资本调度需求将持续增加。

Good Tomorrow 的定位不是发行新的稳定币，而是为不同稳定币提供底层流动性支持。协议可以建立统一资本管理框架，使资产按实际需求进入交易、DeFi、支付或其他金融活动。

不同稳定币不会被默认视为相同风险。协议可根据发行机制、储备结构、赎回能力、市场流动性和监管环境设置不同风险参数。部分资产可能仅适合支付结算，另一些资产则可能同时具备 DeFi 和资本配置资格。

## 支付与结算流动性

支付和结算是 Good Tomorrow 从 DeFi 协议发展为链上金融网络的重要方向。支付业务要求资金能够及时完成清算和交付，而不仅是追求资本收益率。

Good Tomorrow 将支付和结算需求视为独立流动性约束。协议需要维持即时可用资产，用于支付、资产兑换、商户结算及其他短期金融需求。

当部分结算资金暂时闲置时，在不影响即时偿付能力的前提下，可按协议规则进入短期、低风险或高流动性金融市场。这类似传统金融中的现金管理逻辑。

## RWA 与链上资本配置

RWA 代币化为链上金融提供新的资本来源和收益市场，但 RWA 与原生 DeFi 资产存在根本差异。其价值依赖现实世界法律关系、发行主体、托管安排和现金流。

RWA 不应被简单视为更高收益的 DeFi 产品。进入 Good Tomorrow 资本体系前，任何 RWA 均需经过独立资产和风险评估，包括信用质量、法律权利结构、违约追索、托管管理、现金流上链路径和赎回退出机制。

RWA 更适合承担长期资本配置角色，而非即时流动性储备。只有在协议满足基础流动性需求，且 RWA 产品期限、风险和退出机制符合要求时，部分资本才可能进入该类资产。

Good Tomorrow 不会将 RWA 描述为无风险收益来源。信用、法律结构、托管、流动性和监管变化均可能影响实际收益和本金安全，因此 RWA 配置比例需要受到严格风险限制。
""",
    "risk": """# 风险、偿付能力与透明度

对于任何管理用户资产的金融系统，收益能力只是系统运行的一部分。真正决定协议能否长期存在的，是其在市场压力和资产损失情况下维持偿付能力的能力。

## 风险管理层次

Good Tomorrow 的风险管理建立在资产层、策略层和协议层三个层次之上。

| 层次 | 范围 |
| --- | --- |
| 资产层 | 为不同资产设定最大存入规模、最大配置比例和最低流动性要求。 |
| 策略层 | 对每一种资本配置活动设置风险预算限制。 |
| 协议层 | 持续监测资产流动性、赎回需求、资本利用率和市场波动。 |

市场异常时，协议可以提高即时流动性比例、降低新资金配置速度，或停止进入风险增加的市场。

## 风险准备金

协议可以从实际收入中提取一定比例建立风险准备金。风险准备金不属于普通收益分配，而是用于应对策略损失、DeFi 违约、清算失败或外部协议风险。

短期看，保留风险准备金可能降低用户即时收益；长期看，风险缓冲是提高协议持续运行能力的必要条件。

## 链上透明度与财务验证

Good Tomorrow 的长期目标是建立与协议资本结构相对应的链上透明体系，使用户理解协议管理资产规模、流动性资产比例、已部署资本规模，以及收益来源。

协议将逐步建立储备证明、资金利用证明和收益证明机制。储备证明展示协议资产及储备情况；资金利用证明展示用户资产在不同金融模块中的配置状态；收益证明展示已实现收入及主要来源。

三者共同说明资产是否被安全使用，以及协议是否已经获得实际收入。长期来看，协议透明度应逐步转向链上数据、公开地址和可验证智能合约状态。
""",
    "token": """# 代币与治理

## 原生代币

Good Tomorrow 是 Good Tomorrow 协议的原生生态代币，计划部署于 BNB Smart Chain。总代币供应量固定为 **10,000,000 枚 Good Tomorrow**。

初始代币结构采用相对简单的分配模式，不设置传统意义上的多轮私募、机构投资人和复杂早期解锁结构。代币供应主要由初始流动性、长期锁仓部分和生态增长部分组成。

![原始代币供应图](../../.gitbook/assets/image3.png)

| 分配类别 | 数量 | 占总供应量 |
| --- | ---: | ---: |
| Good Tomorrow/USDC 初始流动性 | 9,000,000 | 90% |
| 长期锁仓及释放 | 900,000 | 9% |
| 市场与生态增长 | 100,000 | 1% |
| 总计 | 10,000,000 | 100% |

9% 的长期锁仓部分将在项目启动后前 12 个月完全锁定。锁定期结束后，代币将在未来 12 个月内线性释放。若平均线性释放，第 13 至第 24 个月每月理论释放量为：

$$
\\frac{900,000}{12}=75,000
$$

剩余 100,000 枚代币用于市场、社区和生态发展，包括早期用户增长、生态合作、社区建设及其他长期发展相关活动。

## 协议治理

随着 Good Tomorrow 管理资产规模和金融模块增加，协议治理将逐步成为资本管理体系的重要组成部分。

治理目标不是简单地对所有参数进行社区投票，而是在去中心化决策与专业风险管理之间建立合理边界。一般生态发展事项可逐步交由社区治理，但资本配置比例、资产风险参数和重大金融风险事件需要更强保护，避免短期投票带来治理攻击和市场操纵风险。

Good Tomorrow 未来可形成由协议治理、风险管理机制和链上执行共同组成的结构。代币持有者可参与协议发展方向、资产接入和生态建设等事项，并随着治理机制成熟逐步控制更多协议参数。
""",
    "roadmap": """# 发展路线图

Good Tomorrow 的发展将以链上流动性为核心基础，从 DeFi 资本管理体系出发，逐步构建覆盖稳定币、链上金融、支付结算及 RWA 的流动性金融基础设施。

![原始发展路径图](../../.gitbook/assets/image4.png)

长期发展路径为：

**DeFi 流动性 -> 稳定币流动性 -> 多资产资本网络 -> 支付与结算流动性 -> RWA 流动性 -> Onchain Financial Infrastructure**

## 第一阶段：流动性基础层

建立基础金融协议架构；完成资产存入与赎回机制；建立统一流动性管理体系；构建基础风险参数与资产管理框架；部署 Good Tomorrow/USDC 初始流动性市场；完成核心智能合约测试与安全审计。

目标：建立第一层流动性基础设施，使用户资产能够进入统一、透明且可验证的链上资本管理体系。

## 第二阶段：DeFi 资本网络

从单一流动性管理进入链上资本配置，接入主流 DeFi 金融市场，构建借贷、流动性和收益型资本配置能力，建立动态资金利用率模型，引入策略容量管理与风险预算机制，并实现多市场资本调度。

基础循环为：**流动性 -> 借贷 -> 收益 -> 再分配**。

## 第三阶段：稳定币流动性网络

扩展多稳定币资产支持，建立稳定币资产接入与风险评级机制，连接主流美元稳定币市场，探索区域性稳定币与合规稳定币流动性需求，并构建稳定币之间的资本调度与流动性支持能力。

未来方向包括 USD Stablecoins、Regional Stablecoins、HKD Stablecoins、Payment Stablecoins 和 Regulated Stablecoins。

## 第四阶段：支付与结算流动性基础设施

进入稳定币支付与链上结算市场，构建支付场景下的即时流动性管理能力，支持商户结算与资金调度，探索跨境支付与多稳定币结算机制，并连接支付网络与 DeFi 流动性。

链上资金循环为：**Payment -> Settlement -> Liquidity -> Yield**。

## 第五阶段：RWA 流动性基础设施

逐步接入符合协议风险标准的 RWA，建立 RWA 接入、风险评估和流动性管理框架，探索国债、债券、基金、票据及其他现实世界收益资产的链上流动性需求，建立稳定币与现实世界资产之间的资本连接，并支持不同期限和风险等级资产组合配置。

资本循环为：**Stablecoin Liquidity <-> Onchain Capital <-> Real World Assets**。

## 第六阶段：多生态流动性网络

随着稳定币、支付网络、DeFi 协议和 RWA 资产逐步接入，Good Tomorrow 将发展统一流动性网络，使不同金融应用共享流动性管理、资本配置、稳定币支持、支付与结算流动性、RWA 接入、风险管理和收益结算能力。

## 第七阶段：Onchain Financial Infrastructure

最终，Good Tomorrow 希望建立覆盖链上与现实世界金融需求的流动性金融基础设施。稳定币成为价值流通媒介，DeFi 提供开放金融市场，Good Tomorrow 提供统一流动性与资本管理能力，支付网络提供现实商业场景，RWA 将现实世界资产带入链上。
""",
    "vision": """# 长期愿景

Good Tomorrow 的长期目标不是成为另一个单一功能的 DeFi 协议。随着稳定币、DeFi、支付和现实世界资产逐渐进入区块链，未来链上金融市场将面临更基础的问题：不同资产和金融产品如何共享资本、管理流动性，并在扩大规模时保持系统稳定。

Good Tomorrow 希望成为这一体系中的资本基础层。

早期阶段，流动性基础设施主要服务于稳定币和链上金融市场。随着 DeFi 模块加入，资本开始产生基于真实资金需求的利息收入。随着支付和结算业务发展，流动性获得真实商业使用场景。随着 RWA 接入，协议资本配置范围可延伸至更广泛金融市场。

这些模块并非彼此独立。DeFi 产生利息需求，支付产生结算需求，稳定币产生兑换和流动性需求，RWA 提供新的资产配置方向。Good Tomorrow 的作用，是通过统一资本和风险管理体系将这些需求连接起来。

从长期发展路径看，Good Tomorrow 将经历从流动性协议到金融基础设施，再到 Onchain Financial Network 的演进。

协议最终价值不在于提供固定收益率，而在于建立一套能够长期管理链上资本、识别真实收益来源并服务多个金融市场的基础系统。
""",
    "references": CONTENT["en"]["references"],
}

CONTENT["ko"] = {
    "home": """# Good Tomorrow

Good Tomorrow는 BNB Smart Chain 위에 구축되는 온체인 유동성 금융 인프라 프로토콜입니다. 핵심 대상은 스테이블코인, 실물자산(RWA), 결제 생태계입니다.

프로토콜의 중심은 통합 자본 관리 프레임워크입니다. 조건을 충족한 사용자 자산은 공통 유동성 및 자산부채 관리 체계로 들어가며, 이후 유동성 수요, 시장 금리, 리스크 파라미터, 전략 수용 능력에 따라 스테이블코인 유동성, 수익 전략, 결제와 청산, 향후 기준을 충족하는 RWA 활동에 배분될 수 있습니다.

Good Tomorrow는 고정 APY를 약속하거나 토큰 인센티브를 장기 수익의 주된 원천으로 삼지 않습니다. 수익 모델은 실제 금융 수입을 기준으로 하며, 실현 손실, 리스크 준비금, 유동성 준비금, 필요한 운영비를 차감한 뒤 남은 배분 가능 순이익을 프로토콜 규칙에 따라 분배합니다.
""",
    "overview": """# 개요

## 요약

DeFi는 탈중앙화 거래, 대출, 스테이블코인, 자산 관리, RWA 토큰화 등 여러 금융 원형을 만들어 왔습니다. 그러나 현재 온체인 금융은 여전히 매우 분절되어 있습니다. 스테이블코인 유동성은 여러 프로토콜과 애플리케이션에 흩어져 있고, DeFi, 결제, 자산 관리, 수익 상품 사이에는 자본을 통합 조정하는 장치가 부족합니다.

DeFi 수익의 원천도 명확하지 않은 경우가 많습니다. 일부 수익은 실제 DeFi 이자, 거래 수수료, 투자 수익에서 나오지만, 일부는 프로토콜 토큰 인센티브나 보조금에서 나옵니다. 통합 자본 관리가 없으면 사용자는 자산의 용도, 자본 활용도, 수익의 실제 출처를 판단하기 어렵습니다.

## 배경

DeFi는 공개 스마트 컨트랙트를 통해 거래와 유동성 공급을 가능하게 했습니다. 탈중앙화 거래소는 거래와 가격 발견을 제공하고, 대출 프로토콜은 자본 시장을 형성하며, 스테이블코인은 온체인 거래와 결제의 기본 매개체가 되었습니다. RWA 토큰화는 온체인 자본의 배분 범위를 더 넓힙니다.

하지만 각 프로토콜은 대부분 독립적으로 자본을 관리합니다. 사용자는 스테이블코인을 DeFi에 예치하거나 유동성을 제공하거나 수익 전략에 참여할 수 있지만, 자본은 특정 장소 안에서만 움직이는 경우가 많습니다.

## 문제 정의

### 유동성 분절

스테이블코인과 기타 온체인 자산은 체인, 거래 시장, 프로토콜, 결제 시스템에 나뉘어 있습니다. 각 프로토콜은 자체 유동성 풀과 자본 관리 체계를 운영하므로 자본이 여러 금융 수요 사이에서 통합적으로 배분되지 못합니다.

### 불투명한 수익 원천

APY는 중요한 지표이지만 수익의 출처를 설명하지는 않습니다. Good Tomorrow는 실제 금융 수입에 기반한 수익 계산 방식을 사용하고, 자본 활용, 수입 원천, 리스크 준비금을 점진적으로 온체인에서 투명하게 만들고자 합니다.

### 자본 규모와 전략 수용 능력의 불일치

자본 규모 확대가 곧 자본 효율 향상을 의미하지는 않습니다. 많은 전략에는 수용 한도가 있습니다. Good Tomorrow는 정적인 배분 모델 대신 시스템 규모, 시장 금리, 유동성 수요, 전략 수용 능력에 따라 자본 배분을 동적으로 조정합니다.
""",
    "architecture": """# 프로토콜 아키텍처

Good Tomorrow는 유동성을 기반으로 하는 온체인 금융 인프라입니다. 운영 흐름은 자산 예치, 유동성 관리, 자본 배분, 금융 활동, 수익 정산, 이익 분배로 구성됩니다.

![원문 중국어 자본 흐름도](../../.gitbook/assets/image1.png)

| 단계 | 기능 |
| --- | --- |
| 자산 예치 | 적격 사용자 자산이 프로토콜에 들어옵니다. |
| 유동성 관리 | 상환, 결제, 정상 운영에 필요한 준비금을 유지합니다. |
| 자본 배분 | 시장 수요, 활용률, 리스크 파라미터, 전략 수용 능력에 따라 자본을 배치합니다. |
| 금융 활동 | 거래, 스테이블코인 유동성, 결제, 수익 전략, 적격 RWA를 지원합니다. |
| 수익 정산 | 실현 수입을 확인하고 집계합니다. |
| 이익 분배 | 손실, 준비금, 비용 차감 후 배분합니다. |

![원문 중국어 시스템 아키텍처](../../.gitbook/assets/image2.png)

Good Tomorrow의 핵심 모듈은 유동성 계층, 리스크 계층, 자본 배분 계층, 수익 정산 계층, 이익 분배 계층입니다. 이 모듈들은 독립적으로 움직이지 않고 하나의 금융 운영 프레임워크를 이룹니다.

프로토콜의 목적은 모든 자본을 단일 고수익 전략에 집중하는 것이 아닙니다. 서로 다른 유동성 요구, 리스크 수준, 사용 기간을 가진 자금을 여러 금융 활동에 배치하면서 안전성, 유동성, 자본 효율의 균형을 유지하는 것입니다.
""",
    "liquidity": """# 유동성 인프라

Good Tomorrow의 기본 판단은 명확합니다. 온체인 금융에는 자산과 상품이 부족한 것이 아니라, 서로 다른 금융 수요를 통합 조정할 수 있는 유동성 인프라가 부족합니다.

스테이블코인, DeFi 시장, DEX, 수익 프로토콜, RWA는 각각 독립적으로 발전했습니다. 대부분의 프로토콜은 자체 유동성 풀, 리스크 모델, 자금 사용 규칙을 유지하며, 자본은 특정 애플리케이션 내부에서만 순환합니다.

Good Tomorrow는 유동성을 단일 풀의 정적인 자산이 아니라 관리와 배분이 가능한 금융 자원으로 봅니다. 예치된 자산은 통합 자산부채 관리 체계에 들어가며, 최종 사용처는 당시의 유동성 수요, 시장 금리, 리스크 조건, 전략 수용 능력, 전체 자산 규모에 따라 결정됩니다.

목표는 100% 자금 활용률이 아닙니다. 모든 자본이 즉시 회수하기 어려운 시장에 배치되면 상환이나 유동성 충격에 대응할 수 없습니다. Good Tomorrow는 자본 활용도, 자산 유동성, 리스크 통제 사이의 동적 균형을 추구합니다.
""",
    "capital": """# 자본 관리

전통적인 수익 프로토콜은 사용자가 예치한 자산을 정해진 규칙에 따라 제한된 수익원에 배분하는 경우가 많습니다. 자본이 작을 때는 효율적일 수 있지만, 운용 규모가 커지면 전략 수용 능력의 한계가 드러납니다.

Good Tomorrow는 가장 높은 표시 APY만을 기준으로 자본을 배분하지 않습니다. 예상 수익, 시장 및 신용 리스크, 자산 유동성, 회수 가능성, 시장 깊이, 전략 수용 능력, 시스템 전체 유동성 수요, 리스크 예산을 함께 평가합니다.

전략 수용 능력은 고정되어 있지 않습니다. 시장 깊이, 자산 가격, DeFi 수요, 유동성 조건이 바뀌면 허용 배분 규모도 조정될 수 있습니다. 필요하면 특정 전략의 한도를 낮추거나 신규 자본 유입을 중단할 수 있습니다.

TVL이 커질수록 배분 구조도 바뀔 수 있습니다. 초기에는 규모가 작지만 효율이 높은 시장에 접근할 수 있고, 규모가 커지면 대형 DeFi 시장, 고유동성 스테이블코인 시장, 단기 금융 자산, 더 많은 자본을 감당할 수 있는 저위험 자산의 비중이 높아질 수 있습니다.
""",
    "yield": """# 수익과 이익 분배

Good Tomorrow의 수익 모델은 실제 수입 원칙에 기반합니다. 프로토콜은 영구 고정 APY를 설정하지 않으며, 지속적인 토큰 발행으로 홍보 수익률을 유지하지 않습니다.

잠재적 수입원에는 DeFi 이자, 스테이블코인 유동성 서비스 수수료, 거래 및 정산 수수료, 시장 전략의 실현 수익, RWA 현금흐름, 기타 인프라 서비스 수입이 포함됩니다.

회계적으로 Good Tomorrow는 명목 수익, 미실현 수익, 실제 실현 수입을 구분합니다. 정산이 완료되고 확인 가능한 수입만 프로토콜 수익 회계에 들어갑니다. 자산의 장부가 상승은 그 자체로 배분 가능 이익이 아닙니다.

배분 가능 순수입이 양수일 때만 수익 분배가 가능합니다. 수입이 줄거나 확정 손실이 발생하면 사용자 수익도 줄어들 수 있습니다. 수입 인식 후에는 실현 손실, 리스크 준비금, 유동성 준비금, 운영비를 차감하고 남은 순이익을 자금 제공자, 리스크 준비 체계, 프로토콜 금고, 생태계 발전에 배분할 수 있습니다.
""",
    "networks": """# 스테이블코인, 결제, RWA

Good Tomorrow는 하나의 유동성 계층으로 여러 금융 네트워크를 연결하도록 설계되었습니다.

스테이블코인은 온체인 가치 교환, 자산 정산, 자본 배분의 핵심 매개체입니다. 향후 시장에는 글로벌 USD 스테이블코인, 규제형 스테이블코인, 지역 스테이블코인, 여러 통화 기준 온체인 결제 자산이 공존할 수 있습니다. Good Tomorrow는 새로운 스테이블코인을 발행하는 것이 아니라 다양한 스테이블코인에 기초 유동성을 제공하는 것을 목표로 합니다.

결제와 정산은 Good Tomorrow가 DeFi 프로토콜에서 온체인 금융 네트워크로 발전하는 중요한 방향입니다. 결제 시스템은 높은 수익률보다 적시에 청산과 전달이 가능한 자본을 필요로 합니다. 따라서 프로토콜은 즉시 사용 가능한 자산을 유지하면서, 일시적으로 유휴 상태인 결제 자금을 단기, 저위험, 고유동성 시장에 배치할 수 있습니다.

RWA 토큰화는 새로운 자본 원천과 수익 시장을 열지만, RWA의 가치는 법적 관계, 발행 주체, 보관 구조, 현실 세계 현금흐름에 의존합니다. Good Tomorrow는 RWA를 무위험 고수익 상품으로 보지 않습니다. 편입 전에는 신용 품질, 법적 권리, 부도 시 회수, 보관, 현금흐름의 온체인 연결, 상환 출구를 평가해야 하며, 비중은 엄격한 리스크 한도를 따라야 합니다.
""",
    "risk": """# 리스크, 지급능력, 투명성

사용자 자산을 관리하는 금융 시스템에서 장기 생존을 결정하는 것은 시장 스트레스와 자산 손실 상황에서도 지급능력을 유지하는 능력입니다.

Good Tomorrow의 리스크 관리는 자산 계층, 전략 계층, 프로토콜 계층으로 구성됩니다. 자산 계층은 최대 예치 규모, 최대 배분 비율, 최소 유동성 요구를 설정합니다. 전략 계층은 각 자본 배분 활동에 리스크 예산을 적용합니다. 프로토콜 계층은 유동성, 상환 수요, 자본 활용률, 시장 변동성을 지속적으로 모니터링합니다.

프로토콜은 실제 수입 일부를 리스크 준비금으로 적립할 수 있습니다. 이 준비금은 일반 수익 분배 대상이 아니며 전략 손실, DeFi 디폴트, 청산 실패, 외부 프로토콜 리스크에 대응하기 위한 것입니다.

장기적으로 Good Tomorrow는 준비금 증명, 자본 활용 증명, 수익 증명을 구축하려 합니다. 사용자는 프로토콜이 얼마의 자산을 관리하는지, 얼마가 유동성으로 남아 있는지, 얼마가 배치되었는지, 어떤 활동이 실현 수입을 만들었는지 이해할 수 있어야 합니다.
""",
    "token": """# 토큰과 거버넌스

Good Tomorrow는 Good Tomorrow 프로토콜의 네이티브 생태계 토큰이며 BNB Smart Chain 배포를 계획합니다. 총 공급량은 **10,000,000 Good Tomorrow**로 고정됩니다.

![원문 중국어 토큰 공급표](../../.gitbook/assets/image3.png)

| 배분 항목 | 수량 | 총 공급량 비중 |
| --- | ---: | ---: |
| Good Tomorrow/USDC 초기 유동성 | 9,000,000 | 90% |
| 장기 락업 및 릴리스 | 900,000 | 9% |
| 시장 및 생태계 성장 | 100,000 | 1% |
| 합계 | 10,000,000 | 100% |

장기 락업 물량 9%는 출시 후 첫 12개월 동안 완전히 잠기고, 이후 12개월 동안 선형으로 릴리스됩니다. 균등 월별 릴리스 기준 이론적 월 릴리스 물량은 다음과 같습니다.

$$
\\frac{900,000}{12}=75,000
$$

거버넌스는 탈중앙화 의사결정과 전문 리스크 관리 사이의 경계를 설정해야 합니다. 일반 생태계 발전 사항은 점진적으로 커뮤니티 거버넌스로 이전될 수 있지만, 자본 배분 비율, 자산 리스크 파라미터, 중대한 금융 리스크 사건은 거버넌스 공격과 시장 조작을 막기 위한 강한 보호가 필요합니다.
""",
    "roadmap": """# 개발 로드맵

Good Tomorrow는 온체인 유동성을 핵심 기반으로 삼아 DeFi 자본 관리에서 출발하고, 스테이블코인, 온체인 금융, 결제와 정산, RWA 유동성 인프라로 확장합니다.

![원문 중국어 로드맵](../../.gitbook/assets/image4.png)

장기 경로는 **DeFi Liquidity -> Stablecoin Liquidity -> Multi-Asset Capital Network -> Payment and Settlement Liquidity -> RWA Liquidity -> Onchain Financial Infrastructure**입니다.

## 1단계: 유동성 기반 계층

기초 금융 프로토콜 아키텍처, 예치와 상환, 통합 유동성 관리, 기본 리스크 파라미터, Good Tomorrow/USDC 초기 유동성 시장, 핵심 스마트 컨트랙트 테스트와 보안 감사를 완료합니다.

## 2단계: DeFi 자본 네트워크

주요 DeFi 금융 시장을 연결하고, 대출·유동성·수익형 자본 배분 능력, 동적 자금 활용 모델, 전략 수용 능력 관리와 리스크 예산을 구축합니다. 기본 순환은 **Liquidity -> Lending -> Yield -> Redistribution**입니다.

## 3단계: 스테이블코인 유동성 네트워크

다중 스테이블코인 지원, 자산 편입과 리스크 등급, 주요 USD 스테이블코인 시장 연결, 지역 및 규제형 스테이블코인 수요 탐색을 진행합니다.

## 4단계: 결제와 정산 유동성 인프라

스테이블코인 결제와 온체인 정산 시장에 진입하고, 즉시 유동성 관리, 가맹점 정산, 크로스보더 결제, 다중 스테이블코인 정산, DeFi 유동성과 결제 네트워크 연결을 구축합니다.

## 5단계: RWA 유동성 인프라

리스크 기준을 충족하는 RWA를 점진적으로 연결하고, 국채, 채권, 펀드, 어음 등 현실 세계 수익 자산의 온체인 유동성 수요를 탐색합니다.

## 6-7단계: 다중 생태계 유동성 네트워크와 온체인 금융 인프라

스테이블코인, 결제 네트워크, DeFi 프로토콜, RWA 자산이 연결되면 Good Tomorrow는 여러 금융 애플리케이션이 공유하는 통합 유동성 네트워크로 발전하고, 최종적으로 온체인과 현실 세계 금융 수요를 포괄하는 인프라가 되는 것을 목표로 합니다.
""",
    "vision": """# 장기 비전

Good Tomorrow의 장기 목표는 또 하나의 단일 기능 DeFi 프로토콜이 되는 것이 아닙니다. 스테이블코인, DeFi, 결제, 현실 세계 자산이 블록체인으로 이동할수록 핵심 질문은 서로 다른 자산과 금융 상품이 어떻게 자본을 공유하고, 유동성을 관리하며, 규모가 커져도 안정성을 유지할 수 있는가입니다.

Good Tomorrow는 이 체계의 자본 기반 계층이 되고자 합니다. DeFi는 이자 수요를 만들고, 결제는 정산 수요를 만들며, 스테이블코인은 교환과 유동성 수요를 만들고, RWA는 새로운 배분 방향을 제공합니다. Good Tomorrow는 통합 자본 및 리스크 관리로 이 수요들을 연결합니다.

궁극적 가치는 고정 수익률이 아니라, 온체인 자본을 장기적으로 관리하고 실제 수입 원천을 식별하며 여러 금융 시장에 서비스를 제공할 수 있는 기반 시스템을 만드는 데 있습니다.
""",
    "references": CONTENT["en"]["references"],
}

CONTENT["ja"] = {
    "home": """# Good Tomorrow

Good Tomorrow は、BNB Smart Chain 上に構築されるオンチェーン流動性金融インフラプロトコルです。対象領域はステーブルコイン、現実世界資産（RWA）、決済エコシステムです。

プロトコルの中心には統合資本管理フレームワークがあります。条件を満たすユーザー資産は共通の流動性および資産負債管理システムに入り、その後、流動性需要、市場金利、リスクパラメータ、戦略キャパシティに応じて、ステーブルコイン流動性、収益戦略、決済・清算、将来基準を満たす RWA 活動に配分されます。

Good Tomorrow は固定 APY を約束せず、トークンインセンティブを長期収益の主な源泉としません。収益モデルは実際の金融収入に基づき、実現損失、リスク準備金、流動性準備金、必要な運営コストを差し引いた後の分配可能純利益を、プロトコル規則に従って分配します。
""",
    "overview": """# 概要

## 要約

DeFi は、分散型取引、レンディング、ステーブルコイン、資産管理、RWA トークン化など多くの金融プリミティブを形成してきました。しかし現在のオンチェーン金融は依然として高度に断片化されています。ステーブルコイン流動性は複数のプロトコルとアプリケーションに分散し、DeFi、決済、資産管理、収益商品を横断する統一的な資本調整メカニズムが不足しています。

DeFi の収益源も一様ではありません。実際の DeFi 利息、取引手数料、投資収益から生じるものもあれば、プロトコルトークンインセンティブや補助金に依存するものもあります。統一資本管理がなければ、ユーザーは資産の用途、資本利用率、収益の真の源泉を判断しにくくなります。

## 背景

DeFi は公開スマートコントラクトを通じて取引と流動性提供を可能にしました。DEX は取引と価格発見を提供し、レンディングプロトコルは資本市場を形成し、ステーブルコインはオンチェーン取引と決済の基本媒体となりました。RWA トークン化はオンチェーン資本の配分範囲をさらに広げます。

それでも資本管理は多くの場合、各プロトコル内で独立しています。ユーザーはステーブルコインを DeFi に預けたり、流動性を提供したり、収益戦略に参加できますが、資本は孤立したシステム内にとどまりがちです。

## 課題

### 流動性の断片化

ステーブルコインとその他オンチェーン資産は、チェーン、取引市場、プロトコル、決済システムに分散しています。各プロトコルが独自の流動性プールと資本管理モデルを持つため、異なる金融需要の間で資本を統合的に配分できません。

### 不透明な収益源

APY は重要な指標ですが、収益源を説明するものではありません。Good Tomorrow は実際の金融収入に基づく収益計算を採用し、資本利用、収入源、リスク準備金を段階的にオンチェーンで透明化することを目指します。

### 資本規模と戦略キャパシティの不一致

資本規模の拡大は自動的に効率向上を意味しません。多くの戦略には容量制約があります。Good Tomorrow は静的配分モデルではなく、システム規模、市場金利、流動性需要、戦略キャパシティに応じて資本配分を動的に調整します。
""",
    "architecture": """# プロトコルアーキテクチャ

Good Tomorrow は流動性を基盤とするオンチェーン金融インフラです。運用フローは、資産預入、流動性管理、資本配分、金融活動、収益精算、利益分配で構成されます。

![原文中国語の資本フロー図](../../.gitbook/assets/image1.png)

| 段階 | 機能 |
| --- | --- |
| 資産預入 | 適格ユーザー資産がプロトコルに入ります。 |
| 流動性管理 | 償還、決済、通常運用に必要な準備を維持します。 |
| 資本配分 | 市場需要、利用率、リスクパラメータ、戦略キャパシティにより資本を配分します。 |
| 金融活動 | 取引、ステーブルコイン流動性、決済、収益戦略、適格 RWA を支援します。 |
| 収益精算 | 実現収入を確認し集計します。 |
| 利益分配 | 損失、準備金、コストを差し引いて分配します。 |

![原文中国語のシステムアーキテクチャ](../../.gitbook/assets/image2.png)

主要モジュールは、流動性レイヤー、リスクレイヤー、資本配分レイヤー、収益精算レイヤー、利益分配レイヤーです。これらは独立して動くのではなく、共通の金融運用フレームワークを形成します。

Good Tomorrow の目的は、すべての資本を単一の高収益戦略に集中させることではありません。異なる流動性需要、リスク水準、利用期間を持つ資金を複数の金融活動に配分しながら、安全性、流動性、資本効率の均衡を維持することです。
""",
    "liquidity": """# 流動性インフラ

Good Tomorrow の基本的な判断は、オンチェーン金融には資産や商品が不足しているのではなく、異なる金融需要を統合的に調整できる流動性インフラが不足しているというものです。

ステーブルコイン、DeFi 市場、DEX、収益プロトコル、RWA はそれぞれ独立して発展してきました。多くのプロトコルは独自の流動性プール、リスクモデル、資金利用ルールを維持し、資本は特定アプリケーションの内部で循環します。

Good Tomorrow は流動性を単一プール内の静的資産ではなく、管理・配分できる金融資源として捉えます。預け入れられた資産は統合資産負債管理に入り、最終的な利用先はその時点の流動性需要、市場金利、リスク条件、戦略キャパシティ、全体資産規模によって決まります。

目標は 100% の資金利用率ではありません。すべての資本を即時退出が難しい市場に配分すると、償還や流動性ショックに対応できません。Good Tomorrow は資本利用率、資産流動性、リスク管理の動的均衡を追求します。
""",
    "capital": """# 資本管理

従来の収益プロトコルは、ユーザー資産を事前設定された規則に従って限られた収益源に配分することが多くあります。小規模では効率的でも、運用資産が拡大すると戦略キャパシティの限界が現れます。

Good Tomorrow は、表示 APY が最も高い市場だけを基準に資本を配分しません。期待収益、市場および信用リスク、資産流動性、退出可能性、市場深度、戦略キャパシティ、システム全体の流動性需要、リスク予算を同時に評価します。

戦略キャパシティは固定ではありません。市場深度、資産価格、DeFi 需要、流動性条件が変化すれば、許容配分規模も変化します。必要に応じて特定戦略の上限を下げたり、新規資本流入を停止したりできます。

TVL が拡大すると、配分構造も変わります。初期には小規模だが効率の高い市場にアクセスでき、規模拡大後は大型 DeFi 市場、高流動性ステーブルコイン市場、短期金融資産、より大きな資本を受け入れられる低リスク資産の比率が高まる可能性があります。
""",
    "yield": """# 収益と利益分配

Good Tomorrow の収益モデルは実際の収入原則に基づきます。プロトコルは恒久的な固定 APY を設定せず、継続的なトークン発行で宣伝利回りを維持しません。

将来の収入源には、DeFi 利息、ステーブルコイン流動性サービス手数料、取引・精算手数料、市場戦略の実現利益、RWA のキャッシュフロー、その他インフラサービス収入が含まれます。

会計上、Good Tomorrow は名目収益、未実現利益、実際に実現した収入を区別します。精算が完了し確認可能な収入のみがプロトコルの収益会計に入ります。資産の帳簿価格上昇は、それだけで分配可能利益にはなりません。

分配可能純収入がプラスの場合にのみ、収益分配が可能です。実際の収入が低下したり確認済み損失が発生したりすれば、ユーザー収益も減少します。収入認識後、実現損失、リスク準備金、流動性準備金、運営費を差し引き、残りの純利益を資金提供者、リスク準備体系、プロトコル金庫、エコシステム発展に配分できます。
""",
    "networks": """# ステーブルコイン、決済、RWA

Good Tomorrow は、ひとつの流動性レイヤーを通じて複数の金融ネットワークを接続する設計です。

ステーブルコインはオンチェーンの価値交換、資産精算、資本配分の中核媒体です。将来の市場では、グローバル USD ステーブルコイン、規制対応ステーブルコイン、地域ステーブルコイン、複数通貨建てオンチェーン決済資産が共存する可能性があります。Good Tomorrow は新しいステーブルコインを発行するのではなく、各種ステーブルコインに基礎流動性を提供することを目指します。

決済と清算は、Good Tomorrow が DeFi プロトコルからオンチェーン金融ネットワークへ発展する重要な方向です。決済システムが必要とするのは高利回りだけでなく、必要な時に清算と引き渡しを完了できる資本です。プロトコルは即時利用可能な資産を維持しつつ、一時的に遊休状態の決済資金を短期、低リスク、高流動性市場に配分できます。

RWA トークン化は新しい資本源と収益市場を開きますが、RWA の価値は法的関係、発行主体、保管構造、現実世界のキャッシュフローに依存します。Good Tomorrow は RWA を無リスク高収益商品とは見なしません。組み入れ前に信用品質、法的権利、デフォルト時の回収、保管、キャッシュフローのオンチェーン連携、償還出口を評価し、比率は厳格なリスク上限に従う必要があります。
""",
    "risk": """# リスク、支払能力、透明性

ユーザー資産を管理する金融システムにおいて、長期的な存続を決めるのは市場ストレスや資産損失時にも支払能力を維持できるかどうかです。

Good Tomorrow のリスク管理は、資産レイヤー、戦略レイヤー、プロトコルレイヤーで構成されます。資産レイヤーでは最大預入規模、最大配分比率、最低流動性要件を設定します。戦略レイヤーでは各資本配分活動にリスク予算を適用します。プロトコルレイヤーでは流動性、償還需要、資本利用率、市場変動を継続監視します。

プロトコルは実際の収入の一部をリスク準備金として積み立てることができます。この準備金は通常の収益分配対象ではなく、戦略損失、DeFi デフォルト、清算失敗、外部プロトコルリスクに対応するためのものです。

長期的に Good Tomorrow は、準備金証明、資本利用証明、収益証明を構築することを目指します。ユーザーはプロトコルが管理する資産規模、流動性として残る資産、配分済み資本、実現収入を生んだ活動を理解できるようになるべきです。
""",
    "token": """# トークンとガバナンス

Good Tomorrow は Good Tomorrow プロトコルのネイティブエコシステムトークンであり、BNB Smart Chain への展開を予定しています。総供給量は **10,000,000 Good Tomorrow** に固定されます。

![原文中国語のトークン供給表](../../.gitbook/assets/image3.png)

| 配分区分 | 数量 | 総供給量比率 |
| --- | ---: | ---: |
| Good Tomorrow/USDC 初期流動性 | 9,000,000 | 90% |
| 長期ロックアップとリリース | 900,000 | 9% |
| 市場・エコシステム成長 | 100,000 | 1% |
| 合計 | 10,000,000 | 100% |

長期ロックアップ分 9% はローンチ後最初の 12 か月間完全にロックされ、その後 12 か月にわたり線形にリリースされます。均等月次リリースの場合、理論上の月次リリース量は次の通りです。

$$
\\frac{900,000}{12}=75,000
$$

ガバナンスは、分散型意思決定と専門的リスク管理の境界を明確にする必要があります。一般的なエコシステム発展事項は段階的にコミュニティガバナンスへ移行できますが、資本配分比率、資産リスクパラメータ、重大な金融リスク事象には、ガバナンス攻撃や市場操作を防ぐ強い保護が必要です。
""",
    "roadmap": """# 開発ロードマップ

Good Tomorrow はオンチェーン流動性を中核基盤とし、DeFi 資本管理から始まり、ステーブルコイン、オンチェーン金融、決済・清算、RWA 流動性インフラへ拡張します。

![原文中国語のロードマップ](../../.gitbook/assets/image4.png)

長期経路は **DeFi Liquidity -> Stablecoin Liquidity -> Multi-Asset Capital Network -> Payment and Settlement Liquidity -> RWA Liquidity -> Onchain Financial Infrastructure** です。

## フェーズ1：流動性基盤レイヤー

基礎金融プロトコルアーキテクチャ、預入と償還、統合流動性管理、基本リスクパラメータ、Good Tomorrow/USDC 初期流動性市場、コアスマートコントラクトのテストとセキュリティ監査を完了します。

## フェーズ2：DeFi 資本ネットワーク

主要 DeFi 金融市場を接続し、レンディング、流動性、収益型資本配分能力、動的資金利用モデル、戦略キャパシティ管理、リスク予算を構築します。基本循環は **Liquidity -> Lending -> Yield -> Redistribution** です。

## フェーズ3：ステーブルコイン流動性ネットワーク

複数ステーブルコイン対応、資産組み入れとリスク格付け、主要 USD ステーブルコイン市場との接続、地域および規制対応ステーブルコイン需要の探索を進めます。

## フェーズ4：決済・清算流動性インフラ

ステーブルコイン決済とオンチェーン清算市場に入り、即時流動性管理、加盟店決済、クロスボーダー決済、複数ステーブルコイン清算、DeFi 流動性との接続を構築します。

## フェーズ5：RWA 流動性インフラ

リスク基準を満たす RWA を段階的に接続し、国債、債券、ファンド、手形など現実世界収益資産のオンチェーン流動性需要を探索します。

## フェーズ6-7：複数エコシステム流動性ネットワークとオンチェーン金融インフラ

ステーブルコイン、決済ネットワーク、DeFi プロトコル、RWA 資産が接続されると、Good Tomorrow は複数の金融アプリケーションが共有する統合流動性ネットワークへ発展し、最終的にオンチェーンと現実世界の金融需要を包含するインフラを目指します。
""",
    "vision": """# 長期ビジョン

Good Tomorrow の長期目標は、単一機能の DeFi プロトコルになることではありません。ステーブルコイン、DeFi、決済、現実世界資産がブロックチェーンへ移行するほど、異なる資産や金融商品がどのように資本を共有し、流動性を管理し、規模拡大時にも安定性を維持するかが重要になります。

Good Tomorrow はこの体系の資本基盤レイヤーを目指します。DeFi は利息需要を生み、決済は清算需要を生み、ステーブルコインは交換と流動性需要を生み、RWA は新たな配分方向を提供します。Good Tomorrow は統合資本管理とリスク管理によってこれらの需要を接続します。

最終的な価値は固定利回りではなく、オンチェーン資本を長期的に管理し、実際の収入源を識別し、複数の金融市場にサービスを提供できる基盤システムを作ることにあります。
""",
    "references": CONTENT["en"]["references"],
}

GLOSSARY = [
    ("Good Tomorrow", "Protocol and native ecosystem token name; keep untranslated."),
    ("BNB Smart Chain", "Target blockchain for the protocol and token deployment."),
    ("DeFi", "Decentralized finance; normalize source typo `DeFI` to `DeFi`."),
    ("RWA", "Real-world assets; assets whose value depends on offchain legal and cash-flow structures."),
    ("APY", "Annual percentage yield; do not use as a synonym for realized return."),
    ("TVL", "Total value locked; used when discussing scale effects."),
    ("USDC", "Stablecoin used in the initial Good Tomorrow/USDC liquidity market."),
    ("Risk reserve", "Protocol reserve funded from actual income to absorb losses and external risks."),
    ("Proof of reserves", "Mechanism for showing protocol assets and reserves."),
    ("Proof of capital utilization", "Mechanism for showing where user assets are allocated."),
    ("Proof of yield", "Mechanism for showing realized income and its sources."),
]

CONTENT_MAP_ROWS = [
    ("README.md", "Title, subtitle, abstract thesis", "Protocol positioning and language entry point"),
    ("overview/introduction.md", "Abstract; 1. Introduction; 2. Problem Statement", "Market background, fragmentation, opaque yield, capacity mismatch"),
    ("protocol/architecture.md", "3. Protocol Overview; 4. System Architecture", "Operating flow and five core modules"),
    ("protocol/liquidity-infrastructure.md", "5. Liquidity Infrastructure", "Liquidity as unified managed capital resource"),
    ("protocol/capital-management.md", "6. Capital Management and Asset Allocation", "Strategy capacity, risk-adjusted allocation, TVL scale effects"),
    ("protocol/yield-profit-distribution.md", "7. Yield Generation and Profit Distribution", "Realized income principle and distributable profit"),
    ("networks/stablecoin-payments-rwa.md", "8. Stablecoin Liquidity Network; 9. Payments and Settlement; 10. RWA", "Network expansion into stablecoins, payments, and RWA"),
    ("risk/transparency-and-solvency.md", "11. Risk Management; 12. Onchain Transparency", "Solvency controls, risk reserves, financial verification"),
    ("governance/token-and-governance.md", "13. Token Supply; 14. Governance", "Token supply table, lockup, governance boundaries"),
    ("roadmap/development-roadmap.md", "15. Roadmap", "Seven development phases"),
    ("roadmap/long-term-vision.md", "16. Long-Term Vision", "Final infrastructure thesis"),
    ("reference/references.md", "References", "Source references preserved"),
]


def page_title(lang, key):
    for path, k, titles in PAGES:
        if k == key:
            return titles[lang]
    raise KeyError(key)


def common_project_content(lang, key):
    if key == "glossary":
        title = page_title(lang, key)
        rows = "\n".join(f"| {term} | {definition} |" for term, definition in GLOSSARY)
        return f"# {title}\n\n| Term | Usage |\n| --- | --- |\n{rows}\n"
    if key == "content_map":
        title = page_title(lang, key)
        rows = "\n".join(f"| `{path}` | {source} | {purpose} |" for path, source, purpose in CONTENT_MAP_ROWS)
        return f"# {title}\n\nThis map traces each GitBook page back to the source whitepaper.\n\n| GitBook Page | Source Coverage | Documentation Purpose |\n| --- | --- | --- |\n{rows}\n"
    if key == "translation_guide":
        title = page_title(lang, key)
        return f"""# {title}

## Language Order

1. English
2. 简体中文
3. 한국어
4. 日本語

## Terminology Rules

- Keep **Good Tomorrow**, **BNB Smart Chain**, **USDC**, **DeFi**, **RWA**, **APY**, and **TVL** unchanged across languages.
- Normalize the source typo `DeFI` to `DeFi` in all publishable documentation.
- Translate concepts rather than word-for-word sentence order when needed, but preserve numbers, percentages, lockup terms, phase order, and protocol constraints.
- Do not convert the protocol into a fixed-yield product in translation. Use wording that clearly distinguishes realized financial income from nominal APY and token incentives.
- Preserve risk caveats for RWA, strategy capacity, liquidity reserves, and solvency.

## Style

Use a professional Web3 protocol documentation tone: precise, neutral, and implementation-aware. Avoid promotional claims that are not present in the source whitepaper.
"""
    if key == "qa_report":
        title = page_title(lang, key)
        return f"""# {title}

Generated QA status is maintained in `qa-report.json` at the repository root after running:

```bash
python3 tools/validate_docs.py
```

The latest human-readable QA summary is mirrored in the English QA report and can be localized if the report format is expanded later.
"""
    raise KeyError(key)


def content_for(lang, key):
    if key in CONTENT[lang]:
        return CONTENT[lang][key].rstrip() + "\n"
    return common_project_content(lang, key).rstrip() + "\n"


def summary_for(lang):
    title = "Summary"
    labels = {
        "overview": {"en": "Overview", "zh": "概览", "ko": "개요", "ja": "概要"}[lang],
        "protocol": {"en": "Protocol Design", "zh": "协议设计", "ko": "프로토콜 설계", "ja": "プロトコル設計"}[lang],
        "networks": {"en": "Financial Networks", "zh": "金融网络", "ko": "금융 네트워크", "ja": "金融ネットワーク"}[lang],
        "governance": {"en": "Risk, Token, and Governance", "zh": "风险、代币与治理", "ko": "리스크, 토큰, 거버넌스", "ja": "リスク、トークン、ガバナンス"}[lang],
        "roadmap": {"en": "Roadmap and Vision", "zh": "路线图与愿景", "ko": "로드맵과 비전", "ja": "ロードマップとビジョン"}[lang],
        "reference": {"en": "Reference", "zh": "参考", "ko": "참고", "ja": "リファレンス"}[lang],
        "project": {"en": "Project QA", "zh": "项目 QA", "ko": "프로젝트 QA", "ja": "プロジェクトQA"}[lang],
    }
    links = {key: (path, titles[lang]) for path, key, titles in PAGES}
    return f"""# {title}

* [{links['home'][1]}]({links['home'][0]})

## {labels['overview']}

* [{links['overview'][1]}]({links['overview'][0]})

## {labels['protocol']}

* [{links['architecture'][1]}]({links['architecture'][0]})
* [{links['liquidity'][1]}]({links['liquidity'][0]})
* [{links['capital'][1]}]({links['capital'][0]})
* [{links['yield'][1]}]({links['yield'][0]})

## {labels['networks']}

* [{links['networks'][1]}]({links['networks'][0]})

## {labels['governance']}

* [{links['risk'][1]}]({links['risk'][0]})
* [{links['token'][1]}]({links['token'][0]})

## {labels['roadmap']}

* [{links['roadmap'][1]}]({links['roadmap'][0]})
* [{links['vision'][1]}]({links['vision'][0]})

## {labels['reference']}

* [{links['references'][1]}]({links['references'][0]})

## {labels['project']}

* [{links['glossary'][1]}]({links['glossary'][0]})
* [{links['content_map'][1]}]({links['content_map'][0]})
* [{links['translation_guide'][1]}]({links['translation_guide'][0]})
* [{links['qa_report'][1]}]({links['qa_report'][0]})
"""


def write(path, text):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text.rstrip() + "\n", encoding="utf-8")


def main():
    write(ROOT / ".gitbook.yaml", "root: ./docs/en\n\nstructure:\n  readme: README.md\n  summary: SUMMARY.md\n")
    write(ROOT / "LANGS.md", "# Languages\n\n* [English](docs/en/)\n* [简体中文](docs/zh/)\n* [한국어](docs/ko/)\n* [日本語](docs/ja/)\n")
    write(DOCS / "LANGS.md", "# Languages\n\n* [English](en/)\n* [简体中文](zh/)\n* [한국어](ko/)\n* [日本語](ja/)\n")
    write(ROOT / "README.md", """# Good Tomorrow GitBook Documentation

This repository contains production-ready multilingual GitBook documentation for the Good Tomorrow whitepaper.

English is configured as the default GitBook space through `.gitbook.yaml`. The localized spaces are available under `docs/zh`, `docs/ko`, and `docs/ja`, with matching navigation and page hierarchy.

## Local QA

```bash
python3 tools/validate_docs.py
```

## GitBook Setup

For the default English space, connect GitBook Git Sync to the repository root. For language variants, create separate GitBook spaces and set their project directories to `docs/zh`, `docs/ko`, and `docs/ja` respectively, then link those spaces as site variants in GitBook.
""")
    for lang, name, gitbook_title in LANGS:
        lang_dir = DOCS / lang
        write(lang_dir / ".gitbook.yaml", "root: ./\n\nstructure:\n  readme: README.md\n  summary: SUMMARY.md\n")
        write(lang_dir / "SUMMARY.md", summary_for(lang))
        for rel, key, titles in PAGES:
            frontmatter = f"---\ndescription: {gitbook_title}\n---\n\n"
            write(lang_dir / rel, frontmatter + content_for(lang, key))

    print("Built multilingual GitBook docs.")


if __name__ == "__main__":
    main()

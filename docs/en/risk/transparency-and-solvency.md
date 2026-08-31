---
description: Good Tomorrow Documentation
---

# Risk, Solvency, and Transparency

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

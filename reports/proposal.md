# Proposal: Liquidity-Conditioned Extreme Hedge Errors Between Near-Substitute ETFs

## Motivation

ETF market makers rely on tight relationships between near-substitute ETFs. Even if two ETFs track the same benchmark on average, extreme short-horizon divergences can matter for quoting, hedging, and inventory risk.

## Research Question

Do near-substitute ETFs experience extreme intraday hedge-error events during liquidity stress, and are these events underestimated by rolling beta/correlation models?

## Data

Initial dataset:

- WRDS TAQ quote and trade data
- SPY, IVV, VOO
- QQQ, QQQM

Initial frequency:

- 5-minute bars built from quote midpoints

## Method

1. Construct quote-midpoint returns.
2. Estimate rolling hedge ratios.
3. Compute hedge errors.
4. Classify liquidity-stress regimes using relative spreads, volume, realized volatility, and open/close effects.
5. Compare normal and stress regimes.
6. Estimate historical VaR/ES and exploratory EVT/POT tail measures.

## Expected Contribution

Prior work studies ETF pricing, arbitrage, hedging, and tail risk. This project reframes the problem as an intraday market-making hedge-risk problem by studying whether extreme hedge errors between ETF hedge instruments are state-dependent on liquidity stress.

## Limitations

- Initial version uses ETF-to-ETF pairs, not futures.
- TAQ cleaning choices must be documented carefully.
- EVT estimates are fragile and require validation.

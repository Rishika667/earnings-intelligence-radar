# Earnings Intelligence Radar — Decision Log

This file records important project decisions and the reasoning behind them.

---

## Decision 001 — Project Name

### Decision

The project is named:

Earnings Intelligence Radar

### Reason

The project is intended to function as an earnings-focused financial intelligence product rather than a generic forecasting notebook.

---

## Decision 002 — Separate Project from Financial Intelligence Radar

### Decision

Earnings Intelligence Radar will remain a separate project from Financial Intelligence Radar.

### Reason

Financial Intelligence Radar focuses primarily on monitoring, interpreting, and organizing financial intelligence.

Earnings Intelligence Radar focuses on predictive financial research, earnings nowcasting, alternative-data testing, probability estimation, and historical validation.

Keeping them separate demonstrates two distinct capabilities.

---

## Decision 003 — Free/Public Data

### Decision

The core project must be buildable using free and publicly available data.

### Reason

The objective is to demonstrate methodology and research capability without requiring expensive proprietary datasets.

Potential proprietary alternatives may be discussed for context but must not be required for the core system.

---

## Decision 004 — Near-Real-Time Rather Than True Real-Time

### Decision

The product will be described as near-real-time.

### Reason

Public datasets have different publication frequencies and delays.

Claiming true real-time intelligence would be misleading when the underlying data sources do not update continuously.

---

## Decision 005 — Probability Outputs Must Be Calibrated

### Decision

The platform should provide probabilities only when they can be supported and calibrated by historical evidence.

### Reason

A probability such as "72% chance of beat" should represent an empirically evaluated model output rather than an arbitrary confidence number.

---

## Decision 006 — Prediction Range Rather Than Point Estimate Only

### Decision

The system should provide prediction ranges or distributions in addition to point forecasts where statistically justified.

### Reason

Earnings outcomes contain uncertainty. A single number can create false precision.

---

## Decision 007 — Point-in-Time Methodology

### Decision

Historical predictions must use information that would actually have been available at the prediction date.

### Reason

Using later revisions or post-earnings information would introduce look-ahead bias and make historical performance misleading.

---

## Decision 008 — Walk-Forward Validation

### Decision

Chronological walk-forward validation will be preferred to random train/test splitting for the forecasting problem.

### Reason

Earnings forecasting is a time-series problem. The validation methodology should respect the information sequence.

---

## Decision 009 — Negative Findings Are Valid

### Decision

The project will report weak or failed signals honestly.

### Reason

The purpose is to determine whether alternative data provide genuine incremental information, not to manufacture impressive results.

---

## Decision 010 — No Unsupported Investment Recommendations

### Decision

The platform will focus on earnings intelligence and forecast signals rather than unsupported BUY/SELL recommendations.

### Reason

The project's objective is financial research and intelligence rather than presenting itself as an investment-advice system.

---

## Decision 011 — One Consistent LLM

### Decision

One LLM model will be used throughout the Genspark development workflow.

### Reason

Maintaining one consistent model avoids changing development behavior and reduces unnecessary context transfer between models.

---

## Decision 012 — Build in Stages

### Decision

The project will be developed through staged implementation rather than one large generation request.

### Reason

Staged development improves control, reduces unnecessary AI context usage, makes debugging easier, and creates recoverable checkpoints.

---

## Decision 013 — GitHub as External Project Memory

### Decision

GitHub project-control files will act as persistent external project memory.

### Reason

If an AI session ends, credits run out, or context is lost, the project should be recoverable from documented state rather than relying on conversational memory.

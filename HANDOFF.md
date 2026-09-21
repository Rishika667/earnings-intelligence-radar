# Earnings Intelligence Radar — AI Handoff

This file provides the instructions required for another AI session to continue the project without losing project context.

---

# READ FIRST

Before making any changes to the project, read these files in this order:

1. PROJECT_SPEC.md
2. PROJECT_STATE.md
3. DECISIONS.md
4. BUILD_LOG.md
5. HANDOFF.md

Do not begin implementation until these files have been read.

---

# PROJECT

Name:

Earnings Intelligence Radar

Purpose:

Build a near-real-time financial intelligence platform that uses free public financial, economic, industry, and alternative-data sources to estimate upcoming company earnings performance.

---

# CURRENT STATUS

Stage:

Stage 0 — Project Setup

Repository:

earnings-intelligence-radar

Current version:

v0.1.0

---

# COMPLETED

- Project concept finalized
- Project separated from Financial Intelligence Radar
- Free/public data requirement established
- Near-real-time requirement established
- Revenue nowcasting requirement established
- Prediction range requirement established
- Probability requirement established
- Beat / meet / miss framework established
- Driver-analysis requirement established
- Point-in-time requirement established
- Historical validation requirement established
- Data freshness requirement established
- Data provenance requirement established
- Model limitation requirement established
- GitHub repository created
- PROJECT_SPEC.md created
- PROJECT_STATE.md created
- BUILD_LOG.md created
- DECISIONS.md created
- HANDOFF.md created

---

# NEXT TASK

After completing the project-control system:

Begin:

Stage 1 — Architecture + Project Scaffold

The architecture stage should define:

- System architecture
- Data architecture
- Module structure
- Data schemas
- Configuration structure
- Forecasting architecture
- Validation architecture
- Dashboard architecture
- Project directory structure

The architecture should be practical and implementation-ready.

---

# NON-NEGOTIABLE CONSTRAINTS

Do not:

- Introduce paid data as a core requirement
- Introduce unnecessary complexity
- Use future information in historical forecasts
- Use random train/test splitting as the primary validation method
- Invent probability values
- Hide negative research results
- Claim true real-time coverage when sources are delayed
- Build unsupported BUY/SELL recommendations
- Rewrite completed modules without a documented reason
- Change established data schemas without documenting the change
- Replace working components unnecessarily

---

# DEVELOPMENT PRINCIPLE

Build the smallest credible working version first.

Then expand functionality only when the core system works.

Do not attempt to build every advanced feature simultaneously.

---

# EXPECTED DEVELOPMENT STAGES

Stage 1 — Architecture + Project Scaffold

Stage 2 — Data Foundation

Stage 3 — Forecasting Engine

Stage 4 — Uncertainty Engine

Stage 5 — Research Intelligence

Stage 6 — Monitoring and Trust Layer

Stage 7 — Productization

---

# WHEN A STAGE IS COMPLETED

The AI must:

1. Run appropriate tests.
2. Verify that the implementation works.
3. Update PROJECT_STATE.md.
4. Update BUILD_LOG.md.
5. Update DECISIONS.md if a major decision was made.
6. Update this HANDOFF.md.
7. Create a Git commit/checkpoint.
8. Clearly state the next exact task.

---

# IF CONTEXT OR CREDITS ARE LOST

Do not restart the project.

Instead:

1. Open the GitHub repository.
2. Read PROJECT_SPEC.md.
3. Read PROJECT_STATE.md.
4. Read DECISIONS.md.
5. Read BUILD_LOG.md.
6. Read HANDOFF.md.
7. Identify the current stage.
8. Identify the "Next Exact Action" in PROJECT_STATE.md.
9. Continue from that point.

---

# AI BEHAVIOR

Act as a technical implementation partner.

Do not redesign the entire project unnecessarily.

Do not make major architectural decisions silently.

When a major decision is required:

1. Identify the decision.
2. Explain the relevant trade-off.
3. Record the decision in DECISIONS.md.
4. Continue implementation only after the decision is established.

Keep implementation focused on the current task.

Do not modify unrelated parts of the project.

---

# FINAL PRODUCT GOAL

The completed system should allow a user to:

Company
→ Current available data
→ Earnings nowcast
→ Prediction range
→ Beat / Meet / Miss probability
→ Driver analysis
→ Forecast evolution
→ Historical validation
→ Alternative-data value analysis
→ Data freshness
→ Data provenance
→ Limitations

The final product should be presented as a serious financial research and intelligence platform.

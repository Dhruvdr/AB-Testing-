# Marketing Campaign Optimization: A/B Testing & Statistical Audit 

## 📌 Project Overview
This project evaluates the performance of two distinct digital marketing bidding strategies: **Campaign A (Control)** and **Campaign B (Test)**. 

As a Business Analyst, my goal was to move beyond "surface-level" metrics (like total clicks) and conduct a rigorous statistical audit. This analysis identifies which campaign truly drives **Return on Ad Spend (ROAS)** and **Conversion Efficiency** while ensuring the data integrity of the experiment itself.

## 🛠️ Tech Stack & Methodology
- **Python:** Pandas, NumPy (Data Manipulation)
- **Visualization:** Seaborn, Matplotlib (Exploratory Data Analysis)
- **Statistical Framework:**
    - **Power Analysis:** Validating sample size adequacy.
    - **Chi-Square Test:** Detecting Sample Ratio Mismatch (SRM).
    - **Two-Proportion Z-Test:** Testing for Statistical Significance.
    - **Pearson Correlation:** Analyzing metric relationships (CTR vs. Purchase).

---

## 🛡️ The "Data Integrity" Audit
Before analyzing performance, I implemented a "Guardrail Check" to ensure the experiment was scientifically sound.

* **Sample Power:** Confirmed the experiment was "Overpowered" with **340k+ total interactions**, ensuring high sensitivity to even small performance lifts.
* **SRM Detection (Critical Catch):** A Chi-Square test revealed a severe **Sample Ratio Mismatch (p < 0.01)**. Traffic was split unevenly (159k vs 180k), suggesting a bias in the randomization engine.
* **Mitigation:** To ensure a "fair fight," I performed **Proportional Downsampling** to equalize group sizes before running the final hypothesis tests.

---

## 🔍 Key Business Questions & Insights

### Q1: Which campaign has the highest conversion efficiency?
* **Result:** **Campaign A (Control)**.
* **Finding:** Despite having less raw traffic, Campaign A outperformed B in conversion rate.
* **Stats:** A **Z-statistic of 11.56 (p=0.0000)** confirmed a **-12.06% Relative Lift** for Campaign B, meaning the new strategy actually reduced efficiency.

### Q2: Which campaign is more cost-effective (ROAS)?
* **Result:** **Campaign A**.
* **Metric:** Campaign A generated **$11.42 per $1 spent**, while Campaign B generated **$10.17**.
* **Impact:** Campaign A is significantly more efficient at turning marketing spend into revenue.

### Q3: Does the number of impressions correlate with purchases?
* **Finding:** **Almost Zero Correlation** (A: -0.02, B: 0.10).
* **Insight:** "Branding" (impressions) is not driving direct sales in this dataset. Higher ad volume does not automatically equate to higher revenue.

### Q4: Does a higher CTR lead to a higher Purchase Rate?
* **Finding:** No; a significant **Negative Correlation** was detected (A: -0.62, B: -0.35).
* **Strategic Insight:** This "Inverse Relationship" suggests that the ads may be "clickbaity"—attracting high curiosity but low buyer intent. The ads are successful at getting clicks, but those users "leak" out of the funnel at the landing page.

---

## 🚀 Final Strategic Recommendation
**Action: Scale Campaign A; Terminate/Rework Campaign B.**

1. **Prioritize ROI:** Implement Campaign A as the default bidding strategy to maximize the $11.42 ROAS.
2. **Fix the "Leaky Funnel":** The negative correlation between CTR and Purchase Rate indicates a mismatch between the **Ad Creative** and the **Landing Page**. I recommend a UX audit of the landing page to better align messaging with user expectations.
3. **Investigate Experiment Logic:** The SRM failure ($p=0.00$) suggests the technical team needs to investigate the randomization logic to ensure future A/B tests aren't biased.

---

## 📂 Project Structure
```text
├── data/
│   ├── Control_group.csv  # Campaign A Data
│   └── Test_group.csv     # Campaign B Data
├── main.py                # Full Python Workflow (Audit, Stats, Visuals)
├── Output/                # Saved charts (Z-Dist, ROAS, Correlations)
└── README.md              # Executive Summary

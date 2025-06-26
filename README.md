# AB-Testing-
 This project analyzes the performance of two marketing campaigns—** Control Campaign ** and **Test Campaign **—using A/B testing methodologies. The goal is to determine which campaign drives better user engagement and conversion, and to provide actionable recommendations based on data-driven insights.
 The analysis was conducted using Python with a focus on practical business questions often faced by Product and Marketing Analysts.

---

##  Project Objectives

### Objective:
•  Determine which of the two marketing campaigns (Control Campaign or Test Campaign) leads to better conversion rates, more cost-effective advertising, and higher engagement.

### Hypothesis:
•	Null Hypothesis (H0): There is no difference between the performance of Control Campaign and Test Campaign in terms of conversion rates and cost-effectiveness.
•	Alternative Hypothesis (H1): Test Campaign performs better than Control Campaign in terms of conversion rates, engagement, and cost-effectiveness.

### Key Metrics:
The key metrics to evaluate the campaigns' performance will include:
•	Spend (how much money is spend on Ads),
• Impressions (how many times the campaign ad was shown),
•	Website Clicks (the number of users who clicked on the ad),
•	Searches (users searching for the product after seeing the ad),
•	View Content (users who viewed a product or page),
•	Add to Cart (users who added a product to their cart),
•	Purchases (users who completed a purchase).

This project answers the following four key business questions:
1. **Which campaign (A or B) has the highest conversion rate?**
2. **What is the return on ad spend (ROAS) for each campaign, and which one is more cost-effective?**
3. **Does the number of impressions correlate with the number of purchases for each campaign?**
4. **How does the click-through rate (CTR) of each campaign affect the likelihood of users making a purchase?**

---

## Experiment Design
Primary Key Metrics:
 •  Conversion Rate (CR): Number of purchases / Number of impressions or clicks.
	•  Click-Through Rate (CTR): Number of website clicks / Number of impressions.
 •  Cost Per Purchase (CPP): Total ad spend / Number of purchases.
	•  Return on Ad Spend (ROAS): Revenue generated / Total ad spend.
Estimated Sample Size (3177233)
Test duration (1 month)

---

##  Dataset

The dataset contains user-level interaction data from both campaigns, including:
- `campaign_group` (Control or Test)
- `Date`;
- Spend [USD];
- Impressions;
- Reach;
- Website Clicks;
- Searches;
- View Content;
- Add to Cart;
- Purchase

---

##  Key Insights

- **Average Purchase Conversion Rate:**  
  - Campaign A: 11.48%  
  - Campaign B: 9.23%
- **Conversion Rate**
  - Campaign A: 0.0983 
  - Campaign B: 0.0864
- **Statistical Significance:**  
  Z-statistic: 11.8387
  P-value: 0.0000
  There is a statistically significant difference in conversion rates between Campaign A and Campaign B.
  
- Campaign A generates $11.04 in revenue for every $1 spent.
  Campaign B generates $10.17 in revenue per $1 spent.
  Therefore, Campaign A is more cost-effective.

- Campaign A - Correlation bw Impression and Purchases: -0.02
  Campaign B - Correlation bw Impression and Purchases: 0.10
-"We analyzed the relationship between the number of impressions and number of purchases for Campaign A and B. Campaign A showed a negative correlation (r = -0.02), suggesting impressions does not influence purchases. Campaign B had a low correlation (r = 0.10), indicating a weaker link between impressions and purchases. This suggests that Campaign B’s creative or targeting may be more effective at converting impressions into sales."

- Campaign A - Correlation between CTR and Purchase Rate: -0.63
  Campaign B - Correlation between CTR and Purchase Rate: -0.35
- "We analyzed the relationship between click-through rate (CTR) and purchase behavior for both campaigns. Campaign A showed a moderate negative correlation (r = -0.63), suggesting that higher CTR is not related to more purchases. Campaign B showed a weak negative correlation (r = -0.35), indicating that although users clicked on the ad, it didn’t strongly predict conversions. This may suggest issues in the post-click experience for both Campaigns."

---

##  Project Structure
<pre>
│
├── data/
│ ├── Control_group.csv # Campaign A (Control)
│ └── Test_group.csv  # Campaign B (Test)
│
├── main.py # Full analysis file
│
├── Output/  # Visualising Output 
│
└── README.md # Project documentation 
 </pre>


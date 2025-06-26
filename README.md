# AB-Testing
 This project analyzes the performance of two marketing campaigns—**Control Campaign** and **Test Campaign**—using A/B testing methodologies. The goal is to determine which campaign drives better user engagement and conversion, and to provide actionable recommendations based on data-driven insights.  
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
• Spend (how much money is spend on Ads),  
• Impressions (how many times the campaign ad was shown),  
• Website Clicks (the number of users who clicked on the ad),  
• Searches (users searching for the product after seeing the ad),  
• View Content (users who viewed a product or page),  
• Add to Cart (users who added a product to their cart),  
• Purchases (users who completed a purchase).  

This project answers the following four key business questions:
1. **Which campaign (A or B) has the highest conversion rate?**
2. **What is the return on ad spend (ROAS) for each campaign, and which one is more cost-effective?**
3. **Does the number of impressions correlate with the number of purchases for each campaign?**
4. **How does the click-through rate (CTR) of each campaign affect the likelihood of users making a purchase?**

---

## Experiment Design  
Campaign A -> Control Campaign  
Campaign B -> Test Campaign  

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
  - Recommendation: Campaign A has a higher conversion rate, indicating that it is more effective in converting visitors into customers.  
- **Statistical Significance:**  
  - Z-statistic: 11.8387  
  - P-value: 0.0000  
  - Recommendation: The results are statistically significant, meaning the observed difference in conversion rates between Campaign A and Campaign B is unlikely due to random chance.  
  
- **Revenue Per Dollar Spent:**  
  - Campaign A: $11.04  
  - Campaign B: $10.17  
  - Recommendation:This suggests that Campaign A is more efficient in generating revenue.  

- **Correlation between Impressions and Purchases:**  
  - Campaign A: -0.02 (almost no correlation)  
  - Campaign B: 0.10 (slight positive correlation)
  - Recommendation: Campaign B shows a slight positive correlation between impressions and purchases, suggesting it may benefit from optimizing targeting to improve this relationship. However, Campaign A's minimal correlation indicates that the number of impressions has little impact on purchases,

- **Correlation between CTR and Purchase Rate:**  
  - Campaign A: -0.63  
  - Campaign B: -0.35  
  - Recommendation: Both campaigns show a negative correlation between CTR and purchase rate, which indicates that higher click-through rates don’t necessarily correlate with more purchases. This could point to issues such as high click volume but poor conversion on the landing page. It may be beneficial to optimize the landing page or call-to-action for both campaigns.

##  Business Recommendation
Based on the A/B test results:  
- **Primary Recommendation:** Implement **Control Campaign** as the new default for maximum efficiency and return on investment.  

- **Further Optimization:** Consider **improving Test Campaign** by targeting high-performing impressions or optimizing the conversion funnel.  

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


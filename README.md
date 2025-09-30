# A/B Testing Statistical Analysis: Stanley vs Poppy Algorithm Comparison

[![Python](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![SQL](https://img.shields.io/badge/SQL-T--SQL-orange.svg)](https://docs.microsoft.com/en-us/sql/)
[![Power BI](https://img.shields.io/badge/Power%20BI-Dashboard-yellow.svg)](https://powerbi.microsoft.com/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

## 🎯 Project Overview

This project demonstrates a complete A/B testing analysis comparing two recommendation algorithms: **Stanley the Re-ranker** vs **Poppy's Personalisation**. What started as a straightforward statistical analysis became a compelling demonstration of how Power BI's interactive filtering and built-in statistical capabilities can dramatically change analytical outcomes.

**🔍 The Discovery**: Initial Python analysis showed strong statistical significance (p < 0.001) and high power. However, by leveraging Power BI's quick filtering capabilities while exploring visualizations and utilizing its native statistical analysis tools, the results told a completely different story - revealing how a single data point on June 28th was influencing the entire analysis.

## 📊 Analysis Journey & Results

### Phase 1: Initial Python Analysis
- **Statistical Significance**: p < 0.001 (Highly Significant)
- **Statistical Power**: 1.000 (Suspiciously Perfect)
- **Effect Size**: -0.048 (Small but significant)
- **Initial Conclusion**: Implement Poppy's Algorithm
- **Red Flag**: Perfect power coefficient seemed unrealistic

### Phase 2: Power BI Interactive Analysis & Statistical Testing
- **Method**: Interactive filtering combined with built-in statistical functions
- **Key Approach**: Quick date filtering while viewing visualizations + comprehensive statistical analysis
- **Discovery**: Using Power BI's filtering, June 28th showed anomalous impact on Group B conversion rates
- **Statistical Validation**: Power BI's two-sided hypothesis testing showed p-value 0.3 when interactively filtering different date ranges
- **Interactive Insight**: Real-time filtering while viewing trends revealed how significantly one date influenced overall statistics

### Phase 3: Python Validation
- **Filtered Analysis**: Excluded June 28th data based on Power BI insights
- **Corrected P-value**: > 0.30 (Not Significant)
- **Final Conclusion**: DO NOT IMPLEMENT
- **Business Impact**: Prevented $50K-200K implementation based on more complete analysis

## 🔧 Technology Stack

- **SQL (T-SQL)**: Advanced CTEs for data deaggregation from aggregated format
- **Python**: Statistical analysis with scipy, statsmodels for hypothesis testing
- **Power BI**: Interactive filtering during visual analysis + native statistical testing capabilities
- **Statistical Methods**: Two-proportion z-test, Cohen's h, power analysis

## 📁 Repository Structure

```
ab-testing-analysis/
├── README.md
├── data/
│   ├── sample_data.csv          # Anonymized sample dataset
│   └── data_dictionary.md       # Column descriptions
├── sql/
│   ├── data_deaggregation.sql   # CTE for expanding aggregated data
│   └── data_exploration.sql     # Initial data quality checks
├── python/
│   ├── statistical_analysis.py  # Original analysis (full dataset)
│   ├── filtered_analysis.py     # Validation script with filtered data
│   ├── requirements.txt         # Python dependencies
│   └── notebooks/
│       └── ab_test_analysis.ipynb
├── powerbi/
│   ├── ab_test_dashboard.pbix   # Interactive dashboard with filtering + stats
│   └── screenshots/             # Dashboard screenshots showing filtering impact
├── documentation/
│   ├── methodology.md           # Detailed experimental design
│   ├── findings_summary.md      # Key insights and recommendations
│   └── lessons_learned.md       # Power of interactive analysis
└── assets/
    └── images/                  # Visualization outputs
```

## 🚀 Quick Start

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/ab-testing-statistical-analysis.git
cd ab-testing-analysis
```

### 2. Install Dependencies
```bash
pip install -r python/requirements.txt
```

### 3. Reproduce the Analysis Journey
```bash
# Step 1: Run original analysis (full dataset)
python python/statistical_analysis.py

# Step 2: Use Power BI file to explore data with interactive filtering
# Open powerbi/ab_test_dashboard.pbix
# Try filtering out different dates while viewing statistical results

# Step 3: Run validation analysis with filtered dataset
python python/filtered_analysis.py
```

## 📈 The Analytical Journey

### 🤔 What Made Me Investigate Further
The initial Python analysis returned a **statistical power of 1.000** - essentially perfect power. While statisticians dream of such power, in real-world data this warranted deeper investigation through interactive exploration.

### 🔍 Power BI's Interactive Statistical Analysis
The game-changer was Power BI's ability to combine **quick filtering with real-time statistical analysis**:

**Interactive Analysis Workflow:**
1. **Visual Exploration**: Viewing daily conversion rate trends
2. **Quick Filtering**: Using Power BI's date filters to exclude specific days
3. **Real-time Statistics**: Watching how statistical results changed with different filters applied
4. **June 28th Discovery**: Filtering out this single date dramatically changed the statistical outcome

**Power BI Statistical Functions Used:**
- **Hypothesis Testing**: Two-sided test with confidence intervals (p-value dynamically updated as filters changed)
- **Statistical Significance**: Built-in p-value calculations (showed p=0.3 with filtered data)
- **Effect Size Analysis**: Conversion rate lift analysis (0.26% difference)
- **Confidence Intervals**: 99% confidence level analysis with upper/lower bounds
- **Power Analysis**: Statistical power calculations that updated with filtering

**Key Power BI Advantage:**
The ability to **filter while viewing statistical results** made it immediately apparent how sensitive the analysis was to the June 28th data point. This interactive capability revealed insights that static Python analysis couldn't easily show.

### ✅ Python Validation
Armed with insights from Power BI's interactive analysis:
- Applied the same date filtering discovered in Power BI
- Reran identical statistical tests on filtered dataset
- P-value shifted from <0.001 to >0.30
- Statistical power normalized to realistic levels
- **Conclusion completely reversed**

## 🔍 Key Technical Insights

### Power BI's Interactive Analysis Advantage
1. **Real-time Filtering**: Instantly see how excluding data points affects statistical outcomes
2. **Visual + Statistical Integration**: Statistics update live as you filter visualizations
3. **Exploratory Flexibility**: Quickly test hypotheses about data sensitivity
4. **Insight Discovery**: Interactive exploration reveals patterns static analysis might miss

### The Value of Interactive Statistical Tools
- **Dynamic Hypothesis Testing**: Filter and immediately see statistical significance change
- **Sensitivity Analysis**: Understand which data points drive your conclusions
- **Visual Validation**: See statistical changes reflected in visual trends simultaneously
- **Rapid Iteration**: Test multiple scenarios in minutes vs. hours of coding

### Why This Approach Matters
1. **Speed of Discovery**: Interactive filtering revealed issues in minutes
2. **Intuitive Exploration**: Visual + stats combination made patterns obvious
3. **Confidence in Findings**: Multiple perspectives validated the conclusion
4. **Reproducible in Python**: Insights discovered interactively, confirmed programmatically

## 📊 Business Impact

### The Value of Interactive Analysis
**By leveraging Power BI's filtering and statistical capabilities:**
- ✅ Quickly identified data sensitivity through interactive exploration
- ✅ Discovered how significantly one date influenced statistical conclusions
- ✅ Used built-in statistical tests to validate findings in real-time
- ✅ Prevented implementation based on incomplete analysis
- ✅ Avoided $50K-200K in unnecessary implementation costs

### Decision Making with Context
**Different analytical approaches provided different insights:**
- Static Python analysis: Strong signal to implement
- Interactive Power BI analysis: Revealed data sensitivity and different conclusion
- Combined approach: Comprehensive understanding of true statistical relationship

## 🎯 Final Recommendations

### Primary Recommendation: **DO NOT IMPLEMENT** Poppy's Algorithm
**Evidence**: Analysis with filtered data shows no significant difference (p > 0.30)

### Process Improvements
1. **Interactive Exploration**: Use filtering during statistical analysis to test data sensitivity
2. **Multi-Tool Validation**: Combine interactive tools with programmatic validation
3. **Real-time Statistics**: Leverage tools that update statistical results as you explore
4. **Data Sensitivity Testing**: Always investigate how individual data points influence conclusions

## 🛠️ Technical Implementation

### SQL Data Processing
- **Challenge**: Original data was aggregated with session_count values
- **Solution**: Recursive CTEs to expand to individual session records
- **Innovation**: Preserved all statistical properties while enabling analysis

### Python Statistical Analysis
- **Initial Script**: Standard two-proportion z-test methodology on full dataset
- **Filtered Script**: Same tests applied to dataset excluding June 28th
- **Key Libraries**: statsmodels, scipy, pandas for robust statistical computing

### Power BI Dashboard
- **Purpose**: Interactive filtering combined with statistical analysis
- **Key Features**: 
  - Quick date/dimension filters that update statistical calculations
  - Daily trend visualizations
  - Built-in hypothesis testing and confidence intervals
  - Real-time statistical significance indicators
- **Critical Role**: Interactive capabilities that revealed data sensitivity

## 📚 Learning Outcomes

This project demonstrates:
- **Interactive Analysis Power**: How quick filtering during statistical analysis reveals insights
- **Tool Synergy**: Combining interactive exploration with programmatic validation
- **Statistical Sensitivity**: Understanding how individual data points influence conclusions
- **Business Judgment**: Making decisions with full context of data behavior
- **Modern Analytics**: Leveraging built-in statistical capabilities in BI tools
- **Rapid Discovery**: Finding insights quickly through interactive exploration

## 💡 The Bottom Line

**Initial Python Analysis**: 3 hours → Strong recommendation to implement  
**Power BI Interactive Exploration**: 2 hours → Different statistical outcome discovered  
**Python Validation**: 1 hour → Confirmed filtered findings  
**Total Investment**: 6 hours of comprehensive analysis

**Value Delivered**: Understanding complete statistical picture through interactive analysis  
**Potential Cost Avoided**: $50K-200K+ in implementation costs

The real insight: Interactive filtering while viewing statistical results revealed data sensitivity that static analysis alone didn't clearly show. Power BI's ability to update statistical calculations as you filter made the impact of the June 28th data immediately apparent.

## 🔗 Connect

<p align="center">
  <a href="https://www.linkedin.com/in/marc-dutton-848115185/">
    <img src="https://img.shields.io/badge/LinkedIn-Marc%20Dutton-0077B5?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn"/>
  </a>
  <a href="mailto:mdut011@gmail.com">
    <img src="https://img.shields.io/badge/Email-mdut011%40gmail.com-D14836?style=for-the-badge&logo=gmail&logoColor=white" alt="Email"/>
  </a>
</p>

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

**Note**: This analysis demonstrates the power of interactive statistical analysis tools. Power BI's ability to combine quick filtering with real-time statistical calculations enabled discovery of data sensitivity that fundamentally changed the analytical conclusion. The combination of interactive exploration and programmatic validation represents modern best practice in data analysis.

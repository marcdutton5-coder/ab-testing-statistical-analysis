# A/B Testing Statistical Analysis: Roger vs Penny Algorithm Comparison

[![Python](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![SQL](https://img.shields.io/badge/SQL-T--SQL-orange.svg)](https://docs.microsoft.com/en-us/sql/)
[![Power BI](https://img.shields.io/badge/Power%20BI-Dashboard-yellow.svg)](https://powerbi.microsoft.com/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

## 🎯 Project Overview

This project demonstrates a complete A/B testing analysis comparing two recommendation algorithms: **Roger the Re-ranker** vs **Penny's Personalisation**. What started as a straightforward statistical analysis became a critical lesson in data validation when unusual results led to deeper investigation.

**🔍 The Investigation Journey**: Initial Python analysis showed suspiciously high statistical power (1.000) and strong significance. Power BI exploratory data analysis revealed the culprit - a critical outlier on June 28th that was skewing results and could have led to a costly business mistake.

## 📊 Analysis Journey & Results

### Phase 1: Initial Python Analysis
- **Statistical Significance**: p < 0.001 (Highly Significant)
- **Statistical Power**: 1.000 (Suspiciously Perfect)
- **Effect Size**: -0.048 (Small but significant)
- **Initial Conclusion**: Implement Penny's Algorithm
- **Red Flag**: Perfect power coefficient seemed unrealistic

### Phase 2: Power BI Investigation
- **Method**: Basic EDA and daily trend analysis
- **Discovery**: June 28th showed anomalous spike in Group B conversion rates
- **Insight**: Visual analysis revealed what statistical tests missed
- **Statistical Functions**: Used Power BI's built-in outlier detection

### Phase 3: Python Validation
- **Outlier Removal**: Excluded June 28th data
- **Corrected P-value**: > 0.30 (Not Significant)
- **Final Conclusion**: DO NOT IMPLEMENT
- **Business Impact**: Prevented $50K-200K implementation mistake

## 🔧 Technology Stack

- **SQL (T-SQL)**: Advanced CTEs for data deaggregation from aggregated format
- **Python**: Statistical analysis with scipy, statsmodels for hypothesis testing
- **Power BI**: Critical EDA, trend analysis, and outlier detection using statistical functions
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
│   ├── statistical_analysis.py  # Original analysis (suspicious results)
│   ├── outlier_analysis.py     # Validation script post-Power BI discovery
│   ├── requirements.txt        # Python dependencies
│   └── notebooks/
│       └── ab_test_analysis.ipynb
├── powerbi/
│   ├── ab_test_dashboard.pbix  # EDA dashboard that revealed outliers
│   └── screenshots/            # Dashboard screenshots showing discovery
├── documentation/
│   ├── methodology.md          # Detailed experimental design
│   ├── findings_summary.md     # Key insights and recommendations
│   └── lessons_learned.md      # Why multi-tool analysis matters
└── assets/
    └── images/                 # Visualization outputs
```

## 🚀 Quick Start

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/ab-testing-statistical-analysis.git
cd ab-testing-statistical-analysis
```

### 2. Install Dependencies
```bash
pip install -r python/requirements.txt
```

### 3. Reproduce the Analysis Journey
```bash
# Step 1: Run original analysis (suspicious results)
python python/statistical_analysis.py

# Step 2: Use Power BI file to explore data visually
# Open powerbi/ab_test_dashboard.pbix

# Step 3: Run validation analysis with outlier detection
python python/outlier_analysis.py
```

## 📈 The Analytical Journey

### 🤔 What Made Me Suspicious
The initial Python analysis returned a **statistical power of 1.000** - essentially perfect power. While statisticians dream of such power, in real-world data this often indicates:
- Sample size calculation issues
- Data quality problems  
- Hidden confounding factors
- **Outliers skewing results**

### 🔍 Power BI Investigation Process
Rather than accept the "too good to be true" results, I used Power BI's statistical functions and EDA capabilities:

1. **Daily Trend Analysis**: Plotted conversion rates by day and group
2. **Statistical Functions**: Applied Power BI's outlier detection algorithms
3. **Visual Inspection**: Identified June 28th as having anomalous Group B performance
4. **Root Cause**: Likely data collection error or external event on that date

### ✅ Python Validation
Armed with insights from Power BI analysis:
- Excluded June 28th data
- Reran identical statistical tests
- P-value shifted from <0.001 to >0.30
- Statistical power normalized to realistic levels
- **Conclusion completely reversed**

## 🔍 Key Technical Insights

### Multi-Tool Analysis Advantage
1. **Python Strength**: Rigorous statistical testing and automation
2. **Power BI Strength**: Interactive EDA and visual outlier detection
3. **Combined Power**: Statistical rigor + visual intuition = robust findings
4. **Lesson Learned**: No single tool tells the complete story

### Red Flags That Led to Investigation
- **Perfect Statistical Power**: Real data rarely yields 1.000 power
- **Small Effect Size with High Significance**: Suggested sample size artifacts
- **Business Context**: Results seemed too decisive for algorithm comparison

### Data Quality Validation Process
1. **Always Question Perfect Results**: If it seems too good, investigate deeper
2. **Visual Analysis is Critical**: Charts reveal what statistics can miss  
3. **Multiple Perspectives**: Use different tools to validate findings
4. **Domain Knowledge**: Business context should inform statistical interpretation

## 📊 Business Impact

### The Cost of Not Investigating
**If we had stopped at the initial Python analysis:**
- ✅ Would have recommended implementing Penny's algorithm
- ❌ Implementation costs: $50,000 - $200,000
- ❌ User experience disruption for no benefit
- ❌ Opportunity cost of not pursuing better alternatives

### The Value of Thorough Analysis
**By using Power BI to investigate suspicious results:**
- ✅ Identified critical data quality issue
- ✅ Prevented costly implementation mistake
- ✅ Saved substantial business resources
- ✅ Improved data collection processes for future tests

## 🎯 Final Recommendations

### Primary Recommendation: **DO NOT IMPLEMENT** Penny's Algorithm
**Evidence**: Corrected analysis shows no significant difference (p > 0.30)

### Process Improvements
1. **Multi-Tool Validation**: Never rely on single analysis tool
2. **Suspicious Results Protocol**: Perfect statistics warrant investigation
3. **Visual EDA Standard**: Always include exploratory data analysis
4. **Data Quality Monitoring**: Implement real-time outlier detection

## 🛠️ Technical Implementation

### SQL Data Processing
- **Challenge**: Original data was aggregated with session_count values
- **Solution**: Recursive CTEs to expand to individual session records
- **Innovation**: Preserved all statistical properties while enabling analysis

### Python Statistical Analysis
- **Initial Script**: Standard two-proportion z-test methodology
- **Validation Script**: Enhanced with outlier detection and comparison
- **Key Libraries**: statsmodels, scipy, pandas for robust statistical computing

### Power BI Dashboard
- **Purpose**: Interactive EDA and visual outlier detection
- **Key Features**: Daily trends, statistical functions, anomaly highlighting
- **Critical Role**: Visual analysis that revealed what pure statistics missed

## 📚 Learning Outcomes

This project demonstrates:
- **Statistical Rigor**: Proper hypothesis testing with validation
- **Critical Thinking**: Questioning results that seem too perfect
- **Tool Integration**: Leveraging strengths of multiple analytical platforms
- **Business Judgment**: Connecting technical findings to business decisions
- **Data Quality Awareness**: Understanding how outliers can mislead analysis
- **Risk Management**: Preventing costly decisions through thorough investigation

## 💡 The Bottom Line

**Initial Analysis Time**: 2 hours  
**Power BI Investigation**: 3 hours  
**Python Validation**: 1 hour  
**Total Investment**: 6 hours of thorough analysis

**Potential Cost Avoided**: $50K-200K+ in implementation costs  
**ROI of Thorough Analysis**: 8,300-33,300%

Sometimes the most valuable insight isn't what your data shows - it's recognizing when something doesn't look right and having the tools and curiosity to investigate further.

## 🔗 Connect

- **LinkedIn**: [Your LinkedIn Profile]
- **Portfolio**: [Your Portfolio Website]
- **Email**: your.email@domain.com

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

**Note**: This analysis demonstrates why data scientists need both statistical rigor AND visual intuition. The combination of Python's computational power and Power BI's interactive analysis capabilities enabled a discovery that pure statistical testing missed.

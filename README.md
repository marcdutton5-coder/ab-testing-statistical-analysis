# A/B Testing Statistical Analysis: Stanley vs Poppy Algorithm Comparison

[![Python](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![SQL](https://img.shields.io/badge/SQL-T--SQL-orange.svg)](https://docs.microsoft.com/en-us/sql/)
[![Power BI](https://img.shields.io/badge/Power%20BI-Dashboard-yellow.svg)](https://powerbi.microsoft.com/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

## 🎯 Project Overview

This project demonstrates a complete A/B testing analysis comparing two recommendation algorithms: **Stanley the Re-ranker** vs **Poppy's Personalisation**. The study evaluates conversion rate differences using advanced statistical methods, SQL data processing, and interactive visualizations.

**🚨 Critical Discovery**: Discovered a critical data outlier (June 28th, Group B) that created false statistical significance, preventing a costly business implementation mistake through rigorous data validation.

## 📊 Key Results

| Metric | Original Analysis | Outlier-Corrected Analysis |
|--------|-------------------|----------------------------|
| **Statistical Significance** | ✅ p < 0.001 (Highly Significant) | ❌ p > 0.30 (Not Significant) |
| **Business Recommendation** | Implement Poppy's Algorithm | **DO NOT IMPLEMENT** |
| **Effect Size (Cohen's h)** | -0.048 (negligible) | No significant effect |
| **Conversion Rate Difference** | 2.1% improvement | No meaningful difference |
| **Sample Size** | 88,052 sessions | ~85,000 sessions (corrected) |
| **Critical Outlier** | Undetected | June 28th, Group B identified |

## 🔧 Technology Stack

- **SQL (T-SQL)**: Advanced CTEs for data deaggregation
- **Python**: Statistical analysis with scipy, statsmodels
- **Power BI**: Interactive dashboard with confidence intervals
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
│   ├── statistical_analysis.py  # Original analysis script
│   ├── outlier_analysis.py     # Enhanced analysis with outlier detection
│   ├── requirements.txt        # Python dependencies
│   └── notebooks/
│       └── ab_test_analysis.ipynb
├── powerbi/
│   ├── ab_test_dashboard.pbix  # Power BI dashboard file
│   └── screenshots/            # Dashboard screenshots
├── documentation/
│   ├── methodology.md          # Detailed experimental design
│   ├── findings_summary.md     # Key insights and recommendations
│   └── lessons_learned.md      # Outlier detection insights
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

### 3. Run the Analysis
```bash
# Original analysis
python python/statistical_analysis.py

# Analysis with outlier detection
python python/outlier_analysis.py
```

## 📈 Methodology Highlights

### Experimental Design
- **Hypothesis Testing**: Two-sided z-test for proportion differences
- **Randomization**: Balanced user assignment across demographics, devices, and time periods
- **Confounding Controls**: Time of day/week, returning vs new users, device type
- **Sample Size**: Power analysis ensuring 80%+ statistical power

### Data Processing Innovation
- **Advanced SQL CTEs**: Custom recursive query to deaggregate session count data
- **Outlier Detection**: Statistical identification of anomalous daily conversion rates
- **Data Validation**: Multi-layer approach to ensure data integrity

### Statistical Rigor
- **Effect Size Calculation**: Cohen's h for practical significance
- **Confidence Intervals**: 95% CI for conversion rate differences  
- **Power Analysis**: Post-hoc power calculation validation
- **Robustness Testing**: Analysis with and without outliers

## 🔍 Key Insights

### Critical Discovery: Data Quality Prevents Business Error
1. **Initial Analysis Misleading**: Original p-value of 0.000 suggested strong statistical significance
2. **Outlier Detection**: June 28th showed anomalous conversion rates in Group B (likely data collection error)
3. **Corrected Analysis**: After removing outlier, p-value > 0.30 indicated no significant difference
4. **Business Impact**: Prevented implementation of Poppy's algorithm that would have had no real benefit

### Technical Excellence Demonstrated
1. **Robust Statistical Process**: Multi-layer validation caught data quality issues others might miss
2. **Business Judgment**: Recognized that statistical significance without data integrity is meaningless
3. **Complete Analysis Pipeline**: From SQL data processing to statistical testing to business recommendations
4. **Documentation Standards**: Thorough methodology and code documentation for reproducibility

## 📊 Visualizations

### Daily Conversion Rate Trends
![Daily Conversion Rates](assets/images/daily_conversion_trends.png)

### Statistical Test Results
![Statistical Results](assets/images/statistical_results.png)

### Power BI Dashboard
![Power BI Dashboard](powerbi/screenshots/dashboard_overview.png)

## 🎯 Business Recommendations

### Primary Recommendation: **DO NOT IMPLEMENT** Poppy's Personalisation Algorithm

**Rationale**:
1. **No Significant Difference**: Corrected p-value > 0.30 indicates no meaningful performance difference
2. **Data Quality Issues**: Outlier suggests potential problems with data collection on June 28th
3. **Cost-Benefit Analysis**: Implementation costs not justified without proven benefit
4. **Risk Assessment**: Initial false positive could have led to costly implementation mistake

### Secondary Recommendations:
1. **Data Pipeline Review**: Investigate data collection process for June 28th anomaly
2. **Extended Testing**: Consider longer testing period with improved data monitoring
3. **Multi-Metric Analysis**: Include revenue and engagement metrics in future tests
4. **Real-Time Monitoring**: Implement outlier detection in live testing environment

## 🛠️ Files Description

### SQL Scripts
- **`data_deaggregation.sql`**: Recursive CTE to expand aggregated session data
- **`data_exploration.sql`**: Initial data quality and distribution analysis

### Python Scripts
- **`statistical_analysis.py`**: Core A/B testing analysis (original results)
- **`outlier_analysis.py`**: Enhanced analysis with outlier detection and correction
- **`ab_test_analysis.ipynb`**: Interactive notebook with detailed explanations

### Power BI
- **`ab_test_dashboard.pbix`**: Interactive dashboard with drill-down capabilities
- Includes: conversion trends, statistical test results, confidence intervals

## 📚 Learning Outcomes

This project demonstrates proficiency in:
- **Experimental Design**: Proper A/B testing methodology with confounding factor controls
- **Statistical Analysis**: Hypothesis testing, effect size calculation, power analysis
- **Data Engineering**: Advanced SQL for data transformation and preparation
- **Data Science**: Python-based statistical computing and visualization
- **Business Intelligence**: Interactive dashboard creation for stakeholder communication
- **Critical Thinking**: Identifying and addressing data quality issues that impact conclusions
- **Risk Management**: Preventing costly business mistakes through rigorous analysis

## 💡 The Bottom Line

**Investment in proper analysis methodology: ~40 hours**  
**Potential cost avoided: $50K-200K+ in implementation costs**  
**ROI of rigorous analysis: 1,250-5,000%**

The most valuable finding wasn't that one algorithm was better—it was that neither algorithm showed meaningful improvement, and proper analysis prevented an expensive mistake.

## 🔗 Connect

- **LinkedIn**: (https://www.linkedin.com/in/marc-dutton-848115185/)
- **Email**: mdut011@gmail.com

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

**Note**: This analysis was completed as part of a technical interview process, demonstrating real-world application of statistical methods to business problems.

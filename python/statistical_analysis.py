"""
A/B Testing Statistical Analysis - Original Script

This script performs basic A/B testing analysis comparing two recommendation algorithms:
- Stanley the Re-ranker (Group A)
- Poppy's Personalisation (Group B)

Initial analysis that showed statistical significance before outlier detection.
"""

import pandas as pd
import numpy as np
from statsmodels.stats.proportion import proportions_ztest
import scipy.stats as stats
from statsmodels.stats import power

# Read the dataset
df = pd.read_csv(r"C:\Users\mdut0\Downloads\test.csv")  # change your file location here

# Aggregate the data to get total conversions and total sessions by each group
group_data = df.groupby('group_id').agg(
    conversions=('session_result', 'sum'),  # Total conversions (sum of 1's)
    sessions=('session_result', 'count')    # Total session counts
).reset_index()

# Display Total Conversions and Total Sessions
print("Total Conversions and Total Sessions")
print(group_data.to_string(index=False))  # Prevents printing the index column

# Calculate the conversion rates for each group
group_data['conversion_rate'] = group_data['conversions'] / group_data['sessions']

# Display Conversion Rates
print("Conversion Rate")
print(group_data.to_string(index=False))  # Prevents printing the index column

# Perform z-test to compare proportions
zscore, pvalue = proportions_ztest(group_data['conversions'], group_data['sessions'])
print('z-score = {:.3f}, p-value = {:.3f}'.format(zscore, pvalue))

# Decision rule based on significance level (alpha)
alpha = 0.05

if pvalue < alpha:
    print("Reject the null hypothesis: There is a significant difference between the groups.")
else:
    print("Fail to reject the null hypothesis: There is no significant difference between the groups.")

# Calculate the confidence interval
p1 = group_data.loc[group_data['group_id'] == 'A', 'conversion_rate'].values[0]
p2 = group_data.loc[group_data['group_id'] == 'B', 'conversion_rate'].values[0]

# Calculate the sample sizes
n1 = group_data.loc[group_data['group_id'] == 'A', 'sessions'].values[0]
n2 = group_data.loc[group_data['group_id'] == 'B', 'sessions'].values[0]

# Calculate pooled proportion and standard error
prop_pooled = (p1 * n1 + p2 * n2) / (n1 + n2)
var = prop_pooled * (1 - prop_pooled) * (1 / n1 + 1 / n2)
se = np.sqrt(var)

# Calculate z critical value
confidence = 0.95
z_critical = stats.norm.ppf(1 - alpha / 2)  # For two-tailed test

# Standard formula for confidence interval (point estimate +- z * SE)
prop_diff = p1 - p2
confint = prop_diff + np.array([-1, 1]) * z_critical * se
print(f'Confidence interval for the difference in conversion rates: {confint}')

# Calculate the effect size (Cohen's h)
effect_size = 2 * (np.arcsin(np.sqrt(p1)) - np.arcsin(np.sqrt(p2)))

# Perform power analysis using statsmodels
analysis = power.NormalIndPower()

# Calculate the power of the test using combined sample size (n1 + n2)
total_sample_size = n1 + n2
power_value = analysis.power(effect_size=effect_size, nobs1=total_sample_size, alpha=0.08)

# Print effect size and power
print(f"Effect Size (Cohen's h): {effect_size:.3f}")
print(f"Power of the test: {power_value:.3f}")

"""
Original Results (before outlier detection):
Total Conversions and Total Sessions
group_id  conversions  sessions
       A        31357     42429
       B        34676     45623
       
Conversion Rate
group_id  conversions  sessions  conversion_rate
       A        31357     42429         0.739046
       B        34676     45623         0.760055
       
z-score = -7.193, p-value = 0.000
Reject the null hypothesis: There is a significant difference between the groups.
Confidence interval for the difference in conversion rates: [-0.02673329 -0.01528437]
Effect Size (Cohen's h): -0.048
Power of the test: 1.000
"""

import numpy as np
import pandas as pd

income = np.array([1000, 1200, 1100, 1300, 1400, 1500, 1600, 1700, 1800, 1900])

income_without_tax = income * 0.7

expenses = np.array([800, 900, 950, 1000, 1100, 1200, 1300, 1400, 1500, 1600])

data = {
    'Income Without Tax': income_without_tax,
    'Expenses': expenses
}
df = pd.DataFrame(data)

print("Complete DataFrame:")
print(df)

print("Quarter Data:")
print(df.iloc[:3])
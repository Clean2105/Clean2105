from pathlib import Path

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

np.random.seed(1)
normal = np.random.normal(loc=0.0, scale=1.0, size=1000)

mean = normal.mean()
median = np.median(normal)
variance = normal.var(ddof=1)  

print(f"Mean     = {mean:.3f}")
print(f"Median   = {median:.3f}")
print(f"Variance = {variance:.3f}")

DF = Path("Danh Sách VJOL.xlsx") 

if DF.exists():
    import pandas as pd
    df = pd.read_excel(DF, engine="openpyxl")
    print(df.head())
    df.info()
else:
    print(f"Không tìm thấy file: {DF.resolve()}")

plt.figure(figsize=(8, 5))
sns.histplot(normal, kde=True)
plt.axvline(mean, color="r", label=f"Mean = {mean:.3f}")
plt.axvline(median, color="g", linestyle="--", label=f"Median = {median:.3f}")
plt.title("VJOL")
plt.legend()

plt.savefig("histogram.png", dpi=120)
plt.show()
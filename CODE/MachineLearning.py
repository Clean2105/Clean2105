import matplotlib.pyplot as plt 
import numpy as np 
import pandas as pd 
import sklearn.linear_model

oecd_data = {
    "Country": ["France", "Germany", "Japan", "Korea", "Mexico", "Turkey", "United Kingdom", "United States"],
    "Life satisfaction": [6.5, 7.0, 5.9, 5.8, 6.7, 5.6, 6.7, 7.2]
}
oecd_bli = pd.DataFrame(oecd_data)

gdp_data = {
    "Country": ["France", "Germany", "Japan", "Korea", "Mexico", "Turkey", "United Kingdom", "United States"],
    "GDP per capita": [37675, 40997, 32485, 27195, 9009, 9437, 43773, 55805]
}
gdp_per_capita = pd.DataFrame(gdp_data)

def prepare_country_stats(oecd_bli, gdp_per_capita):
    country_stats = pd.merge(oecd_bli, gdp_per_capita, on="Country")
    return country_stats

country_stats = prepare_country_stats(oecd_bli, gdp_per_capita)

x = np.c_[country_stats["GDP per capita"]]
y = np.c_[country_stats["Life satisfaction"]]

country_stats.plot(kind='scatter', x="GDP per capita", y="Life satisfaction")
plt.title("GDP vs Life Satisfaction")
plt.grid(True)
plt.show()

model = sklearn.linear_model.LinearRegression()
model.fit(x, y)

X_new = [[22587]]
prediction = model.predict(X_new)
print(f"Dự đoán chỉ số hạnh phúc cho GDP {X_new[0][0]}: {prediction[0][0]:.2f}")

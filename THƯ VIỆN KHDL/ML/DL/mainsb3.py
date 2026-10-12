import seaborn as sns 
import matplotlib.pyplot as plt 

tips = sns.load_dataset("tips")
hue_colors = {"Yes": "#808080", "No": "#00FF00"}

sns.scatterplot(x="total_bill", y="tip", data=tips, hue="smoker", palette=hue_colors)
plt.show() 
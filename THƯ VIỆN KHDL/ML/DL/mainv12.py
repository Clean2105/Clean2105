import matplotlib.pyplot as plt 
import numpy as np 

size = [35, 25, 30, 10]
labels = ["Công nghệ", "Dịch vụ", "Sản xuất", "Nông nghiệp"]
colors = ["silver", "gold", "lightgreen", "darkblue"]

plt.pie(size, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140)
plt.title("Biểu đồ doanh thu của một công ty")
plt.legend()
plt.show() 
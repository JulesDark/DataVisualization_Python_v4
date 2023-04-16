import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt

data = pd.read_csv("adidas-quarterly-sales.csv")

plt.figure(figsize=(10, 5))
pd.plotting.autocorrelation_plot(data["Revenue"])
plt.show()




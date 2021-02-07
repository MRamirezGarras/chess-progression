import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("fide_historical.csv")

nombres = df.name.unique()[0:10]

print(nombres)

fig = plt.figure(figsize=(10,6))

for nombre in nombres:
    data = df[df.name == nombre].copy()
    month = data["ranking_date"].str.split("-").str[1]
    month = month.tolist()

    data["month"] = month

    data["month"] = data["month"].astype(int)

    data["mod_age"] = data["age"] + (1/12*data["month"])
    plt.plot(data['mod_age'], data['rating'])

fig.legend(nombres)
plt.xlabel("Age")
plt.ylabel("Rating")
fig.subplots_adjust(right=0.75)
plt.savefig("plots/line_plot.png")
import pandas as pd
import matplotlib.pyplot as plt
import os

df = pd.read_csv("fide_historical.csv")

#Create histograms for each year
for year in df.year.unique():
    data = df[df.year == year]#Select data from a year
    data = data.drop_duplicates(subset = ["name"])#Remove duplicates
    plt.figure()
    my_file = "Histogram year " + str(2000 + year) + ".png"#Create file name
    plt.hist(data.age, bins=30)
    plt.title("Year " + str(2000 + year))
    plt.xlabel("Age")
    plt.ylabel("Number of players")
    plt.savefig(os.path.join("plots/", my_file))

#Create a boxplot with the distribution of all years
plt.figure()
box = df.boxplot("age", by="year")
plt.xlabel("Year")
plt.ylabel("Age")
plt.title("Age distribution by year")
plt.suptitle('')
plt.savefig("plots/boxplot.png")
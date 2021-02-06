#Check the percentage of players that stay in the top-100 list from year to year.
#Use the data in the first list available for each year
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("fide_historical.csv")

percentages = []#List to store the percentages

for year in df.year.unique():
    if year < 17:#We cannot compare last year with the next
        next_year = year + 1
        data = df[df.year == year]
        next_data = df[df.year == next_year]
        date = data.ranking_date.iloc[0]#Select first date
        next_date = next_data.ranking_date.iloc[0]
        players = data.name[data.ranking_date == date]
        next_players = next_data.name[next_data.ranking_date == next_date]
        players = players.tolist()
        next_players = next_players.tolist()
        common = [x for x in players if x in next_players]#Select players from first list that are also in the second
        percentages.append({"year": int(2000 + next_year), "percentage": len(common)})


percentages = pd.DataFrame(percentages, columns= ["year", "percentage"])#Convert to dataframe

plt.figure()
fig = plt.bar(percentages["year"], percentages["percentage"])
plt.ylim((0,100))
plt.title("Percentage of players staying in top-100")
plt.xlabel("Year")
plt.savefig("plots/change_by_year.png")

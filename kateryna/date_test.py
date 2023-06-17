from datetime import datetime
import pandas as pd
from tabulate import tabulate


df = pd.read_csv("/Users/maxwellcorbin/vs_stuff/kateryna/ps4_games.csv")
df["CopiesSold"] = df["Copies sold"].str.replace(" million", "").astype("float") * 1000000
df["ReleaseDate"] = pd.to_datetime(df["Release date[a]"], format="%B %d, %Y")
print(df.ReleaseDate)
df["Copies sold"] = df["Copies sold"].apply(lambda r: float(r.split(" ")[0]) * 1000000)
df["Release date[a]"] = df["Release date[a]"].apply(lambda r: datetime.strptime(r, "%B %d, %Y"))
# print(df["Copies sold"].sum())
# print(df.loc[df["Release date[a]"].idxmax()])
# s = df['Publisher(s)'].value_counts()
# s = df.groupby('Developer(s)').size().sort_values(ascending=False)
# print(tabulate(df.loc[df['Publisher(s)'] == s.index[0]]))
# print(df.loc[:, ['Game', 'Release date[a]']].sort_values(["Release date[a]"], ascending=False))
# print(df.columns)
# d = datetime.strptime("September 7, 2018", r"%B %d, %Y")
# print(d)
df["Year"] = df["Release date[a]"].map(lambda d: d.year)
# print(df.loc[df["Genre(s)"].str.contains("role-playing", case=False)].groupby(
    # "Year")["Copies sold"].sum())
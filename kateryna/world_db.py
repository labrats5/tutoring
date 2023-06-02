import mysql.connector
import matplotlib.pyplot as plt
import pandas as pd
from tabulate import tabulate
import tensorflow as tf

cnx = mysql.connector.connect(user="root",
                              password="happy@456",
                              host="localhost",
                              database="world")

query1 = """--sql
SELECT Continent, SUM(Population) AS Population
FROM country
GROUP BY Continent
HAVING Population > 0
ORDER BY Continent;"""

query2 = """--sql
WITH cte AS (
    SELECT
        CountryCode,
        Name,
        Population,
        RANK() OVER (
            PARTITION BY CountryCode
            ORDER BY Population DESC
        ) as rnk
    FROM city
)
SELECT
    CountryCode,
    Name,
    Population
FROM cte
WHERE rnk = 1
ORDER BY Population DESC
LIMIT 50;"""

df = pd.read_sql_query("SELECT * FROM city LIMIT 50", con=cnx)
df.index += 1
print(tabulate(df, headers='keys', tablefmt='fancy_grid', showindex=False))

# # Matplotlib.
# plt.pie(x=df["Population"], labels=df["Continent"], autopct='%1.1f%%')
# plt.title("Population of Every Continent")
# plt.savefig("kateryna/media/ContintentPop.png")
# plt.show()

# # Markdown File.
# df.to_markdown("kateryna/media/ContintentPop.md")

# # Tabulate.
# print(tabulate(df, headers='keys', tablefmt='fancy_grid', ))

# # Cursor.
cursor = cnx.cursor()
cursor.execute(query2)

for CountryCode, Name, Population in cursor:
    print(f"Country: {CountryCode}, CityName: {Name}, Pop: {Population}")

cursor.close()
cnx.close()
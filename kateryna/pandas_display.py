import pandas as pd
from IPython.display import display
from tabulate import tabulate

# cursor.execute(query2)

dict = {}
dict["Country"] = [1,2,3]
dict["Name"] = [3,4,5]
dict["Population"] = [4,5,6]


df = pd.DataFrame(dict)

print(tabulate(df, headers = 'keys', tablefmt = 'psql'))


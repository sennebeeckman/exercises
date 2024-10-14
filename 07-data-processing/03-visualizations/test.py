import pandas as pd
import numpy as np
import ast
import matplotlib.pyplot as plt
import seaborn as sns

from datetime import datetime
from dateutil.parser import parse

filepath = "./games.csv"
data = pd.read_csv(filepath, index_col=0)

today = datetime.now()
today_str = today.strftime("%b %d, %Y")
data['Release Date'] = data["Release Date"].str.replace("releases on TBD", today_str)
data['Release Date'] = pd.to_datetime(data['Release Date'])

# add columns for Day, Month, and Year based on the Release Date Column data
data['Day'] = data['Release Date'].dt.day
data['Month'] = data['Release Date'].dt.strftime('%b')
data['Year'] = data['Release Date'].dt.year

# add a Week Day column with the day of the week that the game was released on
data['Week day'] = data['Release Date'].dt.day_name()

top_rating = data[['Title','Rating']].sort_values(by = 'Rating', ascending = False)

sns.histplot(data=data["Rating"])
plt.show()
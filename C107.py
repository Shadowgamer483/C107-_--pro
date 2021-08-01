import csv
import pandas as pd
import plotly.express as px

df=pd.read_csv("D:\Daksh\WhiteHatJr\projects whitehat\C106\C107\data.csv")
mean=df.groupby(["st","lvl"],as_index=False)["at"].mean()
fig=px.scatter(mean,x="st",y="lvl",size="at",color="at")
fig.show()








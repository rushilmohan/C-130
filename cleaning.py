import pandas as pd
import csv

df = pd.read_csv("total_stars.csv")
print(df.shape)

del df["Luminosity"]
del df ["Distance.1"]
del df ["Mass.1"]
del df ["Radius.1"]
del df ["Unnamed: 0"]
del df ["Unnamed: 6"]
print(df.shape)

df.to_csv("final.csv")

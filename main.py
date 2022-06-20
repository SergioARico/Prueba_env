import pandas as pd
from datetime import datetime

df = pd.read_csv("Data/airportsLocation.csv")
now = datetime.now()

print(df.head(10))
print(now)
print("## Fin Programa ##")

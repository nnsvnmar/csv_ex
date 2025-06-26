import pandas as pd

df = pd.read_csv("docs/inventory.csv")

stores = df["store_location"].dropna().unique().tolist()

with open("data/lookups/store_location.txt", "w", encoding="utf-8") as f:
    for s in stores:
        f.write(s + "\n")

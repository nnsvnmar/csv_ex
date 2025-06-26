import pandas as pd
import os

# 경로 설정
CSV_PATH   = os.path.join("docs", "inventory.csv")
LOOKUP_DIR = os.path.join("data", "lookups")

os.makedirs(LOOKUP_DIR, exist_ok=True)

df = pd.read_csv(CSV_PATH)

for col, filename in [
    ("product_name",   "product_name.txt"),
    ("store_location", "store_location.txt")
]:
    values = df[col].dropna().unique().tolist()
    with open(os.path.join(LOOKUP_DIR, filename), "w", encoding="utf-8") as f:
        for v in values:
            f.write(f"{v}\n")
    print(f" • {filename}: {len(values)} items")

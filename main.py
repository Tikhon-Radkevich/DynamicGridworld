import pandas as pd

import matplotlib.pyplot as plt
import seaborn as sns


pd.set_option("display.max_columns", None)
pd.set_option("display.width", None)

data_path = "data/predicting-sales-quantity-in-our-dynamic-gridworld"

train = pd.read_csv(f"{data_path}/train.csv")
test = pd.read_csv(f"{data_path}/test.csv")
sup = pd.read_csv(f"{data_path}/supplemental_cities.csv")

train = pd.merge(train, sup, on="city_id")
test = pd.merge(test, sup, on="city_id")

train["type"] = 0
test["type"] = 1
all_data = pd.concat([train, test], axis=0)

# fill price
sns.boxplot(y=all_data["price"].values, x=all_data["ad_level"].values, data=all_data)
all_data["price"].fillna(6.0, inplace=True)

# fill ad_level
sns.boxplot(y=all_data["ad_level"], x=all_data["education_level"])
all_data["ad_level"].fillna(3.0, inplace=True)

# fill population & median_income
all_data["population"] = all_data["population"].fillna(train["population"].mean())
all_data["median_income"] = all_data["median_income"].fillna(train["median_income"].mean())

all_data["no_stores"] = all_data.groupby("city_id").transform("size")

# values=["ad_level", "price", "quantity"]
pivot_df = all_data.pivot(index="city_id", columns="store_id", values=["ad_level"])
pivot_df.fillna(0, inplace=True)

all_data = all_data.merge(pivot_df["ad_level"], on="city_id", how="left")

print(all_data.sort_values("no_stores", ascending=False))

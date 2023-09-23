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
# sns.boxplot(y=all_data["price"].values, x=all_data["ad_level"].values, data=all_data)
all_data["price"].fillna(6.0, inplace=True)

# fill ad_level
# sns.boxplot(y=all_data["ad_level"], x=all_data["education_level"])
all_data["ad_level"].fillna(3.0, inplace=True)

# fill population & median_income
all_data["population"] = all_data["population"].fillna(train["population"].mean())
all_data["median_income"] = all_data["median_income"].fillna(train["median_income"].mean())

all_data["no_stores"] = all_data.groupby("city_id").transform("size")


test = all_data[all_data["type"] == 1]
pivot_df = all_data.pivot(index="city_id", columns="store_id", values=["ad_level", "id"])
pivot_df["ad_level"] = pivot_df["ad_level"].fillna(0)
pivot_df["ad_level"] = pivot_df["ad_level"].astype(bool)

combined_df = pivot_df[["ad_level", "id"]]
print(combined_df.head(10))
exit()
result_df = melted_df[melted_df["ad_level"]]
result_df = result_df[["store_id", "variable"]]
print(pivot_df.head(10))
exit()

for c in ["ad_level", "price", "quantity"]:
    pivot_df = all_data.pivot(index="city_id", columns="store_id", values=[c])
    pivot_df.fillna(0, inplace=True)
    all_data.drop(columns=[c], inplace=True)
    all_data = all_data.merge(pivot_df[c], on="city_id", how="left")



all_data.drop(columns=["store_id"], inplace=True)

all_data.drop_duplicates("city_id", inplace=True)

# print(all_data.sort_values("no_stores", ascending=False).head(10))


train = all_data[all_data["type"] == 0]
train = train.drop(columns=["type"])
train.reset_index(inplace=True, drop=True)
test = all_data[all_data["type"] == 1]
test = test.drop(columns=["type"])
test.reset_index(inplace=True, drop=True)

quantity_columns = [i for i in range(30)]
test.drop(columns=quantity_columns, inplace=True)

y = train[quantity_columns]
X = train.drop(columns=quantity_columns)

test_quantity_mask = list(map(lambda x: f"{x}_x", quantity_columns))
print(test_quantity_mask)

test_quantity_mask = test[test_quantity_mask].astype(bool)

print(test_quantity_mask.head(10))

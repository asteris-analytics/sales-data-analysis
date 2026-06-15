from itertools import groupby

import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv("Europe_Sales.csv")
print(df.head())
print(df.info())
print(df.columns)
print(df.shape)

item_profit=df.groupby("Item Type")["Total Profit"].sum()
item_profit=item_profit.sort_values(ascending=False)
print(item_profit.head(10))
print(len(item_profit))
order_type=df.groupby("Item Type")["Order ID"]

avg_profit=df.groupby("Item Type")["Total Profit"].mean()
avg_profit=avg_profit.sort_values(ascending=False)
print(avg_profit.head(10))

reg_profit=df.groupby("Country")["Total Profit"].sum()
reg_profit=reg_profit.sort_values(ascending=False)
print(reg_profit.head(10))
reg_profit=df.groupby("Country")["Total Profit"].mean()
reg_profit=reg_profit.sort_values(ascending=False)
print(reg_profit.head(10))
top10_profit = reg_profit.head(10)

plt.figure(figsize=(10,6))
top10_profit.plot(kind="bar")

plt.title("Top 10 Countries by Total Profit")
plt.xlabel("Country")
plt.ylabel("Total Profit")

plt.show()
df["Order Date"] = pd.to_datetime(df["Order Date"])

df["Month"] = df["Order Date"].dt.month

rev_month=df.groupby("Month")["Total Revenue"].sum()
rev_month=rev_month.sort_values(ascending=False)
print(rev_month.head(12))
prof_month=df.groupby("Month")["Total Profit"].sum()
prof_month=prof_month.sort_values(ascending=False)
print(prof_month.head(12))
monthly_profit = df.groupby("Month")["Total Profit"].sum()

plt.figure(figsize=(10,6))
monthly_profit.plot(kind="line", marker="o")

plt.title("Total Profit by Month")
plt.xlabel("Month")
plt.ylabel("Profit")

plt.grid(True)

plt.show()
df["Profit Margin"] = (df["Total Profit"] / df["Total Revenue"]) * 100
marg_profit=df.groupby("Item Type")["Profit Margin"].mean()
marg_profit=marg_profit.sort_values(ascending=False)
print(marg_profit.head(10))
item_summary=pd.DataFrame({
    "item_profit": item_profit,
    "max_margin": marg_profit
})
print(item_summary.sort_values("max_margin", ascending=False).head(10))
plt.figure(figsize=(10,6))
plt.scatter(item_summary["max_margin"],item_summary["item_profit"])
plt.xlabel("Profit Margin (%)")
plt.ylabel("Total Profit")
for item in item_summary.index:
    plt.annotate(
        item,
        (
            item_summary.loc[item,"max_margin"],
            item_summary.loc[item, "item_profit"]
        )
    )
plt.show()
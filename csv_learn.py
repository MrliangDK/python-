import pandas as pd

df = pd.read_csv("fruit.csv")

# print(df1 := df.head(5))
df1 = df.head(8)
# print(df1.columns)
df1["Date"] = pd.to_datetime(df1["Date"]).dt.date
# df1["Date"] = pd.to_datetime(df1["Date"])
df1 = df1.sort_values(by="Date", ignore_index=True)
df1.index = df1.index + 1

# print(df1.info())

# print(df1["Date"].dtype)

print(df1.to_string(col_space=2))


print("总销量:{}".format(df1["Sale"].sum()))
sale_peach = df1.loc[df["Fruit"] == "Peach", "Sale"].sum()

print("桃子总销量:{}".format(sale_peach))
df1.to_excel("df1.xlsx", sheet_name="Sheet1", index=False)
print(df1)
# pandas excel

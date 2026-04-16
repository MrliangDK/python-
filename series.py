import pandas as pd

df = pd.read_excel("TOP250.xlsx")
# print(df.head(0))
s1 = df["语言"].str.strip()
# print(s1.index)
# print(s1.values)
# print(s1.head(5))
# print(s1.dtype)
# print(s1.head(5))
# print(s2 := s1.head(5).index.to_list())
num_map = {
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine",
    0: "zero",
}
print(s3 := s1.head(5).values.tolist())
s = pd.Series(s3, index=[1, 2, 3, 4, 5], name="A")
print(s[1])
print(s.index)
new_index = [num_map[n] for n in s.index]
print(new_index)
ss = pd.Series(s3, index=new_index, name="new_A")
print(ss)
sss = pd.Series(num_map, index=[1, 5], name="sss")
print(sss)


# # new_index = [1, 2, 3]
# # name = ["张三", "李四", "王五"]
# # serise1 = pd.Series(name, index=new_index)

# # # print(serise1, serise1.dtype)
# # # print(serise1.index)
# # print(serise1.values)


# data = [["张三", 27], ["李四", 12], ["王五", 13]]
# mydata = pd.DataFrame(data, columns=["姓名", "年龄"])
# mydata.index = mydata.index + 1


# mydata["姓名"] = mydata["姓名"].astype(str)
# mydata["年龄"] = mydata["年龄"].astype(int)

# # print(mydata)


data2 = {"calories": [420, 380, 390], "duration": [50, 40, 45]}
df = pd.DataFrame(data2, index=[1, 2, 3])
print(df.loc[1])
# print(df)
# print(type(df.loc[1]))

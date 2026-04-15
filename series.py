import pandas as pd

# new_index = [1, 2, 3]
# name = ["张三", "李四", "王五"]
# serise1 = pd.Series(name, index=new_index)

# # print(serise1, serise1.dtype)
# # print(serise1.index)
# print(serise1.values)

name = ["张三", "李四", "王五"]
age = [27, 18, 18]
dict1 = dict(zip(name, age))
sheet1 = pd.DataFrame(dict1, columns=["姓名", "年龄"])
sheet1["姓名"] = sheet1["姓名"].astype[str]
sheet1["年龄"] = sheet1["年龄"].astype[int]
print(sheet1)
# dataframe

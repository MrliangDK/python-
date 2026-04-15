import keyword
import sys
import inspect
import math
from math import e
import operator
import random
import os
from functools import reduce
import function
from datetime import datetime
import time
import glob
import pandas as pd

# git add .
# git commit -m "update"
# # git push
# print(pd.__version__)

# mydataset = {"sites": ["Google", "Runoob", "Wiki"], "number": [1, 2, 3]}

# myvar = pd.DataFrame(mydataset)

# print(myvar)


# Series
# 正则表达式
class juxing:
    # wide = 0
    # long = 0

    def __init__(self, l, w):
        self.long = l
        self.wide = w

    def mianji(self):
        # print("面积为{}".format(self.long * self.wide))
        return self.long * self.wide

    def zhouchang(self):
        print("周长为{}".format((self.long + self.wide) * 2))

    def __add__(self, other):
        return self.mianji() + other.mianji()

    def __sub__(self, other):
        return self.mianji() - other.mianji()


x = juxing(5, 4)
y = juxing(8, 2)
# print(x - y)
# x = juxing()
# x.long = 5
# x.wide = 4
# y.mianji()
# x.zhouchang()
# num = int(input("请输入"))
# print("{}的平方根为{}".format(num, math.sqrt(num)))
# print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
# print(datetime.now(), glob.glob("*.py"))


# with open("example.txt", "r") as f:
#     # content = f.readline()
#     for content in f:
#         print(content, end=" ")
# with open("example.txt", "a") as f:
#     f.write("\nmy name is leon\n")
# os.startfile("example.txt")

c = [1, 2, 3, 4]
# print(
#     reduce(lambda a, b: a * b, c),
#     list(map(lambda x: x**2, c)),
#     list(filter(lambda x: x < 3, c)),
# )
c.append(5)
c.extend(c)
c.insert(len(c), 0)
c.remove(5)
c.sort()
del c[0:2]

os.makedirs("new")
os.removedirs("new")
# print(os.getcwd(), os.listdir())
# num = 1


# def func():
#     global num
#     num += 1
#     print(num)


# func()
# print(num)
# print(function.list_1(c), end=" ")
# print("Π后十位{0:.10f}".format(math.pi))


# str = input("请输入:")
# print("你输入的是{}".format(str))
# print(dir(function))

# def print_length(func):
#     def wrapper(a):
#         print("列表长度：", len(a))  # 新加功能
#         func(a)  # 执行原来的遍历

#     return wrapper


# @print_length
# def Traversing_list(a: list):
#     for i in a:
#         print(i)


# Traversing_list(c)


# a = 0
# b = 1
# print(a, b, end=" ")
# while True:
#     m = a + b
#     print(m, end=" ")
#     if m > 900:
#         break
#     a = b
#     b = m


# a = 1
# sum1 = 1
# while(a<100):
#     a = a+1
#     sum1 = sum1+a
# sum2 = sum(range(1,101))
# print(operator.eq(sum1,sum2),end=" ")


# message = "tom smith"
# first_name = "tom"
# last_name = "smith"
# dict1 = {"a": 1, "b": 2}
# dict2 = dict1.copy()

# print(
#     id(message),
#     message.isdigit(),
#     type(message),
#     operator.add(len(first_name), len(last_name)),
#     operator.is_(dict1, dict2) or operator.eq(dict1, dict2),
# )

# full_name = f"{first_name} {last_name}"
# #print(message.upper().lower())
# #print(message.title()) /n /t
# #print(keyword.kwlist)
# str_1 = '123456789'
# print(str_1[0:3])
# str_2 = "I love you"

# print(n:=10)

# # def add(a:int,b:int):
# #     '''两整数求和'''
# #     return a+b

# # # help(add)
# # # print(add.__doc__)
# # print(inspect.getdoc(add))


# # x = bytes(str_2,encoding="UTF-8")
# # print(x)
# #print(str[0:-1])
# #print(str[3:])
# #print(str_1[1:5:2])
# #n = sys.stdout.write(str_1+'\n')
# # print(n)
# # print(type(str_1))
# # bool_1 = isinstance(str_1,(int,str))
# # print(bool_1)
# # a = complex(0,1)
# # b = complex(0,2)
# # print(a*b)
# # print(type(a.imag),type(a.real))
# # Python 字符串是不可变类型
# list_str_1 = list(str_1);list_str_1[0] = 8;
# print(list_str_1)
# print(10 not in list_str_1)
# # print(type(list_str_1[0]))
# list_str_1.reverse()
# str_1 = "".join(str(i) for i in list_str_1)
# print(str_1)

# def reverseword(input1):
#     # input1_word = input1.split(" ")
#     # input1_word = input1_word[-1: :-1]

#     str_3 = input1[::-1]

#     print(str_3)


# reverseword(str_2)

# age = [1,2,3,4]
# name = ["tom","smith"]
# A = (age,name)
# print(A)

# 数字number
# a = 1+2j

# print(int(a.real))

# a = 0.5;b = 0.5;c = a*b
# # print(round(c,1),math.log(e))
# # print(math.ceil(c))
# print(f'{a+b=}')

# print("\a")

# import time

# for i in range(101): # 添加进度条图形和百分比(还未搞懂)
#     bar = '[' + '=' * (i // 2) + ' ' * (50 - i // 2) + ']'
#     print(f"\r{bar} {i:3}%", end='', flush=True)
#     time.sleep(0.05)
# print()

# 猜数字的AI
# 和猜数字一样，不过这次是设计一个能猜数字的AI

# # 功能描述： 用户输入一个单位以内的数字，
# # AI要用最少的次数猜中，并且显示出猜的次数和数字。
import random

guess_answer = 55
left = 0
right = 100
guess_number = random.randint(left, right)
print(guess_number)
i = 1
while True:
    hint = str(input("请给出提示:"))
    if hint == "大了":
        right = guess_number - 1
        i += 1

    elif hint == "小了":
        left = guess_number + 1
        i += 1

    elif hint == "中了":
        print("guessed it")
        print("总共猜了{}次".format(i))
        break
    guess_number = (left + right) // 2
    print("我再猜:", guess_number)

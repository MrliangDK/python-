import random


def list_1(a: list):
    d = {i: a[i] for i in a}
    return d


def guess_game():
    print("welcome to guess_game(1-100 integer)")
    guess_answer = random.randint(0, 100)
    while True:
        try:
            guess_number = int(input("请猜数"))
            if guess_number > guess_answer:
                print("bigger")
            elif guess_number < guess_answer:
                print("smaller")
            elif guess_number == guess_answer:
                print("guessed it")
                break
        except:
            print("please enter a integer")


# print({__name__})

if __name__ == "__main__":
    print("直接运行")
else:
    pass
    # print("作为模块")

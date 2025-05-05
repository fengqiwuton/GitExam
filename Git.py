
import random

def guess_number_game():
    # 生成一个1到100之间的随机数
    target_number = random.randint(1, 100)
    attempts = 0  # 记录尝试次数

    print("欢迎来到猜数字游戏！")
    print("我已经想好了一个1到100之间的数字。")
    print("你能猜到它是什么吗？")

    while True:
        # 获取用户输入
        try:
            guess = int(input("请输入你的猜测（1-100）："))
        except ValueError:
            print("请输入一个有效的整数！")
            continue

        # 增加尝试次数
        attempts += 1

        # 判断猜测结果
        if guess < target_number:
            print("太小了！再试一次。")
        elif guess > target_number:
            print("太大了！再试一次。")
        else:
            print(f"恭喜你！你猜对了！数字是 {target_number}。")
            print(f"你总共尝试了 {attempts} 次。")
            break  # 猜对了，退出循环

    print("游戏结束，感谢参与！")

# 调用函数启动游戏
guess_number_game()
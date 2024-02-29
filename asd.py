import random
random_number = random.randint(1,100)
game = 0

while True:
    user = input("1~100 중 입력하세요: ")
    num=int(user)
    game += 1
    if (random_number > num):
        print("UP")
    elif (random_number < num):
        print("down")
    elif (random_number == num):
        print(f"정답입니다. 시도한 횟수는" + {game} + "번 입니다.")
        break
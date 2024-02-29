import random

random_number = random.randint(1, 3)

count_win=0
count_lose=0
count_draw=0

#1은 가위, 2는 바위, 3은 보.

while True:
    rsp=input("가위(S), 바위(R), 보(P) 중 하나를 선택하세요.")
    if rsp in ("가위", "s", "S"):
        if random_number==1:
            print("당신은 가위를 냈습니다, 컴퓨터도 가위를 냈습니다.")
            print("비겼습니다")
            count_draw+=1
        if random_number==2:
            print("당신은 가위를 냈습니다, 컴퓨터는 바위를 냈습니다.")
            print("졌습니다")
            count_lose+=1
        if random_number==3:
            print("당신은 가위를 냈습니다, 컴퓨터는 보를 냈습니다.")
            print("이겼습니다")
            count_win+=1
        conti=input("다시 하시겠습니까? Y/N")
        if conti in ("Y", "y", "예", "예스"):
            continue
        if conti in ("N", "n", "아니요", "노"):
            print(f'당신은 {count_win}승 {count_draw}무 {count_lose}패입니다')
            break
        else:
            print("유효한 입력이 아닙니다.")
            continue
    if rsp in ("바위", "r", "R"):
        if random_number==1:
            print("당신은 바위를 냈습니다, 컴퓨터는 가위를 냈습니다.")
            print("이겼습니다")
            count_win+=1
        if random_number==2:
            print("당신은 바위를 냈습니다, 컴퓨터도 바위를 냈습니다.")
            print("비겼습니다")
            count_draw+=1
        if random_number==3:
            print("당신은 바위를 냈습니다, 컴퓨터는 보를 냈습니다.")
            print("졌습니다")
            count_lose+=1
        conti=input("다시 하시겠습니까? Y/N")
        if conti in ("Y", "y", "예", "예스"):
            continue
        if conti in ("N", "n", "아니요", "노"):
            print(f'당신은 {count_win}승 {count_draw}무 {count_lose}패입니다')
            break
        else:
            print("유효한 입력이 아닙니다.")
            continue
    if rsp in ("보", "p", "P"):
        if random_number==1:
            print("당신은 보를 냈습니다, 컴퓨터는 가위를 냈습니다.")
            print("졌습니다")
            count_lose+=1
        if random_number==2:
            print("당신은 보를 냈습니다, 컴퓨터는 바위를 냈습니다.")
            print("이겼습니다")
            count_win+=1
        if random_number==3:
            print("당신은 보를 냈습니다, 컴퓨터는 보를 냈습니다.")
            print("비겼습니다")
            count_draw+=1
        conti=input("다시 하시겠습니까? Y/N")
        if conti in ("Y", "y", "예", "예스"):
            continue
        if conti in ("N", "n", "아니요", "노"):
            print(f'당신은 {count_win}승 {count_draw}무 {count_lose}패입니다')
            break
        else:
            print("유효한 입력이 아닙니다.")
            continue
    else:
        print("유효한 입력이 아닙니다")
        continue
    
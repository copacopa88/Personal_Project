import random

count_win=0
count_lose=0
count_draw=0

def game():
     while True: 
        global count_win, count_lose, count_draw        
        user_choice = input("가위, 바위, 보 중 하나를 선택하세요: ")
       
        if user_choice in["가위", "바위", "보"]:
            pass
            
        else:
            print("유효한 입력이 아닙니다.")
            continue
        
        choices = ["가위", "바위", "보"]
        computer_choice=random.choice(choices)
        
        print(f"당신은 {user_choice}를 냈습니다. 컴퓨터는 {computer_choice}를 냈습니다")
        if user_choice == computer_choice:
            count_draw+=1
            print("비겼습니다.")
            break
        elif (user_choice=="가위" and computer_choice == "보") or (user_choice=="바위" and computer_choice == "가위") or (user_choice=="보" and computer_choice == "바위"):
            count_win+=1
            print("이겼습니다! 축하드려요!")
            break
        elif (user_choice=="가위" and computer_choice == "바위") or (user_choice=="바위" and computer_choice == "보") or (user_choice=="보" and computer_choice == "가위"):
            count_lose+=1
            print("당신이 졌습니다.")
            break

game()
while True:
    conti=input("다시 하시겠습니까? Y/N: ")
    if conti in ("y", "Y" "예", "예스"):
        game()
    elif conti in ("n", "N", "아니요", "노"):
        print(f'당신은 {count_win}승 {count_draw}무 {count_lose}패입니다')
        break
    else:
        print("유효한 입력이 아닙니다.")
        continue

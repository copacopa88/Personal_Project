import random

print("공포의 랜덤 돌려돌려 돌림판")

random_number = random.randint(1, 100)
count=0
roop_count=0
count_list=[]

#첫번째 while 루프
def game():
    while True:
        global roop_count
        if roop_count >= 1: #맨 처음에만 최고기록을 보이게 하는 루프 카운터
            min_num = min(count_list)
            print(f'최고 기록은 {min_num}번입니다.')   
        print(random_number) #테스트용 랜덤 숫자 보이기
        num=input("1부터 100까지의 숫자를 입력해주세요")
        dice=int(num)
        global count
        if dice>100 or dice==0:
            count+=1
            roop_count=0
            print("유효한 범위 내의 숫자를 입력하세요") 
        elif random_number<dice: 
            count+=1
            roop_count=0
            print("다운")
        elif random_number>dice:
            count+=1
            roop_count=0
            print("업")
        elif random_number==dice:
            count+=1
            roop_count+=1
            print("축하합니다! 당첨입니다!")
            print(f'{count}번 만에 당첨되셨습니다!')
            count_list.append(count)
            break
        
game() #첫번째 while 함수 실행
    
#두번째 while 루프    
while True:
    Y_N=input("다시 하시겠습니까? (Y/N)")
    if Y_N in ["y", "Y"]:
        count = 0
        random_number = random.randint(1, 100) 
        game()           
    elif Y_N in ["n", "N"]:
        print("게임을 종료합니다")
        break
    else:
        print("Y/N를 입력해 주세요")
        continue   

#완전한 루프 종료
print(count_list) #전체 전적이 잘 list에 저장되었는지 확인


import random

number = random.randrange(1, 20) # 1~20사이의 수를 랜덤으로 갖음
trial = 0 # 도전 횟수 카운트
while trial<5: # 기회는 5번
    trial += 1 # 한 번 입력시 1씩 증가
    my_turn = int(input("1~20 사이의 숫자 입력 : ")) # 사용자의 입력받기
    if my_turn <= 0: # 사용자가 0 이하의 수를 입력했을 때
        my_turn = int(input("다시 입력해주세요. "))
    if my_turn == number: # 사용자가 정답을 맞췄을 때
        print(f"대단해요! {trial}번 만에 맞췄습니다!")
        break # 반복문 탈출
    if my_turn < number: # 입력받은 값이 정답보다 작을 때는 up을 출력
        print("UP")
    if my_turn > number: # 입력받은 값이 정답보다 클 때는 down을 출력
        print("DOWN")
    if my_turn != number and trial == 5: # 마지막 회차 때 정답을 맞추지 못했을 경우
        print("아쉽게도 맞추지 못했습니다. \n다음 기회에")

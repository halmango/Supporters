import random

# 엄청나게 많이 주사위를 던졌을 때 각 숫자마다 나오는 확률이 1/6 인지 확인해보는 코드
number = int(input("몇 번 던지겠습니까?")) #던질 횟수 입력받기
count_1 = 0 #횟수 카운트
count_2 = 0
count_3 = 0
count_4 = 0
count_5 = 0
count_6 = 0
 
for i in range(0, number):
    dice = random.randint(1,6)
    if dice == 1:
        count_1 += 1
    elif dice == 2:
        count_2 += 1
    elif dice == 3:
        count_3 += 1
    elif dice == 4:
        count_4 += 1
    elif dice == 5:
        count_5 += 1
    elif dice == 6:
        count_6 += 1

    a = float(count_1 / number)
    b = float(count_2 / number)
    c = float(count_3 / number)
    d = float(count_4 / number)
    e = float(count_5 / number)
    f = float(count_6 / number)
        
print(f"1은 {count_1} 번 나왔습니다. 1이 나올 확률은 {a} 입니다.")
print(f"2는 {count_2} 번 나왔습니다. 2가 나올 확률은 {b} 입니다.")
print(f"3은 {count_3} 번 나왔습니다. 3이 나올 확률은 {c} 입니다.")
print(f"4는 {count_4} 번 나왔습니다. 4가 나올 확률은 {d} 입니다.")
print(f"5는 {count_5} 번 나왔습니다. 5가 나올 확률은 {e} 입니다.")
print(f"6은 {count_6} 번 나왔습니다. 6이 나올 확률은 {f} 입니다.")

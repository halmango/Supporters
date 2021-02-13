#잘못된 번호 입력시 "잘못된 번호 입니다" 출력
#계산기는 2개의 숫자를 받음
#n 과 m +,-,*,/ 연산한 결과는 x입니다 -> 문자열 포매팅 사용
#나누기 연산 시 분모는 0이 될 수 없다. 0을 입력받았을 때 '연산이 불가합니다' 출력
import sys

print("1. 더하기")
print("2. 빼기")
print("3. 곱하기")
print("4. 나누기")
print("5. 프로그램을 종료합니다.")

operator = int(input("원하는 기능의 번호를 입력하세요: "))

if operator == 5:
    print("프로그램을 종료합니다.")
    sys.exit()
elif operator >= 6:
    print("잘못된 번호입니다.")
    sys.exit()

n = int(input("첫번째 정수를 입력하시오."))
m = int(input("두번째 정수를 입력하시오."))

if operator == 1:
    print(f"{n} 과 {m} 를 더하기 연산한 결과는 {n+m} 입니다.")
elif operator == 2:
    print(f"{n} 과 {m} 를 빼기 연산한 결과는 {n-m} 입니다.")
elif operator == 3:
    print(f"{n} 과 {m} 를 곱하기 연산한 결과는 {n*m} 입니다.")
elif operator == 4:
    try:
        print(f"{n} 과 {m} 를 나누기 연산한 결과는 {n/m} 입니다.")
    except ZeroDivisionError:
        print("연산이 불가합니다.")

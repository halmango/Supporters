list_1 = [1, 22, 333, 4444, 55555]

try:
    number_input = int(input("정수 입력> "))
   print(f"{number_input}번째 요소: {list_1[number_input]}")
except IndexError:
    print("인덱스를 벗어났습니다.")
except ValueError:
    print("정수를 입력해주십시오.")


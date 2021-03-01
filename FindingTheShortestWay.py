# 그림과 같은 길이 있습니다.
# 최단 거리로 집에 갈 수 있는 경우의 수를 구하세요.

# a 는 오른쪽, b 는 위쪽
list_road = ['a','a','a','a','b','b','b','b']
x = len(list_road) # 요소의 개수 카운트
count_a = list_road.count('a') # a개수 카운트
count_b = list_road.count('b') # b개수 카운트
y = 1
A = 1
B = 1
for i in range(1, x+1):
    y *= i
for j in range(1, count_a + 1):
    A *= j
for k in range(1, count_b + 1):
    B *= k
cases = y // (A*B)

print(f"최단 거리로 집에 갈 수 있는 경우의 수는 {cases} 입니다.")
# 리스트에 n 개의 수를 입력한 후, 정렬하여 k번째 수 출력하기
# 첫 줄 한 줄에 n과 k를 입력받는다.
# 리스트에 들어가는 수는 정수이며, 한 줄에 한 칸의 공백으로 구분하여 입력한다.
# k번째 수까지를 한 줄에 한 칸의 공백으로 구분하여 출력한다.

n, k = map(int,input().split())
a = list(map(int,input().split()))
a.sort()
for i in range(n):
  if a[i] <= k :
    print(a[i], end = ' ')




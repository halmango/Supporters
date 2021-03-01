#list_a = []
#for i in range(0,7):
#    a = int(input())
#    list_a.append(a)
#print(sum(list_a))

a = list(map(int, input().split()))
result = sum(a)
print(result)

num = input() #"26"
n = num 
count = 0
while True:
    if len(n) == 1:
        n = "0" + n # "08" = "0" + "8"
    sum = str(int(n[0]) + int(n[1])) # 2 + 6 = "8"
    n = n[-1] + sum[-1] # "6" + "8" = "68"
    count += 1
    if n == num:
        break
print(count)


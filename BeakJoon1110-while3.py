num = int(input()) #26
n = num 
count = 0
while True:
    digits_ten = n // 10 #2
    digits_one = n % 10 #6
    x = digits_ten + digits_one #2+6 = 8
    y = x % 10 #8
    n = digits_one*10 + y #68
    count += 1
    if n == num:
        break
print(count)
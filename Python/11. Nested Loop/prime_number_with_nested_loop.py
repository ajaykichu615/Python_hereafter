lst = [23,2,2,1,44,23,12,1,76,7,3]
for num in lst:
    c = 0
    for i in range (2,num//2+1):
        if num % i == 0:
            c += 1
    if c == 0 and num != 1:
        print(num)



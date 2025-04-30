lower =  int(input("Enter lower limit:"))
upper =  int(input("Enter upper limit:"))
for num in range(lower, upper+1):
    str1 = str(num)
    l = len(str1)
    s = 0
    for i in str1:
        s += int(i)**l
    if s == num:
        print(num)
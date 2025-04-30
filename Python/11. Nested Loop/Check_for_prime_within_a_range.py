lower =  int(input("Enter lower limit:"))
upper =  int(input("Enter upper limit:"))

for num in range(lower,upper+1):
    if num <= 1:
        continue
    c = 0
    for i in range(2, num//2+1):
        if num%i == 0:
            c += 1
    if c == 0:
        print(num)
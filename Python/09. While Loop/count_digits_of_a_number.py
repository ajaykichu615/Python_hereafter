num = int(input("Enter a number: "))
count = 0
temp = abs(num) #take absolute value to handle negative numbers
while temp > 0:
    temp //= 10
    count += 1

#Special case for 0, since it has 1 digit

if num == 0:
    count =1

print(f"Number of digits: {count}")

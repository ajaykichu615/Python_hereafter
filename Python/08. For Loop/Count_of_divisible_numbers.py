"""Find out the count of numbers which is divisible by both 3 and 5 in between numbers 100 to 300."""

count = 0

for i in range(100, 301):
    if i % 3 == 0 and i % 5 == 0:
        count += 1
print(count)
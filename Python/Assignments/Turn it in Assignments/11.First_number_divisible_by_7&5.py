"""Find the first number divisible by 7 and 5 between 1 and 100 using break."""

for i in range(1,101):
    if i % 7 == 0 and i % 5 == 0:
        print(f"{i} is the first number divisible by 7 and 5 b/w 1-100")
        break

else:
    print("There are no numbers divisible by 7 and 5 b/w 1-100")

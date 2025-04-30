"""Create a list of numbers and add 100 to the end of the list using the append() method."""


num = list(map(int, input("Enter numbers separated by spaces: ").split()))


num.append(100)
print(num)
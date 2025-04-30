"""WAP to calculate the sum of only positive non-zero natural numbers by skipping negative numbers and zero using
 continue from the list [1,6,10,-3,7,9,-2] and display the sum using for_else as the looping statement"""

lst = [1,6,10,-3,7,9,-2]
s = 0
for num in lst:
    if num <= 0:
        continue
    s += num
else:
    if s == 0:
        print("No positive non-zero numbers were found in the list.")
    else:
        print(f"Sum of +ve non zero numbers in the list is: {s}")

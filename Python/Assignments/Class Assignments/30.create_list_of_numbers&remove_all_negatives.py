"""Create a list of numbers and remove all negative numbers."""

lst = [12,34,-56,-55,98,-85,92,-22]

for num in lst.copy():
    if num <= 0:
        lst.remove(num)
print(f"Updated list: {lst}")

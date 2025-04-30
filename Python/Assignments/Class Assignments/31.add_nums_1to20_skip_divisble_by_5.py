"""Add numbers from 1 to 20 to a list, but skip numbers divisible by 5 using insert()."""

lst = []
for num in range(1,21):
    if num % 5 != 0:
        lst.insert(0,num)
print(sorted(lst.copy()))

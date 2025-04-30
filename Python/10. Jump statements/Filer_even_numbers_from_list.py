lst = [12,3,3,12,2,-23,23]

for i in lst:
    if i<0 or i%2!=0:
        continue
    print(i)

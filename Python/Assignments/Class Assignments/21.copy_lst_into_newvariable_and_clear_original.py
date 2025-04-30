"""Copy the list into a new variable and then clear the original list using the copy() and clear()"""

lst = [2,44,64,78,26,80]
lst_new = lst.copy()
lst.clear()
print(f"New list: {lst_new}\nOld list: {lst}")
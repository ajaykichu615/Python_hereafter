for i in range(1, 6):        # Outer loop for rows (1 to 5)
    for j in range(6 - i):   # Inner loop to print 'i' values (decreasing count)
        print(i, end=' ')
    print()                  # Move to the next line

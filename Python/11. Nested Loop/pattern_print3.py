for i in range(1, 6):          # Outer loop for rows (1 to 5)
    for j in range(1, i + 1):  # Inner loop to print 'i' values
        print(i, end=' ')
    for k in range(i + 1, 6):  # Inner loop to print incrementing numbers
        print(k, end=' ')
    print()                    # Move to the next line



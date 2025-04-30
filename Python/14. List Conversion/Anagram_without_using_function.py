str1 = list(input("Enter the first string: ").lower().strip())
str2 = list(input("Enter the second string: ").lower().strip())

# Check length first for quick rejection
if len(str1) != len(str2):
    print("Strings are not anagrams")
else:
    # Manual frequency count
    for char in str1:
        if char in str2:
            str2.remove(char)  # Remove matched character
        else:
            print("Strings are not anagrams")
            break
    else:
        print("Strings are anagrams")



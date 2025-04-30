str1 = input("Enter the first string:").lower() # You may also add.strip() along with lower() to remove unwanted spaces in the input string.
str2 = input("Enter the second string:").lower()

if sorted(str1) == sorted(str2):
    print("Strings are an Anagram")
else:
    print("Strings are not an Anagram")
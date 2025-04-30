"""Given the string "Artificial Intelligence and Data Science", perform the following:

1. Split the sentence into words.

2. Find and print the longest word.

Expected Output:

"Intelligence" """

str1 = "Artificial Intelligence and Data Science"
str2 = str1.split()
a = str2[0]
b = str2[1]
c = str2[2]
d = str2[3]
e = str2[4]
longest = max(a,b,c,d,e, key=len)
print("Longest strings is : ", longest)


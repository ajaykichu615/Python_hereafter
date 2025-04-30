"""Given the string "Python is fun", perform the following:

1. Split the sentence into words.
2. Reverse each word.
3. Join them back into a sentence.

Expected Output:

"nohtyP si nuf" """

str1 = "Python is fun"
str2 = str1.split()
a = str2[0]
b = str2[1]
c = str2[2]
str3 = a[::-1]
str4 = b[::-1]
str5 = c[::-1]
str6 = str3+' '+ str4+' '+str5
print(str6)


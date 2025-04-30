"""Write a program that extracts the domain name from an email address using split().

Example Input:

"john.doe@gmail.com"

Expected Output:

"gmail.com" """

str1 = input("Enter the email address: ")
str2 = str1.split("@")
print(str2[1])
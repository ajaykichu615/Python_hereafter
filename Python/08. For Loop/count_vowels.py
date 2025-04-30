"""Write a for loop to count the number of vowels in the word 'hello'  """

str1 = 'Hello'
vowel = 'AEIOUaeiou'
c = 0

for i in str1:
    if i in vowel:
       c += 1
print(c)



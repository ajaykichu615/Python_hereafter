"""Write a function named count_words() that:
1. Asks the user for a sentence using input().
2. Counts the occurrences of each
unique word.
3. Prints the word count as a dictionary."""

def count_words():
    str1 = input("Provide a sentence: ").lower().split()
    dict1 = {}

    for i in str1:
        if i not in dict1:  # If word is new, add to dict with count 1
            dict1[i] = 1
        else:                 # If word exists, increment its count
            dict1[i] += 1

    print(dict1)

count_words()





def count_words(str1):
    lst = str1.split()
    dict1 = {}

    for i in str1:
        if i not in dict1:  # If word is new, add to dict with count 1
            dict1[i] = 1
        else:                 # If word exists, increment its count
            dict1[i] += 1

    print(dict1)

count_words("bleh bleh bleh")
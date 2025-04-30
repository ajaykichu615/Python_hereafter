"""Write a function that finds the first non-repeating character in a string.
Example:
Input: "aabbcddexc"
Output:'e'"""


def first_non_repeating_char(s):
    # Count occurrences of each character
    char_count = {}
    for char in s:
        char_count[char] = char_count.get(char, 0) + 1

    # Find the first character with count 1
    for char in s:
        if char_count[char] == 1:
            return char

    # Return None if no non-repeating character found
    return None


# Get input from user
str1 = input('Enter a string: ')
result = first_non_repeating_char(str1)

# Print the result
if result is not None:
    print(f"The first non-repeating character is: '{result}'")
else:
    print("All characters are repeating")




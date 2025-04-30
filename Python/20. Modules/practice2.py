""" Create a function generate_password(l,d,s) that returns a random password of length using letters,
digits and symbols"""

def generate_password(l,d,s):
    import string
    import random

    # Create character pools
    letter_chars = random.choices(string.ascii_letters, k=l)
    digit_chars = random.choices(string.digits, k=d)
    special_chars = random.choices(string.punctuation, k=s)

    # Combine all characters
    all_chars = letter_chars + digit_chars + special_chars

    # Shuffle the combined characters
    random.shuffle(all_chars)

    # Convert list to string
    password = ''.join(all_chars)

    return password


# Get user input
letters = int(input("How many Letters?: "))
digits = int(input("How many Digits?: "))
specials = int(input("How many Special characters?: "))

# Generate and print password
print("Password:", generate_password(letters, digits, specials))
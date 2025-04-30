"""Create a dictionary storing names as keys and phone numbers as values:

contacts = {
    "Alice": "9876543210",
    "Bob": "9123456789",
    "Charlie": "9234567890",
}
Exercises:
Print Bob’s phone number.
Add a new contact "David" with a phone number.
Update "Charlie"’s number to "9998887777".
Delete "Alice"’s contact.
Print all contact names.
"""
contacts = {
    "Alice": "9876543210",
    "Bob": "9123456789",
    "Charlie": "9234567890",
}

print(f" Bob's phone number: {contacts['Bob']}")
contacts['David']= '7012028872'
contacts.update({'Charlie':'9998887777'})
contacts.pop('Alice')
print(contacts)
print(list(contacts.keys()))
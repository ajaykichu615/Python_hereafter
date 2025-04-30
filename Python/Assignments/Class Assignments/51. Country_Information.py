"""Create a dictionary with country names as keys and details as values:

countries = {
    "India": {"capital": "New Delhi", "currency": "INR"},
    "USA": {"capital": "Washington, D.C.", "currency": "USD"},
    "Japan": {"capital": "Tokyo", "currency": "Yen"},
}
Exercises:
Print the capital of Japan.
Add "France" with "Paris" as capital and "Euro" as currency.
Change the currency of India to "Rupee".
Remove "USA" from the dictionary.
Print all country names.
"""

countries = {
    "India": {"capital": "New Delhi", "currency": "INR"},
    "USA": {"capital": "Washington, D.C.", "currency": "USD"},
    "Japan": {"capital": "Tokyo", "currency": "Yen"},
}

print(countries['Japan']['capital'])
countries.update({'France': {'capital':'Paris','currency': 'Euro'}})
countries['India']['currency'] = 'Rupee'
countries.pop('USA')
print(list(countries.keys()))
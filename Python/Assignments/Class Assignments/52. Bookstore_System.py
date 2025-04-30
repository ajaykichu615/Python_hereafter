"""Given a bookstore’s book stock:

books = {
    "Python Basics": {"author": "John Doe", "price": 400, "stock": 10},
    "Data Science": {"author": "Jane Smith", "price": 600, "stock": 5},
    "AI Guide": {"author": "Alan Turing", "price": 800, "stock": 2},
}
Exercises:
Print the author of "AI Guide".
Add a new book "Machine Learning" by "Andrew Ng" with price 700 and stock 4.
Increase stock of "Python Basics" by 5.
Reduce the stock of "AI Guide" by 1.
Print all books sorted by price.
"""

books = {
    "Python Basics": {"author": "John Doe", "price": 400, "stock": 10},
    "Data Science": {"author": "Jane Smith", "price": 600, "stock": 5},
    "AI Guide": {"author": "Alan Turing", "price": 800, "stock": 2},
}

print(books['AI Guide']['author'])
books.update({'Machine Learning':{'author': "Andrew Ng", 'price': 700, 'stock': 4}})
books['Python Basics']['stock'] += 5
books['AI Guide']['stock'] -= 1
sorted_books = list(sorted(books.items(), key = lambda x:x[1]['price']))

for title,_ in sorted_books:  #_ pythonic placeholder for avoiding unnecessary memory usage instead of using variables
    print(title)


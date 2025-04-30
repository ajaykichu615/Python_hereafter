""""A school library maintains a set of available books:

books = {"Python Basics", "Machine Learning", "Data Science", "AI Ethics"}

Tasks:
1. A new book "Deep Learning" arrives. Add it to the collection.

2. "AI Ethics" is borrowed. Remove it from the set.

3. "Blockchain Basics" is mistakenly recorded but never existed. Try removing it without an error.

4. The library adds a new set of books: {"Computer Vision", "Big Data"}. Update the collection.

5. Print the final list of books.
"""
books = {"Python Basics", "Machine Learning", "Data Science", "AI Ethics"}

books.add("Deep Learning")
books.remove("AI Ethics")
books.discard("Blockchain Basics")
books.update({"Computer Vision", "Big Data"})

print(books)
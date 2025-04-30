"""Create a dictionary with movie names as keys and their release years as values:

movies = {
    "Inception": 2010,
    "Titanic": 1997,
    "Avatar": 2009,
}

Exercises:
Print the release year of "Titanic".
Add a new movie "The Matrix" (1999).
Update "Avatar"'s year to 2022.
Remove "Titanic" from the dictionary.
Print all movies sorted by release year.
"""

movies = {"Inception": 2010,"Titanic": 1997,"Avatar": 2009}

print(movies['Titanic'])
movies['The Matrix']=1999
movies.update({'Avatar':2022})
movies.pop('Titanic')
print(sorted(movies.items(), key=lambda x: x[1]))
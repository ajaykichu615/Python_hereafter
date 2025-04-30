# Create a Movie class
# Class variables: industry, language, format (e.g., "Bollywood", "Hindi", "2D")
# Object variables: title, director, release_year
# Set object variables via the constructor.

class Movie:
    industry = 'Bollywood'
    language = 'Hindi'
    format = '2D'

    def __init__(self,title,director,release_year):
        self.title = title
        self.director = director
        self.release_year = release_year

    def display_details(self):
        print(f'Movie name: {self.title}')
        print(f'Director name: {self.director}')
        print(f'Release year: {self.release_year}')
        print(f'Language: {self.language}')



m1 = Movie("3 Idiots", "Rajkumar Hirani", 2009)
m2 = Movie("Dangal", "Nitesh Tiwari",2016)
m1.display_details()
m2.display_details()

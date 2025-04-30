# Create a University Class
# Class variables: country, accreditation, type (e.g., "India", "NAAC", "Public")
# Object variables: name, location, ranking
# Use the constructor to initialize the object variables.

class University:
    country = 'India'
    accreditation = 'NAAC'
    type = 'Public'

    def __init__(self,n,l,r):
        self.name = n
        self.location = l
        self.ranking = r

u1 = University("Delhi University", "Delhi", 5)
u2 = University("IIT Bombay", "Mumbai", 1)


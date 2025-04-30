"""Euclidean distance formula: sqrt((x2-x1)**2+(y2-y1)**2)
points = (x1,y1),(x2,y2)
euclidean_distance(p1,p2)"""

def euclidean_distance(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return ((x2 - x1)**2 + (y2 - y1)**2) ** 0.5

p1 = tuple(map(float, input("Enter first point (x1 y1): ").split()))
p2 = tuple(map(float, input("Enter second point (x2 y2): ").split()))

print(euclidean_distance(p1,p2))

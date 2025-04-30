"""In a school, there are two groups of students:

Group A studies: {Math, Physics, Chemistry, English}

Group B studies: {Biology, Chemistry, Physics, Computer Science}

Tasks:

1. Find the subjects common to both groups.

2. Find the subjects only studied by Group A.

3. Find the subjects only studied by Group B.

4. Find the subjects studied by at least one group.

5. Find the subjects that are not common but unique to each group.
"""

A = {'Math', 'Physics', 'Chemistry', 'English'}
B = {'Biology', 'Chemistry', 'Physics', 'Computer Science'}

common = A.intersection(B)
OnlyA = A.difference(B)
OnlyB = B.difference(A)
BothAB = A.union(B)
UniqueAB = A.symmetric_difference(B)

print("subjects common to both groups:", common)
print("subjects only studied by Group A:", OnlyA)
print("subjects only studied by Group B:", OnlyB)
print("subjects studied by at least one group:", BothAB)
print("subjects that are not common but unique to each group:", UniqueAB)

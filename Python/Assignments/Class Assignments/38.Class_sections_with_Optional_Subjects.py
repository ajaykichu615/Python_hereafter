"""
Section X students: {John, Alice, Bob, Rachel, Steve}

Section Y students: {Rachel, Steve, David, Emma, Bob}

Tasks:
1. Find students common to both sections.

2. Find students who are only in Section X.

3. Find students who are only in Section Y.

4. Find all students from both sections.

5. Find students not common in both sections"""

X = {'John', 'Alice', 'Bob', 'Rachel', 'Steve'}
Y = {'Rachel', 'Steve', 'David', 'Emma', 'Bob'}

print("students common to both sections: ",X.intersection(Y))
print("students who are only in Section X: ",X.difference(Y))
print("students who are only in Section Y: ",Y.difference(X))
print("students from both sections: ",X.union(Y))
print("students not common in both sections: ",X.symmetric_difference(Y))

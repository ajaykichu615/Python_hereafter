"""A teacher recorded student attendance on two different days:
Monday's attendees: {John, Alice, Bob, Rachel, Steve}
Wednesday's attendees: {Alice, Bob, Rachel, David, Emma}

Tasks:

1. Find the students who attended both days.

2. Find students who attended only on Monday.

3. Find students who attended only on Wednesday.

4. Find students who attended at least one day.

5. Find students who attended exactly one day.
"""

M = {'John', 'Alice', 'Bob', 'Rachel', 'Steve'}
W = {'Alice', 'Bob', 'Rachel', 'David', 'Emma'}

common  = M.intersection(W)
onlyM = M-W
onlyW = W-M
bothMW = M.union(W)
exactly_a_day = M.symmetric_difference(W)

print("students who attended both days:",common)
print("students who attended only on Monday:",onlyM)
print("students who attended only on Wednesday:",onlyW)
print("students who attended at least one day:",bothMW)
print("students who attended exactly one day:",exactly_a_day)

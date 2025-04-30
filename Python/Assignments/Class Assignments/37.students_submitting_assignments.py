"""The teacher gives a Python assignment. Two groups of students submit it:

Students who submitted Part 1: {Amit, Bella, Charlie, Diana, Ethan}

Students who submitted Part 2: {Charlie, Diana, Ethan, Farhan, Grace}

Tasks:
1. Find students who submitted both parts.

2. Find students who submitted only Part 1.

3. Find students who submitted only Part 2.

4. Find students who submitted at least one part.

5. Find students who submitted exactly one part.
"""
part1 = {'Amit', 'Bella', 'Charlie', 'Diana', 'Ethan'}
part2 = {'Charlie', 'Diana', 'Ethan', 'Farhan', 'Grace'}

print("students who submitted both parts:", part1.intersection(part2) )
print("students who submitted only Part 1:", part1.difference(part2) )
print("students who submitted only Part 2:", part2.difference(part1))
print("students who submitted at least one part:", part1.union(part2))
print("students who submitted exactly one part:", part1.symmetric_difference(part2))
"""In a school, students can join different clubs.

Science Club members: {Alice, Bob, Charlie, David, Eva}

Literary Club members: {Charlie, David, Fiona, George, Eva}

Tasks:
1. Find the students who are in both clubs.

2. Find students only in the Science Club.

3. Find students only in the Literary Club.

4. Find students who are in either of the clubs.

5. Check if there are any students common in both clubs.
"""

sci = {'Alice', 'Bob', 'Charlie', 'David', 'Eva'}
lit = {'Charlie', 'David', 'Fiona', 'George', 'Eva'}

common = sci.intersection(lit)
only_sci = sci.difference(lit)
only_lit = lit.difference(sci)
both_sci_lit = sci.union(lit)
check_both = sci.isdisjoint(lit)

print("students who are in both clubs: ",common)
print("students only in the Science Club: ",only_sci)
print("students only in the Literary Club: ",only_lit)
print("students who are in either of the clubs: ",both_sci_lit)
print("Check if there are any students common in both clubs: ", 'No' if check_both else 'Yes')
"""A school maintains a Science Club with existing members:

science_club = {"Alice", "Bob", "Charlie"}

Tasks:
1. Add a new student "David" to the club.

2. Add another student "Emma" who just joined.

3. Update the club with a new batch: {"Frank", "Grace", "Helen"}.

4. Print the final list of members.
"""

sci = {"Alice", "Bob", "Charlie"}

# Add a new student "David"
sci.add("David")

# Add another student "Emma"
sci.add("Emma")

# Update the club with a new batch
sci.update({"Frank", "Grace", "Helen"})

# Print the final list of members
print("Final list of members:", sci)




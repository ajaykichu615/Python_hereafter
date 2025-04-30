"""A coding competition has the following registered participants:

participants = {"Jake", "Mia", "Sophia", "Liam"}

Tasks:
1. Remove "Sophia" as she withdrew from the competition.

2. "Lucas" was added by mistake. Try removing him without error, even if he’s not in the list.

3. Remove and display any one random participant using a suitable method.

4. Clear the entire set after the competition ends.
"""

participants = {"Jake", "Mia", "Sophia", "Liam"}
participants.remove("Sophia")

print("After removing Sophia...",participants )

participants.discard("Lucas")

print("Random participant:", participants.pop())

participants.clear()
print("Cleared Set: ", participants )


"""An online Python workshop has registered participants:

attendees = {"John", "Sana", "Ravi", "Meera"}

Tasks:
1. "Tom" wants to join. Add him.

2. "Meera" cancels her participation. Remove her.

3. A last-minute batch of students joins: {"Kiran", "Latha", "Pooja"}. Update the set.

4. "Akhil" was never in the list but got added mistakenly. Remove him safely.

5. Remove a random participant using a suitable method.
"""

attendees = {"John", "Sana", "Ravi", "Meera"}

attendees.add("Tom")
attendees.remove("Meera")
attendees.update({"Kiran", "Latha", "Pooja"})
attendees.discard("Akhil")
attendees.pop()

print(attendees)
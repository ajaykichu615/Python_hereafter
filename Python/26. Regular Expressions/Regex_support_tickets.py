# 1. Extract all Ticket IDs.
# Sample Result: ['1001', '1002', ..., '1010']
#
# 2. Find all customer names who submitted a High priority ticket.
# Sample Result: ['Emily Carter', 'Sophia Lee', 'James Brown', 'Sophia Lee', 'John Miller']
#
# 3. Extract all distinct issue types.
# Sample Result:
# ['Login failed', 'Payment error', 'Account locked', 'Forgot password', 'Bug report', 'Unable to access files', 'Slow performance', 'Error 404 on dashboard']
#
# 4. List names and issues for tickets created in 2023-10-05.
# Sample Result:
# ['Mia Davis - Bug report', 'James Brown - Unable to access files']
#
# 5. Count how many tickets are marked as 'High' priority.
# Sample Result: 5
#
# 6. Create a dictionary where key = Name and value = number of tickets submitted.
# Sample Result:
#
# {
#   'Emily Carter': 2,
#   'John Miller': 2,
#   'Sophia Lee': 2,
#   'Daniel White': 1,
#   'Mia Davis': 1,
#   'James Brown': 1,
#   'Olivia Wilson': 1
# }
#
# 7. Extract ticket IDs for all issues containing the word 'Login'.
# Sample Result: ['1001', '1008']
#
# 8. Get all tickets where the issue starts with the word 'Account'.
#
# Sample Result:
# ['TicketID: 1003
# 'TicketID:1010...']

import re
with open(r'sample_support_tickets-1.txt', 'r') as obj1:
    text = obj1.read()

ticketID = re.findall(r'TicketID: (\d{4})', text)
names =  re.findall(r'Name: ([A-Za-z ]+?)\s*\|\s*Issue: .*?\|\s*Priority: High', text)
issue =  re.findall(r'Issue: (.*?)\s*\|', text)
names_on = re.findall(r'Name: ([A-Za-z ]+)\s*\|\s*Issue: (.*?)\s*\|\s*Priority: .*?\|\s*Date: 2023-10-05', text)
count = re.findall(r'Priority: High', text)
dict1_names = re.findall(r'Name:\s*([A-Za-z ]+)', text)
ticket_count = {}
for name in names:
    if name in ticket_count:
        ticket_count[name] += 1
    else:
        ticket_count[name] = 1
tickets_login = re.findall(r'TicketID: (\d+).*?Issue: .*?Login.*?', text)
tickets_account = re.findall(r'(TicketID: \d+).*?Issue: Account.*?', text)


print(ticketID)
print(names)
print(list(set(issue)))
print(names_on)
print(len(count))
print(ticket_count)
print(tickets_login)










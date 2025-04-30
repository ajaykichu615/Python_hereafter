# Open sample. txt in r+ mode, print its content, and then write "Updated!" at the beginning.

with open('sample.txt', 'w+') as s:
    print(s)
    s.write('Here we go')
with open('sample.txt', 'r+') as s:
    content = s.read()
    s.seek(0)
    s.write('Updated '+ content)
# Ask the user to input 3 sentences. Write them all into sentences.txt. Each sentence should be on new line.

with open('sentences.txt', 'w') as obj1:
    for i in range(1, 4):
        sentence = input(f"Enter sentence {i}: ") + '\n'
        obj1.write(sentence)


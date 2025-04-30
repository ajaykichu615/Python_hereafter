# Objective:
# Build a basic notepad application that allows the user to create and view personal notes using Python’s file handling modes w, a, and r.
# ---
# Instructions:
#
# Display a Menu to the User with the following choices:
# 1. Create a New Note
# 2. Append to an Existing Note
# 3. View a Note
# 4. Exit
#
# 2. If the user chooses "Create a New Note":
# Ask for the note title (use this as the filename, e.g., shopping.txt).
# Ask the user to enter multi-line content (use a loop to collect lines until the user types DONE).
# Save the content in a new file named <title>.txt.
# Use w mode to write the content (it will overwrite if file exists).
# Show a message: "Note saved successfully!"
#
#3. If the user chooses "Append to an Existing Note":
#  Ask for the existing note title (e.g., shopping.txt).
# If the file exists:
# Ask for additional content (until user types DONE).
# Use a mode to append it to the existing file.
# Show a message: "Note updated!"
#
# If the file does not exist:
# Show an error message: "Note not found!"
#
# 4. If the user chooses "View a Note":
# Ask for the note title.
# Open the corresponding file using r mode.
# Display the content of the note.
# If the file does not exist, show: "Note not found!"
#
# 5. If the user chooses "Exit", terminate the program with a goodbye message.

def get_multiline_input():
    print("Enter your content (type 'DONE' on a new line to finish):")
    lines = []
    while True:
        line = input()
        if line.strip().upper() == 'DONE':
            break
        lines.append(line)
    return '\n'.join(lines)


while True:
    print("\n--- Notepad Menu ---")
    print("1. Create a New Note")
    print("2. Append to an Existing Note")
    print("3. View a Note")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ").strip()

    if choice == '1':
        title = input("Enter the note title (without .txt): ").strip()
        content = get_multiline_input()
        with open(f"{title}.txt", 'w') as file:
            file.write(content)
        print(f"Note '{title}.txt' saved successfully!")

    elif choice == '2':
        title = input("Enter the title of the existing note (without .txt): ").strip()
        # Will crash if file does not exist (intentional)
        open(f"{title}.txt").close()
        content = get_multiline_input()
        with open(f"{title}.txt", 'a') as file:
            file.write('\n' + content)
        print("Note updated!")

    elif choice == '3':
        title = input("Enter the title of the note to view (without .txt): ").strip()
        with open(f"{title}.txt", 'r') as file:
            print("\n--- Note Content ---")
            print(file.read())

    elif choice == '4':
        print("Goodbye! Thanks for using Notepad.")
        break

    else:
        print("Invalid choice. Please enter 1, 2, 3, or 4.")

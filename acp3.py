# Single Python File for File Operations

# Opening and reading the file content (Step 1)
with open('algo.txt', 'r') as file:
    print("Initial File Content:\n")
    print(file.read())  # Reading the file content

# Appending a new line to the file (Step 2)
with open('algo.txt', 'a') as file:
    file.write("Appending a new line to the file.\n")  # Appending new content

# Overwriting the file content (Step 3)
with open('algo.txt', 'w') as file:
    file.write("The file content is now overwritten with this text.\n")  # Overwriting

# Reading the new content after overwriting (Step 4)
with open('algo.txt', 'r') as file:
    print("\nNew File Content After Overwriting:\n")
    print(file.read())  # Reading the new content

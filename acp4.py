# Single Python File for Reading Operations

# Creating a sample text file for demonstration
with open('example.txt', 'w') as file:
    file.write("Hello, World!\n")
    file.write("Welcome to Lesson 2: Operations on a File.\n")
    file.write("This file will be used for demonstrating various read operations.\n")
    file.write("Enjoy learning Python file handling!")

# 1. Reading the entire file at once
print("Reading the whole file:\n")
with open('example.txt', 'r') as file:
    content = file.read()
    print(content)  # Print the entire content

# 2. Reading the file line by line using readline()
print("\nReading the file line by line using readline():")
with open('example.txt', 'r') as file:
    line = file.readline()
    while line:
        print(line, end='')  # Print each line without extra newline
        line = file.readline()

# 3. Reading all lines at once as a list using readlines()
print("\n\nReading all lines at once (as a list) using readlines():")
with open('example.txt', 'r') as file:
    lines = file.readlines()
    for line in lines:
        print(line, end='')  # Print each line from the list

# 4. Using a loop to iterate through the file object
print("\n\nReading the file using a for loop:")
with open('example.txt', 'r') as file:
    for line in file:
        print(line, end='')  # Print each line while iterating

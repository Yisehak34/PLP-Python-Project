# File Read & Write Challenge + Error Handling Lab

# Ask the user for a filename
filename = input("Enter the name of the file to read: ")

try:
    # Open the original file for reading
    with open(filename, "r") as file:
        content = file.read()
    
    # Modify the content (example: convert all text to uppercase)
    modified_content = content.upper()
    
    # Write the modified content to a new file
    new_filename = "modified_" + filename
    with open(new_filename, "w") as new_file:
        new_file.write(modified_content)
    
    print(f"Modified content written to '{new_filename}' successfully!")

except FileNotFoundError:
    print("Error: The file does not exist ❌")
except IOError:
    print("Error: The file cannot be read or written ❌")

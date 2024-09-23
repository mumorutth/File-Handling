# file_handling_assignment.py

def create_file():
    try:
        # Create a new text file and write three lines of text
        with open("my_file.txt", 'w') as file:
            file.write("Hello, this is my first line.\n")
            file.write("The second line contains a number: 42\n")
            file.write("Finally, here is a third line!\n")
        print("File 'my_file.txt' created and written successfully.")

    except Exception as e:
        print(f"Error while creating the file: {e}")

def read_file():
    try:
        # Read the contents of the file and display them
        with open("my_file.txt", 'r') as file:
            content = file.read()
            print("\nContents of 'my_file.txt':")
            print(content)

    except FileNotFoundError:
        print("Error: The file 'my_file.txt' does not exist.")
    except PermissionError:
        print("Error: You do not have permission to read the file.")
    except Exception as e:
        print(f"An error occurred: {e}")

def append_to_file():
    try:
        # Append three additional lines to the file
        with open("my_file.txt", 'a') as file:
            file.write("Appending a fourth line!\n")
            file.write("Fifth line here with some text.\n")
            file.write("And here is the sixth line, just for fun!\n")
        print("Three lines appended to 'my_file.txt' successfully.")

    except FileNotFoundError:
        print("Error: The file 'my_file.txt' does not exist.")
    except PermissionError:
        print("Error: You do not have permission to write to the file.")
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    create_file()
    read_file()
    append_to_file()
    read_file()  # Read again to show the appended content

if __name__ == "__main__":
    main()

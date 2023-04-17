#Write a program to copy the contents of one file into another.

def copy_file(source_file, destination_file):
    """
    Copies the contents of one file into another.
    Args:
        source_file (str): Path to the source file.
        destination_file (str): Path to the destination file.
    """
    try:
        # Open the source file in read mode
        with open(source_file, 'r') as source:
            # Read the contents of the source file
            file_contents = source.read()

        # Open the destination file in write mode
        with open(destination_file, 'w') as destination:
            # Write the contents to the destination file
            destination.write(file_contents)

        print("File copied successfully.")
    except FileNotFoundError:
        print("One or both files not found.")
    except Exception as e:
        print("An error occurred:", e)


# Example usage:
source_file = "source.txt"  # Replace with the path to your source file
destination_file = "destination.txt"  # Replace with the path to your destination file

copy_file(source_file, destination_file)

# Prints ascii art from txt file, provided the file name is given

def print_ascii(textFile):
    # Read ASCII art from a text file
    with open(textFile, 'r') as file:
        ascii_art = file.read()

    # Split the ASCII art into lines
    lines = ascii_art.strip().split('\n')

    # Create a 2D array from the lines
    ascii_array = [list(line) for line in lines]

    # Print the 2D array
    for row in ascii_array:
        print("".join(row))

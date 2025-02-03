import sys
import csv
from tabulate import tabulate


def main():
    try:
        # Ensure a filename is provided
        if len(sys.argv) != 2:
            raise FileNotFoundError("Usage: python script.py filename.txt")

        filename = sys.argv[1]
        if not filename.endswith(".csv"):
            raise FileNotFoundError("Usage: python script.py filename.py")

        with open(filename, 'r') as file:
            reader = csv.reader(file)
            content = list(reader)  # Convert CSV data into a list of lists
    
        print(tabulate(content, headers="firstrow", tablefmt="grid"))  # Print the number of lines
    

    except FileNotFoundError as e:
        print(f"Error: {e}")
        sys.exit(1)  # Exit with error

    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)  # Exit with error

main()
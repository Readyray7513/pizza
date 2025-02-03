# CSV File Viewer

## Description

This script reads a CSV file and displays its contents in a formatted table using the `tabulate` module.

## Usage
python script.py filename.csv


### Requirements
- Python 3.x
- The script should be run from the command line.
- A valid CSV file (`.csv`) must be provided as an argument.

## Features
- Reads CSV files and displays their contents in a structured table.
- Uses the `tabulate` module to format the output.
- Provides error handling for missing arguments and incorrect file types.

## Error Handling
- If no filename is provided, the script will display an error message and exit.
- If a non-CSV file is provided, it will notify the user.
- Catches unexpected errors and provides a meaningful error message.

## Example
Given a file `example.csv` with the following content:


Name, Age, City
Alice, 25, New York
Bob, 30, Los Angeles
Charlie, 22, Chicago


Running:
python script.py example.csv


Will output:
+---------+-----+-------------+
| Name    | Age | City        |
+---------+-----+-------------+
| Alice   |  25 | New York    |
| Bob     |  30 | Los Angeles |
| Charlie |  22 | Chicago     |
+---------+-----+-------------+


## License
This script is free to use and modify.


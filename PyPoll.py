# PyPoll Program
# Nehla Amin
# April 16, 2022

# Imports
import datetime as dt
import csv
import random
import os


# The data we need to retrieve
load_file = os.path.join('Resources', 'election_results.csv')
save_file = os.path.join("analysis", "election_analysis.txt")

# read file
with open(load_file) as election_data:
    # Read the file object with the reader function.
    file_reader = csv.reader(election_data)

    # Print each row in the CSV file.
    for row in file_reader:
        print(row)

    # Print the header row.
    headers = next(file_reader)
    print(headers)


# Perform analysis:
# A complete list of candidates who received votes
# The percentage of votes each candidate won
# The total number of votes each candidate won
# The winner of the election based on popular vote



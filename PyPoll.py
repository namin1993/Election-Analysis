# PyPoll Program
# Nehla Amin
# April 16, 2022

# Purpose: Perform analysis
# A complete list of candidates who received votes
# The percentage of votes each candidate won
# The total number of votes each candidate won
# The winner of the election based on popular vote

# Imports
import datetime as dt
import csv
import random
import os


# The data we need to retrieve
load_file = os.path.join('Resources', 'election_results.csv')
save_file = os.path.join("Analysis", "election_analysis.txt")

total_votes = 0
candidate_options = []
candidate_votes = {}

# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# read file
with open(load_file) as election_data:
    # Read the file object with the reader function.
    file_reader = csv.reader(election_data)

    # Print the header row.
    headers = next(file_reader)

    # Create Candidate name list and Candidate vote dictionary
    for row in file_reader:
        
        total_votes += 1
        candidate_name = row[2]

        if candidate_name not in candidate_options:

            candidate_options.append(candidate_name)

            # Begin tracking that candidate's vote count.
            candidate_votes[candidate_name] = 0

        candidate_votes[candidate_name] += 1


with open(save_file, 'a') as txt_file:

    # Print the final vote count to the terminal.
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")
    print(election_results, end="")
    # Save the final vote count to the text file.
    txt_file.write(election_results)

    # Print Voting Results
    for candidate in candidate_options:

        votes = candidate_votes[candidate]
        vote_percentage = float(votes) / float(total_votes) * 100
        #print(f"{candidate}: received {vote_percentage:.1f}% of the vote. ({votes:,})\n")

        # Determine Winning Candidate
        if votes > winning_count:
            winning_count = votes
            winning_candidate = candidate
            winning_percentage = vote_percentage


    # Print Winning Candidate
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
        
    print(winning_candidate_summary)
    txt_file.write(winning_candidate_summary)
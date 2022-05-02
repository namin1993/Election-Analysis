# PyPoll Challenge

## Overview Election Audit

### Purpose

The purpose for this Election Audit script is to determine: 
1.) Who the winner of the election is
2.) Which county had the largest voter turnout
3.) The percentage of total votes contributed by voters of each county

## Analysis and Challenges

### Election Audit Results

- The total number of voters for this election was 369,711 people
-  The percentage of county votes out of the total voter turnout are as follows:
  - Jefferson at 10.5%
  - Denver at 82.8%
  - Arapahoe at 6.7%

- The county with the largest voter turnout in the election was Denver
- The percentage of votes per each election candidate are as follows:
  - Charles Casper Stockham: 23.0%
  - Diana DeGette: 73.8%
  - Raymon Anthony Doane: 3.1%
- The winner for this county election is Diana DeGette.


## Election Audit Summary

The two ways in which the election commission can modify the script in order to audit any election are as follows:

  - Change the file name within the file_to_load variable
    file_to_load = os.path.join("Resources", "New File Name")

    Make sure that the original CSV file has the same column order as the current election file used for this analysis.

  - Breakdown the popularity of each candidate within the voter base of each county. Do this by creating a for loop after the row reader loop (line 43). For each row in the CSV document that is read, if the candidate_name and county_vote from the row matches the current iteration of the county_list and candidate_name, count the vote and store the county, candidate, vote count in a dictionary of lists. 

  Make sure to define the dictionary variable and county_candidate_vote variable before the for loop.

  After line 84 of opening and writing into the election_analysis file, iterate through the dictionary with a for loop in order to write the information into a file.
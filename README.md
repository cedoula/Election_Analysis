# Election-Audit_Analysis

## Project Overview
A Colorado Board of Elections employee has given us the following tasks to complete the election audit of a recent local congressional election.

1. Calculate the total number of votes cast.
2. Provide a breakdown of the number of votes and the percentage of total votes for each county in the precinct.
3. Determine which county had the largest number of votes.
4. Get a complete list of candidates who received votes.
5. Calculate the total number of votes each candidate received.
6. Calculate the percentage of votes each candidate won.
7. Determine the winner of the election based on popular vote.

## Resources
- Data Source: election_results.csv
- Software: Python 3.7.6, Visual Studio Code 1.47.3

## Election-Audit Results
The analysis of the election shows that:
- There were 369,711 votes cast in the election.
- The breakdown of the number of votes and the percentage of total votes per county was:
    - Jefferson had 10.5% of the votes and 38,855 ballots cast.
    - Denver had 82.8% of the votes and 306,055 ballots cast.
    - Arapahoe had 6.7% of the votes and 24,801 ballots cast.
- The county with the largest turnout was Denver with 82.8% of the votes and 306,055 number of votes.
- The candidates were:
    - Charles Casper Stockham
    - Diana DeGette
    - Raymon Anthony Doane
- The candidate results were:
    - Charles Casper Stockham received 23.0% of the vote and 85,213 number of votes.
    - Diane DeGette received 73.8% of the vote and 272,892 number of votes.
    - Raymon Anthony Doane received 3.1% of the vote and 11,606 number of votes.
- The winner of the election was:
    - Diana DeGette, who received 73.8% of the vote and 272,892 number of votes.

## Election-Audit Summary
We have created the script *PyPoll_Challenge.py* for this project. It could be modified in order to be used to conduct an audit analysis for any election organized by the election commission.\
Here are the requirements:
1. Ensure the election results *.csv file has the following structure:  
```
Ballot ID | County | Candidate
```
2. Modify *PyPoll_Challenge.py* script by assigning user input variables for the folder and name of the results *.csv file and analysis *.txt file which will respectively be read and saved.\
Here is an example of the new script:\
Change code from
```
# Add a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")

# Add a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")
```
to 
```
# Ask User to enter the folder and file name of the results *.csv file to read
file_to_load_location = input("Enter the name of the folder containing the results *.csv file please.  ")
file_to_load_name = input("Enter the name of the results *.csv file please.  ")
# Add a variable to load a file from a path.
file_to_load = os.path.join(file_to_load_location, f"{file_to_load_name}.csv")

# Ask User to enter the folder and file name of the analysis *.txt file to create/save
file_to_save_location = input("Enter the name of the folder containing the analysis *.txt file please.  ")
file_to_save_name = input("Enter the name of the analysis *.txt file please.  ")
# Add a variable to save the file to a path.
file_to_save = os.path.join(file_to_save_location, f"{file_to_save_name}.txt")
```

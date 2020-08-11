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
How to use for any election:
- assign user input variables for csv file and folder location and use it in the code to open the correct file to read.
- assign user input variables for txt file to save and its folder location and use it in code to write results in it.
- make sure result csv file has the following structure: Ballot ID | County | Candidate
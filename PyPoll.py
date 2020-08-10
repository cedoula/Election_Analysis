# The data we need to retrieve:
# 1 - Total number of votes cast.
# 2 - A complete list of candidates who received votes.
# 3 - Total number of votes each candidate received.
# 4 - Percentage of votes each candidate won.
# 5 - The winner of the election based on popular vote.

import csv
import os

# Assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources","election_results.csv")
# Assign a variable for the file to save and the path
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Initialize a total vote counter.
total_votes = 0
# Declare a list of candidates.
candidate_options = []
# Declare a dictionary for the votes per candidate
candidate_votes = {}
# Declare a variable for the winning candidate
winning_candidate = ""
# Declare a variable for the winning count
winning_count = 0
# Declare a variable for the winning percentage
winning_percentage = 0.0

# Open the election results and read the file.
with open(file_to_load) as election_data:
    
    # To do: read and perform analysis.
    # Read the file object with the reader function.
    file_reader = csv.reader(election_data)
    
    # Read and print the header row.
    headers = next(file_reader)

    # Print each row in the CSV file.
    for row in file_reader:
        # Increment total_votes
        total_votes +=1
        # Print the candidate name from each row>
        candidate_name = row[2]
        # Check if candidate name has been added to the candidate list.
        if candidate_name not in candidate_options:
            # Add candidate name to the candidate options ist
            candidate_options.append(candidate_name)

            # Begin tracking that candidate's vote count.
            candidate_votes[candidate_name] = 0

        # Add a vote to that candidate's count.
        candidate_votes[candidate_name] +=1

# Open the result txt file and write to it.
with open(file_to_save, "w") as txt_file:
    # Print the final vote count to the terminal
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")
    print(election_results, end="")
    # Save the final vote count to the text file.
    txt_file.write(election_results)

    # Iterate through the candidate list.
    for candidate_name in candidate_options:
        # Retrieve the vote count of a candidate.
        votes = candidate_votes[candidate_name]
        # Calculate the percentage of votes of a candidate.
        vote_percentage = (float(votes) / float(total_votes)) * 100
        # Print the candidate name and its percentage of vote.
        candidate_results = (f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
        print(candidate_results)
        # Save the candidate results to the text file.
        txt_file.write(candidate_results)
        
        # Determine winner vote count and name.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_percentage = vote_percentage
            winning_candidate = candidate_name

    # Winning summary 
    winning_candidate_summary = (
        f"------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"------------------------\n")

#print(winning_candidate_summary)


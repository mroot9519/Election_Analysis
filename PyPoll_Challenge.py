# The data we need to retreieve.
# 1. The total number of votes cast
# 2. A complete list of candidates who received votes.
# 3. The percentage of votes each candidate won.
# 4. The total number of votes each candidate won
# 5. The winner of the election based on the popular vote.

# Open CSV
# Add our dependencies.
import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources/election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")
# Initialize a total vote counter.
total_votes = 0
# Candidate options and candidate votes
candidate_options = []
candidate_votes = {}
# Track the winning candidate, vote count, and percentage.
winning_candidate = ""
winning_count = 0
winning_percentage = 0
#County namaes and votes
counties = []
county_votes = {}

largest_turnout = 0
largest_turnout_county = ""
# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)
    # Read the header row.
    headers = next(file_reader)
    # Print each row in the CSV file.
    for row in file_reader:
        # Add to the total vote count.
        total_votes += 1
        # Get the candidate name from each row.
        candidate_name = row[2]
        # Get county name from each row
        county_name = row[1]
        # If statement does nnot match any existing candidate add it to tje
        # candidate list
        if county_name not in counties:
            #append new counties to county list
            counties.append(county_name)
            # Begin tracking county votes
            county_votes[county_name] = 0
        # add a vote to county count
        county_votes[county_name] += 1
        # If the candidate does not match any existing candidate add it the
        # the candidate list.
        if candidate_name not in candidate_options:
            # Add the candidate name to the candidate list.
            candidate_options.append(candidate_name)
            # And begin tracking that candidate's voter count.
            candidate_votes[candidate_name] = 0
        # Add a vote to that candidate's count
        candidate_votes[candidate_name] += 1
#Save results as text file
with open(file_to_save,"w") as txt_file:
    # Print the final vote count to the terminal.
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")
    print(election_results, end="")
    # Save the final vote count to the text file.
    txt_file.write(election_results)

    #Print County Votes
    for county in county_votes:
        #Retrieve vote count and percentage
        votes_per_county = county_votes[county]
        county_vote_percentage = float(votes_per_county) / float(total_votes) * 100
        county_results = (f"{county}: {county_vote_percentage:.1f}% ({votes_per_county:,})\n")
        print(county_results)
        if (votes_per_county > largest_turnout): 
            largest_turnout = votes_per_county
            largest_turnout_county = county
        txt_file.write(county_results)
    #Print largest turnout county
    largest_turnout_summary = (
        f"-------------------------\n"
        f"Largest Turnout County: {largest_turnout_county}\n"
        f"-------------------------\n"
        )
    print(largest_turnout_summary)
    #Save to text file
    txt_file.write(largest_turnout_summary)

    for candidate in candidate_votes:
        # Retrieve vote count and percentage.
        votes = candidate_votes[candidate]
        vote_percentage = float(votes) / float(total_votes) * 100
        # Print each candidate, their voter count, and percentage to the
        # terminal.
        candidate_results = (f"{candidate}: {vote_percentage:.1f}% ({votes:,})\n")
        # Print each candidate, their voter count, and percentage to the terminal.
        print(candidate_results)
        #  Save the candidate results to our text file.
        txt_file.write(candidate_results)
        

        # Determine winning vote count, winning percentage, and candidate.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_candidate = candidate
            winning_percentage = vote_percentage
    # Print the winning candidates' results to the terminal.
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    print(winning_candidate_summary)
    # Save the winning candidate's name to the text file.
    txt_file.write(winning_candidate_summary)





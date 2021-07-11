# The data we need to retrieve.
# 1. Total Number of votes cast.
# 2. A complete list of candidates who received votes.
# 3. Percentage of votes each candidates won.
# 4. The total number votes each candidates won.
# 5. The winner of election based on popular votes.

# Import the datetime class from the datetime module.
import datetime

# Use the now() attribute on the datetime class to get the present time.
now = datetime.datetime.now()

# Print the present time.
print("The time right now is ", now)

# Import csv module.
import csv
import os

# Assign a variable for the file to load and the path.
file_to_load = os.path.join('Resources', 'election_results.csv')

# Open the election results and read the file.
election_data = open(file_to_load, 'r')

# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Using the with statement open the file as a text file.
outfile = open(file_to_save, "w")

# 1. Initialize a total vote counter.
total_votes = 0

# Initialize Candidate List Variable.
candidate_options = []

# Declare Empty Candidate Votes Dictionary
candidate_votes = {}

# Declare winning count and winning percentage variables
winning_count = 0
winning_percentage = 0
winning_candidate = ""


# Read the file object with the reader function.
with open(file_to_load, "r") as election_data:
    file_reader = csv.reader(election_data)

    # Read the header in the election data.
    headers = next(file_reader)
    print(headers)

    # Print each row in the CSV file.
    for row in file_reader:

        # Increment total_votes
        total_votes += 1

        # Print Candidate Name in each row
        candidate_name = row[2]

        # Add Candidate Name to the Candidate Option if not already added
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)

            # Track candidate votes for each candidate
            candidate_votes[candidate_name] = 0
            
        # Add Votes for the candidate
        candidate_votes[candidate_name] += 1        

    # Print Total Votes for each candidate
    print(candidate_votes)

    # Calculate Votes % for each candidate.
    for candidate_name in candidate_votes:
        votes = candidate_votes[candidate_name] 
        votes_percentage = (float(votes) / float(total_votes)) * 100
        # print(f"{candidate_name} received {votes_percentage:.1f} % of total votes. Received {votes}.")

        # Determine winning vote count and candidate
        # Determine if the votes is greater than the winning count.
        if (votes > winning_count) and (votes_percentage > winning_percentage):
            # If true then set winning_count = votes and winning_percent = vote_percentage.
            winning_count = votes
            winning_percentage = votes_percentage
         
            # And, set the winning_candidate equal to the candidate's name.
            winning_candidate = candidate_name

        #  To do: print out the winning candidate, vote count and percentage to terminal.
        print(f"{candidate_name}: {votes_percentage:.1f}% ({votes:,})\n")

    winning_candidate_summary = (
    f"-------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"-------------------------\n")
    print(winning_candidate_summary)

# Using the with statement open the file as a text file.
with open(file_to_save, "w") as txt_file:

    # Print the final vote count to the terminal.
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n")

    print(election_results, end="")
    
    # Save the final vote count to the text file.
    txt_file.write(election_results)
    txt_file.write(winning_candidate_summary)
# Open the electopn data file and read.
# with open(file_to_load) as election_data:
#    print(election_data)

# Close the file.
election_data.close()
txt_file.close()

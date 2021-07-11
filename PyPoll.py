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

# Using the with statement open the file as a text file.
with open(file_to_save, "w") as txt_file:

    # Write some data to the file.
    txt_file.write("Counties in Election\n----------------\nArapahoe\nDenver\nJefferson")

# Open the electopn data file and read.
# with open(file_to_load) as election_data:
#    print(election_data)

# Read the file object with the reader function.
with open(file_to_load, "r") as election_data:
    file_reader = csv.reader(election_data)

    # Read the header in the election data.
    headers = next(file_reader)
    print(headers)


# Close the file.
election_data.close()
txt_file.close()

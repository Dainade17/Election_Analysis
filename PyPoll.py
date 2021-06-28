import csv
import os

####***** unsolved******
#dir(os) 

####***** unsolved******
#dir(csv)

#assign a variable to load file
file_to_load = os.path.join("Module_3", "Module_Practice", "Election_Analysis","3-3-Resources", "election_results.csv")


# assign a variable to save file
file_to_save = os.path.join("Module_3", "Module_Practice", "Election_Analysis","analysis", "election_analysis.txt")

total_votes= 0
candidate_options = []
candidate_votes = {}

winning_candidate = ""
winning_count = 0
winning_percentage = 0
# Open the election results and read the file.
with open(file_to_load) as election_data:

    # Print the file object.
    # print(election_data)
#### ******the result does not look the way it shows in the module******

    file_reader = csv.reader(election_data) 

    headers = next(file_reader)
    #print(headers)

    # To print all data or specific column
    for row in file_reader:
        total_votes += 1
        #print(total_votes)

        # Print the candidate name from each row.
        candidate_name = row[2]

        # Add the candidate name to the candidate list.
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)
            candidate_votes[candidate_name] = 0
        candidate_votes[candidate_name] += 1
        # Print the candidate list.
print(candidate_votes)

for candidate_name in candidate_votes:
    # 2. Retrieve vote count of a candidate.
    votes = candidate_votes[candidate_name]
    # 3. Calculate the percentage of votes.
    vote_percentage = float(votes) / float(total_votes) * 100
    # 4. Print the candidate name and percentage of votes.
    print(f"{candidate_name}: received {vote_percentage}% of the vote")
    


    if (votes > winning_count) and (vote_percentage > winning_percentage):
         # If true then set winning_count = votes and winning_percent =
         # vote_percentage.
         winning_count = votes
         winning_percentage = vote_percentage
         # And, set the winning_candidate equal to the candidate's name.
         winning_candidate = candidate_name
winning_candidate_summary = (
    f"-------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"-------------------------\n")
print(winning_candidate_summary)

####################References############################
#Writing file
'''
# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")
# Using the open() function with the "w" mode we will write data to the file.
open(file_to_save, "w")

# Using the with statement open the file as a text file.
outfile = open(file_to_save, "w")
# Write some data to the file.
outfile.write("Hello World")

# Close the file
outfile.close()


# Using the with statement open the file as a text file.
with open(file_to_save, "w") as txt_file:

    # Write some data to the file.
    txt_file.write("Counties in the Election")
    txt_file.write("\n------------------------")
    txt_file.write("\nArapahoe\nDenver\nJefferson")
    '''
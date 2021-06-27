import csv
import os

####***** unsolved******
#dir(os) 

####***** unsolved******
#dir(csv)

#assign a variable to load file
file_to_load = os.path.join("3-3-Resources", "election_results.csv")


# assign a variable to save file
file_to_save = os.path.join("analysis", "election_analysis.txt")


# Open the election results and read the file.
with open(file_to_load) as election_data:

    # Print the file object.
    # print(election_data)
#### ******the result does not look the way it shows in the module******

    file_reader = csv.reader(election_data) 

    headers = next(file_reader)
    print(headers)
    '''
    # To print all data or specific column
    for row in file_reader:
        print(row[0])
    '''
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
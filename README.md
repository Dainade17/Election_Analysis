# Election_Analysis

1. Overview of Election Audit: 
- The purpose of this challenge was to study the election results and find out the county with the highest count of voter turnout in addition to the winning cadidate. We considered 3 counties Jefferson, Denver and Arapahoe and saw Denver had the highest turnout.
- We already figured the winning cadidate while working through the modules. We have the winning cadidate name printed in the txt file. 

2. Election-Audit Results:
- Total vote count was 369,711. This was the first analysis we did by simply storing the total row count excluding the header by running a for loop and adding one as we found value in each row. We stored this in the variable total_votes.
    Code used-
    for row in reader:
        total_votes = total_votes + 1

- Denver has the maximum votes with 306,055, which is 82.8% of the total voter turnout
- To determine which county had the largest voter turnout we calculated the total number of votes for county and the percentage of total votes for each county in the precinct:

i. We first declared the list, dictionary and variables where we wanted to store the results which we ultimately wanted to print
  - We declared a list as county_list = [] to store the county names and a dictionary as county_dict = {} to store the county names and county votes. 
  - We also declared 3 variables to store the winning county name as winning_county="", winning county vote count as winning_county_count= 0 and winning county vote      percentage as winning_county_percentage= 0
  - We also specified the column using the row function to run through to find out county names and total votes for each county
    Code used-
    county_name = row [1]


ii. We began with a for loop (same as above) and then we introduced a conditional statement inside the loop to append all the unique county names and then add 1 as each time we find the name
    Code used- 
        if county_name not in county_list:
            county_list.append(county_name)
            county_dict[county_name] = 0
        county_dict[county_name] += 1
 
iii. Once we figured the all the counties and their total vote count we were able to calculate the vote percentages of each county and find the winning county with maximum votes
  Code used- 
    for county_name in county_dict:
        county_votes_count = county_dict.get(county_name)
        county_vote_percentage = float(county_votes_count) / float(total_votes) * 100
        county_results = (f"{county_name}: {county_vote_percentage:.1f}% ({county_votes_count:,})\n")                
        if (county_votes_count > winning_county_count) and (county_vote_percentage > winning_county_percentage):
            winning_county_count = county_votes_count
            winning_county_percentage = county_vote_percentage
            winning_county = county_name       

- Diana DeGette was the winning cadidate with 72,892 votes and their vote percentage is 73.8%
To determine the winning candidate we followed the same set of codes and i.e. 
    i. Specify which row to conisder for candidate name
         Code used-
         candidate_name = row[2]
    ii. Within the for loop, run a condition to store the candidate names in the declared lists followed by their vote count in the dictionary
         Code used-     
                if candidate_name not in candidate_options:
                candidate_options.append(candidate_name)
                candidate_votes[candidate_name] = 0
            candidate_votes[candidate_name] += 1
    iii. Once the candidate name and their vote count were determined we calculated who was the winning cadidate
        Code used-
        for candidate_name in candidate_votes:
        votes = candidate_votes.get(candidate_name)
        vote_percentage = float(votes) / float(total_votes) * 100
        candidate_results = (
            f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
        print(candidate_results)
        txt_file.write(candidate_results)
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_candidate = candidate_name
            winning_percentage = vote_percentage
 

 3. Election-Audit Summary: This script can be reused in future for other election result calculation provided we ensure the location for read and writing are accurate as well as the rows we specified for county calculation and winning voter calculations are accurate. 
I was able to change one of the county name and save the csv file and rerun the code. The result replaced the old county name with the new county name and printed the correct result. 

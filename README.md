# Election_Analysis

## Project Overview
This project is to analyze the recently concluded election and provide the below results.

1. Calculate total votes cast.
2. Get the list of candidates who got votes.
3. Calculate total votes each candidate received.
4. Calculate the percentage of votes each candidate received.
5. Determine the winning candidate based on popular votes.

## Resources
The below 2 resources were used.

1. election_results.csv file whihc is the data source.
2. Python3 software code snd VS Code to determne read and process the file, then provide the results.

## Election-Audit Results

1. Total votes casted in the recently concloded congressional election: 369,711
2. Breakdown of votes in each participating counties is below.
    County          Votes %         Total Votes
    ------          -------         -----------
    Jefferson       10.5%           38,855
    Denver          82.8%           306,055
    Arapahoe        6.7%            24,801

3. Based on the above breakdown, Denver received largest number of votes.
4. Breakdown of votes received by the candidates contested in election is below.
    Candidate                       Votes %         Total Votes
    ---------                       -------         -----------
    Charles Casper Stockham         23.0%           85,213
    Diana DeGette                   73.8%           272,892
    Raymon Anthony Doane            3.1%            11,606
    
5. Based on the above breakdown, Diana DeGette won the elections.
    
## Election-Audit Summary
With the delivery of the Python script, I would like to propose the useage of this script for the upcoming elections to analyse and identify the results of the elections in a much quicker and efficient fashion. By running the script, we save a lot of time by analyzing the data in an automated way. By this automation, we are confident that:

1. The results will be very accurate, since the changes of human errors are eliminated and
2. The results will be published in a much shorter time period.

To use this script for the upcoming elections, we will need to do small changes to the script.
1. The source file name and the location should be changed based on the location of the file. This change can be made at the line 9 of the script.
2. The output file shall also be changed as desired. This shance shall be made at line 11 of the script.
3. The script shall be made more efficient to chose the file using an input dialog to choose the source file.

## Challenges:
1. This script assumes the source (csv) file has clean data and is in the same format. 
2. The code needs major refactor in order to support different file formats and to support additional data columns in the csv file.

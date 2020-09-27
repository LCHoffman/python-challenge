# python-challenge
Lindsey Hoffman - Python Homework 

I used working with lists as my main method for parsing and analyzing the data for both PyBank and PyPoll.  

In PyBank, I built lists from the CSV to keep track of the months, the profit or loss each month and the change in profit.  The months list (total_month) was used to find the total number of months, for calculating average change and for identifying the month with the greatest increase or decrease in profit.  The profit and loss list (pandl) was used to calculate the total revenue for the time frame and to iterate through to calculate the change in profit from month to month.  These results were added to the profit_change list.  The profit_change list was used to find the greatest increse (max) and greatest decrease (min) in profit.  These placement of these values in the list were compared to the total_months list to find the month for each.

In PyPoll, I built lists from the CSV first to hold all of the votes (voter) and all of the candidates (candidate) which were entered each time a vote for them was placed.  The total votes counted was found by taking the length of the voter list.  This number was also used to calculate vote percentages.  I then counted each incidence of each voter name in the candidate list and used those values to calculate the vote percentage.  To determine the winner, I created two new lists (Names and percent_list) and zipped them together to compare each candidate's percentage.

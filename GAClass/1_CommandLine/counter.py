#!/usr/bin/python
""" Lesson on piping csv output into python executable """
# Use in bash to write to output file
#$cat nytimes.csv | python counter.py > myoutput.txt

# import required libraries
import sys
import re

age = 0
impressions = 0
clicks = 0
max_age = 0
age_total = 0
total = 0

# Start a counter and store the textfile in memory
lines = sys.stdin.readlines()
#lines.pop(0) # Gets rid of header file

# Use regular expression to match if numeric, comma, or line return
mypattern = re.compile(r'[0-9,\n\r]')
#mypattern = re.compile(r'[a-zA-Z"]')

#"Age","Gender","Impressions","Clicks","Signed_In"
# For each line, find the sum of index 2 in the list.
for line in lines:

    if mypattern.match(line):

        cur_age = int(line.strip().split(',')[0]) #Age
        age = age + cur_age
        impressions = impressions + int(line.strip().split(',')[2]) #Impressions
        clicks = clicks + int(line.strip().split(',')[3]) #Clicks
        total = total+1

        # Store maximum age
        if cur_age >= max_age:
            max_age = cur_age

        # Whose online as a baby?!  Ignore babies age 0
        if cur_age > 0:
            age_total = age_total + 1
        else:
            continue
    else:
        lines.pop() #Remove line if any unidentified characters



print "Impressions Sum:", impressions
print "Age Average:", float(age)/total
print "Age Average (no zeroes):", float(age)/age_total
print "Total Clicks:", clicks
print "Click through rate:", float(clicks)/impressions
print "Oldest person in the file:", max_age
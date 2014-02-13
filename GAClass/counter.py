#!/usr/bin/python
""" Lesson on piping csv output into python executable """
# Use in bash to write to output file
#$cat nytimes.csv | python impressionser.py > mytest.txt

# import required libraries
import sys

age = 0
impressions = 0
clicks = 0
maxage = 0
agetotal = 0
total = 0

# Start a counter and store the textfile in memory
lines = sys.stdin.readlines()
lines.pop(0)

#"Age","Gender","Impressions","Clicks","Signed_In"
# For each line, find the sum of index 2 in the list.
for line in lines:
    cur_age = int(line.strip().split(',')[0]) #Age
    age = age + cur_age
    impressions = impressions + int(line.strip().split(',')[2]) #Impressions
    clicks = clicks + int(line.strip().split(',')[3]) #Clicks
    total = total+1

    # Whose online as a baby?!
    if cur_age > 0:
        agetotal = agetotal + 1
    else:
        continue


    # Store maximum age
    if cur_age >= maxage:
        maxage = cur_age

print "Impressions Sum:", impressions
print "Age Average:", float(age)/total
print "Age Average (no zeroes):", float(age)/agetotal
print "Total Clicks:", clicks
print "Click through rate:", float(clicks)/impressions
print "Oldest person in the file:", maxage
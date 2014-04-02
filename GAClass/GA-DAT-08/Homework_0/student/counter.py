#!/usr/bin/python
# import required libraries
import sys

# Start a counter and store the textfile in memory
count = 0
lines = sys.stdin.readlines()
lines.pop(0)

# For each line, find the sum of index 2 in the list.
for line in lines:
    count = count + int(line.strip().split(',')[2])

print count

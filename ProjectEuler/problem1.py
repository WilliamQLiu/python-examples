"""If we list all the natural numbers below 10 that are multiples of 3 or 5, we get
   3, 5, 6 and 9.  The sum of these multiples is 23.

   Find the sum of all the multiples of 3 or 5 below 1000"""

"""Algorithm:
   if multiple of 3 and 5 then
   else if multiple of 3 then
   else if multiple of 5 then
   else nothing

   sum list
"""

def multiples(number):
    total=0
    index=0
    while(index<number):
        if((index%3==0) and (index%5==0)):
            total+=index
        elif (index%3==0):
            total+=index
        elif (index%5==0):
            total+=index
        index=index+1
    return total

if __name__ == "__main__":
    print multiples(10)
    print multiples(1000)
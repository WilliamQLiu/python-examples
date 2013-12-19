"""
Background:
Solve the following problem (show me, don't just tell me)
  The prime factors of 13195 are 5, 7, 13 and 29.  
  What is the largest prime factor of the number 600851475143?

  I'm a little rusty so I started by wikipeding these:

    Prime numbers
        * Number P > 1 is called prime if and only if the only numbers
          that divide P without a remainder are 1 and P
    
    Prime Factors 
        * The prime numbers that divide that integer exactly
        * E.g. 5 * 7 * 13 * 29 = 13195

    Fundamental Theorem of Arithmetic
        * Any number is either:
          1.) a prime number or
          2.) can be made up of prime numbers
          * There is only one distinct set of prime factors for any number
          * By distinct, it means list prime factor only once
          * E.g. 330 = 2 * 3 * 5 * 11 and 39 = 3 * 13
"""

#First attempt, just made a list of prime numbers, out of memory on large numbers
def get_prime(number):
	primenumbers=[]
	for index in range(2, number):
		if(number%index == 0):
			primenumbers.append(index)
	return primenumbers

#Solution for returning largest prime factor of a number
def fund_theorem(number):
    counter=2 #Smallest prime number
    largestfactor=0 #Holds largest prime factor
    while(counter <= number): #Go through all the numbers
        if(number%counter==0): #If the number has no remainder
            number = number/counter #We can factor out this counter (since we know there's a distinct prime factor)
            largestfactor=counter #sets current largest prime factor
        counter = counter+1 #will set the counter up 1 so we can see if it's the next prime factor
    return largestfactor

if __name__ == "__main__":
    
    testcase1=39
    testcase2=330
    testcase3=13195
    testcase4=600851475143

    print fund_theorem(testcase4)
    """
      Explaination:
      Let's use the Fundamental Theorem of Arithmetic (i.e. a number = one distinct prime factor combination)
      We'll combine this with the algorithm 'Sieve of Erathosthenes' (I had to wiki for algorithms)
      The idea is to 'sieve' out prime factors knowing that all numbers must be made of 
      one distinct combination of prime factors
      
      Here's an example with number (39):

      * we set the counter at 2 because it's the smallest prime number
      * the number (39) can't divide by the counter (2) to get a nice round integer (i.e. can't sieve it)
        so we increment the counter to 3
      * the number (39) can divide by the counter (3) to get a nice round integer with no remainder (i.e. can sieve)
      * we 'sieve' out the prime factor/counter (3) and now the number is (13)
        * this prime factor/counter is now the current largest factor
      * we continue counting up while incrementally checking if we can sieve out any more prime factors
      * there isn't anymore prime factors until we reach the last number (13)
      * we replace the previous largestfactor (3) with the new larger one (13)

      Idea: if we need to make this faster and if this is applied for large numbers only, we can make the counter
        1) go through a list of just prime numbers instead of incrementing the counter by 1
        2) instead of going through every number, the last number checked can be the square root of the number (say rounded up to be safe)
           E.G.  sqrt of 600,851,475,143 is 775146.0992
                 if we multiply 775147 * 775147 we get 600,853,871,609
    """
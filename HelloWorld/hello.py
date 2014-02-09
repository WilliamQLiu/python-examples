# Will's First Python Program

# import modules used here -- sys is a very standard one
import sys

# Gather our code in a main() function
def main():
    try:
        print 'Hello World!  My name is ', sys.argv[1]
    except:
        print 'Hello World!'
    # Command line args are in sys.argv[1], sys.argv[2] ...
    # sys.argv[0] is the script name itself and can be ignored

# Standard boilerplate to call the main() function to begin
# the program.
if __name__ == '__main__':
    main()

# Find best implementation available on the platform
try:
    from cStringIO import StringIO  # Much faster, C implementation
    print "Loaded cStringIO"
except:
    from StringIO import StringIO  # Much more portable
    print "Loaded StringIO"


if __name__ == '__main__':

    # Write to a buffer
    myoutput = StringIO()
    myoutput.write("This goes to the buffer")
    print >>myoutput, "And this too"

    # Retrieve the value written
    print myoutput.getvalue()

    myoutput.close()  # Discard buffer memory

    # Initialize a read buffer
    myinput = StringIO('Initial value for read buffer')

    # Read from the buffer
    print myinput.read()


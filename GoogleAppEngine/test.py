
months = ['January',
          'February',
          'March',
          'April',
          'May',
          'June',
          'July',
          'August',
          'September',
          'October',
          'November',
          'December']
          
def valid_month(month):
    month = month.lower() # Puts it into all lowercase
    month = month.title() # Puts first character to upper case
    for x in range(12):
        if month==months[x]:
            print months[x]
            return
    print "None"

valid_month("jaNuAry")  
valid_month("January")
valid_month("foo")
valid_month("")
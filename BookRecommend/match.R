# Open up library for ODBC connections
library(RODBC)
library(plyr) #Needed to use function ddply

# Connect to ODBC using: odbcConnect(DSN, uid="", pwd="")
dbhandle <- odbcDriverConnect("driver={SQL Server};server=WILL-PC\\SQLEXPRESS;database=BookDatabase;Trusted_Connection='yes'")

# Select all data from table Books (assuming [BookDatabase].[dbo].[Books])
mydata <- sqlQuery(dbhandle, 'SELECT * FROM [Books]')

# See the first 6 rows of data using head()
head(mydata)
#   UserID       ISBN BookRating                                  BookTitle
#1     169 0446601640           7                    Slow Waltz in Cedar Bend
#2     176 1900850303           4                        The Angelic Darkness
#3     178 0451410319           6                                        Hush
#4     183 2070567842           8 Folio Junior: L'histoire De Monsieur Sommer
#5     183 8401422825           9                              Fahrenheit 451
#6     183 8440630794           7                  Cuentos del Planeta Tierra


# Function to get the common reviewers using two book's ISBN
common_reviews <- function(book1, book2){
  reviews1 <- subset(mydata, ISBN==book1) # Get the matching datasets where the ISBN matches the first book
  reviews2 <- subset(mydata, ISBN==book2) # Get the matching datasets where the ISBN matches the second book
  reviews_sameset <- intersect(reviews1[,'UserID'], reviews2[,'UserID']) # Return common UserIDs of the two datasets
  if(length(reviews_sameset)==0){
    NA # Do nothing if no common reviewers, NA is just an indicator of missingness
  }
  else{
    reviews_sameset # Return dataset of common reviewers
  }
}

# Test common_reviews using two ISBNs, returns all the same users (UserID) who have reviews of both books
common_reviews('059035342X','043935806X')

# [1]   6563   9908  10560  22625  25919  30735  35148  55492  66942  85367  85993  87938  88435  88733  99720 100227
#[17] 101851 103541 146803 147141 153662 159506 169682 175003 180591 208815 213628 220688 225887 229768 240144 242083
# [33] 242106 247447 252829 267830


book_lookup <- mydata[,c("ISBN", "BookTitle")]
#book_lookup <- book_lookup[duplicated(book_lookup)==FALSE,] # Removes users with duplicate reviews
head(book_lookup)

# Pulls back the ISBN based on the Book-Title
# x$y looks at dataframe x at column y
# subset allows you to select certain amounts of data from a dataframe
common_reviews_by_name <- function(name1, name2){
  #print(head(book_lookup))
  book1 <- subset(book_lookup, BookTitle==name1)$ISBN # Get column of ISBN data for first book
  #print(book1)
  book2 <- subset(book_lookup, BookTitle==name2)$ISBN # Get column of ISBN data for second book
  #print(book2)
  common_reviews(book1,book2)
}

#common_reviews_by_name("Harry Potter and the Sorcerer's Stone (Harry Potter (Paperback))","Harry Potter and the Order of the Phoenix (Book 5)")
#common_reviews_by_name("Harry Potter and the Prisoner of Azkaban (Book 3)","Harry Potter and the Chamber of Secrets (Book 2)")

# Additional test scenarios
common_reviews('0439064864','043935806X')
common_reviews_by_name("Harry Potter and the Chamber of Secrets (Book 2)", "Harry Potter and the Order of the Phoenix (Book 5)")

# Get common reviews for the two ISBNs
# ISBN: 059035342X is 'Harry Potter and the Order of the Phoenix (Book 5)'
# ISBN: 043935806X is 'Harry Potter and the Sorcerer's Stone (Harry Potter(Paperback))
# Returns common reviewers e.g.
#  [1]   6563   9908  10560  22625  25919  30735  35148  55492  66942  85367  85993
#[12]  87938  88435  88733  99720 100227 101851 103541 146803 147141 153662 159506
#[23] 169682 175003 180591 208815 213628 220688 225887 229768 240144 242083 242106
#[34] 247447 252829 267830
common_reviews('059035342X','043935806X')


# Extract the 'BookRating' from a subset of users
# Remove duplicate reviews
myratings <- c("BookRating")
get_review_metrics <- function(book, userset){
  book.data <- subset(mydata, ISBN==book & UserID %in% userset)
  #print(book.data)
  o <- order(book.data$UserID)
  book.data <- book.data[o,]
  dups <- duplicated(book.data$UserID)==FALSE # Remove duplicate user reviews
  book.data <- book.data[dups,]
  #print(book.data)
  book.data[,myratings] # Return BookRating column
}

calc_similarity <- function(b1,b2){
  common_users <- common_reviews(b1,b2)
  print(common_users)
  if (is.na(common_users)){
    return(NA)
  }
  book1.reviews <- get_review_metrics(b1, common_users)
  book2.reviews <- get_review_metrics(b2, common_users)
  print(book1.reviews) #8 10 10 10  8 10 10 10  9 10 10  8 10 10  9 10 10  8  9  6 10  7 10 10 10 10  8 10  9 10 10 10 10 10 10  8
  print(book2.reviews) #10  7 10 10 10 10 10  9  7 10 10  8 10  8  9 10 10  9  8 10 10  8 10 10  7 10  8 10 10 10 10  7 10  9 10  6
  
  #Notes: apply(X, MARGIN, FUN), really to just make a loop
  #Apply returns a vector or array or list of values obtained by applying a function to margins of an array or matrix
  #X is the array, MARGIN is a vector giving the subscripts which the function will be applied over (e.g. Matrix 1 indicates rows, 2 indicadtes columns, c(1,2) indicates rows and columns
  #FUN is the function to be applied

  #cor function gets the correlation coefficient of two variables in a data sample (normalized measurement of how the two are linearly related)
  #cor methods can be pearson (default), spearman, or kendall
  cor(book1.reviews, book2.reviews) 
  #print(cor, na.rm=TRUE)
  
}

b1 <- '059035342X' # Harry Potter and the Sorcerers Stone
b2 <- '043935806X' # Harry Potter and the Order of the Phoenix

calc_similarity(b1,b2)
#[1]  8 10 10 10  8 10 10 10  9 10 10  8 10 10  9 10 10  8  9  6 10  7 10 10 10 10  8 10  9 10 10 10 10 10 10  8
#[1] 10  7 10 10 10 10 10  9  7 10 10  8 10  8  9 10 10  9  8 10 10  8 10 10  7 10  8 10 10 10 10  7 10  9 10  6
# Correlation = 0.2451016

## Now we compare the 20 most commonly reviewed books
## Define the books we want, then we use 'expand.grid' to create all the combinations of books
## Finally we remove any self-to-self comparisons (e.g. Harry Potter and the Sorcerers Stone to Harry Potter and the Sorcerers Stone
## Then we use 'ddply' to do a map/reduce style calculation on the data
## ddply(.data, .variables, .fun) Splits data frame, apply function, and then return results in a data frame
## expand.grid creates a data frame from all combinations of the supplied vectors or factors


book.counts <- ddply(mydata, .(BookTitle), nrow)
o <- order(-book.counts$V1)
#o <- order(book.counts)
#print(o)
# Get the 20 most commonly reviewed books
all.books <- head( book.counts[o,], 20)$BookTitle
print(all.books)
book.pairs <- expand.grid(book1=all.books, book2=all.books)
book.pairs <- subset(book.pairs, book1!=book2) #do not include rating a book with itself
print(book.pairs) # Shows all the book pairings with book1 to book2

## Create function to pass in bookname and get ISBN back
book_name_to_ISBN <- function(mybookname){
  myisbn <- subset(mydata, BookTitle==mybookname, select=c('ISBN')) #select=c('ISBN','BookTitle') for checking ISBN with BookTitle
  uniqueisbn <- unique(myisbn) # e.g. can return multiple rows with multiple ISBNs for same title
  uniqueisbn <- head(uniqueisbn,1) # Return just the first ISBN
  print(head(uniqueisbn,1))
}


## Test case for Books with no intersecting users
#mybook1 <- book_name_to_ISBN("Hornet Flight: A Novel")
#mybook2 <- book_name_to_ISBN("New York Public Library Literature Companion")
## Test case for Books with overlapping users
mybook1 <- book_name_to_ISBN("Harry Potter and the Prisoner of Azkaban (Book 3)")
mybook2 <- book_name_to_ISBN("Harry Potter and the Chamber of Secrets (Book 2)")
calc_similarity(mybook1$ISBN,mybook2$ISBN)
book_name_to_ISBN("Harry Potter and the Chamber of Secrets (Book 2)")


# Pass in book name as mybook1, then converts book name to ISBN using function 'book_name_to_ISBN', returns ISBN
# Then calculates similarity (which calls common reviews function, which returns common reviewers
results <- ddply(book.pairs, .(book1, book2), function(x){
  b1 <- book_name_to_ISBN(x$book1)
  #print(b1)
  b2 <- book_name_to_ISBN(x$book2)
  #print(b2)
  c("sim"=calc_similarity(b1$ISBN,b2$ISBN))
},.progress="text") # To see progress bar in text of how much is left to be completed

print(results) #Shows column 1 (book1's Title), column 2 (book2's Title), column 3 (similarity)

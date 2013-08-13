# Open up library for ODBC connections
library(RODBC)

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
  #print(common_users)
  if (is.na(common_users)){
    return(NA)
  }
  book1.reviews <- get_review_metrics(b1, common_users)
  book2.reviews <- get_review_metrics(b2, common_users)
  weights <- c(1)

  # cor(x, y=NULL, use="everything", method=c("pearson","kendall","spearman"))
  # x = a numeric vector, matrix or data frame
  # 
  #corrs <- sapply(names(book1.reviews), function(metric){
  #  cor(book1.reviews[metric], book2.reviews[metric]) # cor computes the correlation of x and y vectors
  #})
  
  #sum(corrs * weights, na.rm=TRUE)
  #sum(corrs, na.rm=TRUE) # na.rm means excluding missing values from analysis
  #sum(corrs)
}

b1 <- '059035342X'
b2 <- '043935806X'

calc_similarity(b1,b2)
#[1]  8 10 10 10  8 10 10 10  9 10 10  8 10 10  9 10 10  8  9  6 10  7 10 10 10 10  8 10  9 10 10 10 10 10 10  8
#[1] 10  7 10 10 10 10 10  9  7 10 10  8 10  8  9 10 10  9  8 10 10  8 10 10  7 10  8 10 10 10 10  7 10  9 10  6


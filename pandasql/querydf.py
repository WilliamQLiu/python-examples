from pandasql import sqldf

pysqldf = lambda q: sqldf(q, globals())


if __name__ == "__main__":


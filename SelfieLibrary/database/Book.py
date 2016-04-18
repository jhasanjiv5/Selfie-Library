import psycopg2
import sys


con = None

try:
     
    con = psycopg2.connect(database="testdb", user="selfilib", password="12345", host="127.0.0.1", port="5432")     
    
    cur = con.cursor()
  
    cur.execute("CREATE TABLE BookD(Id BIGINT PRIMARY KEY, BookName VARCHAR(60),AuthorName VARCHAR(40),Company VARCHAR(40),Edition INTEGER, Price NUMERIC, IssueDate DATE,ReturnDate DATE)")
    cur.execute("INSERT INTO BookD VALUES(9792345678907,'Options, Futures, And Other Derivatives','John C.Hull','Pearson',8, 80.00, '2016-03-12','2016-04-12')")
    cur.execute("INSERT INTO BookD VALUES(9780670921911,'The First 20 Hours','JoshKaufman','Portfolio Penguin',1, 12.99, '2016-03-12','2016-04-12')")
    cur.execute("INSERT INTO BookD VALUES(65833254,'127 Hours','JoshKaufman','Portfolio Penguin',1, 12.99, '2016-03-12','2016-04-12')")
    
    con.commit()
    

except psycopg2.DatabaseError, e:
    
    if con:
        con.rollback()
    
    print 'Error %s' % e    
    sys.exit(1)
    
    
finally:
    
    if con:
        con.close()

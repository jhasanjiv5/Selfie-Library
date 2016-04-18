import psycopg2
import sys


con = None

try:
     
    con = psycopg2.connect(database="testdb", user="selfilib", password="12345", host="127.0.0.1", port="5432")   
    
    cur = con.cursor()
  
    cur.execute("CREATE TABLE Studentdata(Id INTEGER PRIMARY KEY, FName VARCHAR(20),LName VARCHAR(20), BookId BIGINT)")
    cur.execute("INSERT INTO Studentdata VALUES(1,'Geeta','Parangi',9780273759072)")
    cur.execute("INSERT INTO Studentdata VALUES(2,'Katyayani','Singh',9780670921911)")
    cur.execute("INSERT INTO Studentdata VALUES(3,'Sanjiv','Jha',9780670921911)")
    
    con.commit()
    

except psycopg2.DatabaseError, e:
    
    if con:
        con.rollback()
    
    print 'Error %s' % e    
    sys.exit(1)
    
    
finally:
    
    if con:
        con.close()

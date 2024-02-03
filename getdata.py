import pymysql
import pandas as pd

con = pymysql.connect(host='localhost', user='root', passwd='98Naturena!!', charset='utf8')
cur = con.cursor()
cur.execute('create database AccommodationDB character set utf8')
cur.execute('use AccommodationDB')

# get document
df = pd.read_excel("data/Public-List-of-Accreditation_8.xlsx")
sqlSentence1 = 'create table Accommodation(Id VARCHAR(255), Accreditation_Number VARCHAR(255), Number_of_Beds VARCHAR(255), Email VARCHAR(255), Cell_Number VARCHAR(255), Street_Address VARCHAR(255), Nearest_Campus VARCHAR(255), Residence_Name VARCHAR(255))'
cur.execute(sqlSentence1)

# Get the length of the document
length = len(df)
for i in range(0, length):
    # data conversion character type
    record = tuple(None if pd.isna(value) else value for value in df.loc[i])  # Replace NaN values with None
    # insert table data
    sqlSentence = "INSERT INTO Accommodation(Id, Accreditation_Number, Number_of_Beds, Email, Cell_Number, Street_Address, Nearest_Campus , Residence_Name) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
    cur.execute(sqlSentence, record)
 
# end, close
cur.close()
con.commit()
con.close()

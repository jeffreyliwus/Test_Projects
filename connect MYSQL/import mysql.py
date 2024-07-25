import mysql.connector

myDB = mysql.connector.connect(
    host="localhost", user="root", passwd="Jeff032587!", database="pythonxtest"
)
myCur = myDB.cursor()
# myCur.execute("CREATE TABLE user(userID int PRIMARY KEY, username varchar(10), email varchar(25), userType varchar(10))")
# create table

myCur.execute('INSERT INTO user VALUES (1251, "Smith", "smith@example.com", "REGULAR")')
# make changes in the database
myDB.commit()
myCur.execute("SELECT * FROM user")
result = myCur.fetchall()
for i in result:
    print(i)
myDB.close()

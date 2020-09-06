import mysql.connector

con = mysql.connector.connect(
user = "ardit700_student",
password = "ardit700_student",
host = "108.167.140.122",
database = "ardit700_pm1database"
)

cursor = con.cursor()

#word = input('enter a word: ')

query = cursor.execute("SELECT * FROM Dictionary WHERE length(Expression) < 4")
results = cursor.fetchall()
if results:
    for result in results:
        print(result[0])
        print('-'*10)
else:
    print('no entry found')

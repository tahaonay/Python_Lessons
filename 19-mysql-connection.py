import mysql.connector 
# Authentication plugin 'caching_sha2_password' is not supported hatası verirse
# pip install mysql-connector-python

mydb = mysql.connector.connect(
    host ="localhost", #192......  internetten alınırsa
    user ="root",
    password ="12345678",
    database = "node-app"
)

mycursor = mydb.cursor()

# ---Database oluşturma
# mycursor.execute("CREATE DATABASE mydatabase")

# ---Database görüntüleme
# mycursor.execute("SHOW DATABASES")
# for i in mycursor:
#     print(i)

# ---tABLO OLUŞTURMA
# mycursor.execute("CREATE TABLE customers (name VARCHAR(255), adress VARCHAR(255))")


print(mydb)
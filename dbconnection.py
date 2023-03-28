import mysql.connector

class dbconnection:

    def getconnection(self):
        dbconnection=mysql.connector.connect(
                host='localhost',
                user='root',
                password='Omni2343$',
                database='bkp'
                )
        return dbconnection

#dbconnection().getconnection()
#print(dbconnection)

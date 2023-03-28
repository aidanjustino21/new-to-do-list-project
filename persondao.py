import mysql.connector
from dbconnection import dbconnection

class persondao:

    def insertperson(self,person):

        #get the connection
        dbconn = dbconnection().getconnection()
        #print(dbconn)

        #get the cursor

        cursor = dbconn.cursor()

        #create the statement

        statement = '''insert into person_table (person_name, address_id) values (%s,%s)'''
        #excute the query

        cursor.execute(statement,person)

        #commit the transaction
        dbconn.commit()

        #close the cursor
        cursor.close()

        #close the connection
        dbconn.close()




    def selectpersonlist(self):

        #get the connection
        dbconn = dbconnection().getconnection()
        print(dbconn)

        #get the cursor
        cursor = dbconn.cursor()

        #create the statement

        statement = '''select *  from person_table'''

        #excute the query

        cursor.execute(statement)

        #get the result from the cursor
        result = cursor.fetchall()

        for r in result:
            print(r)

        #close the cursor
        cursor.close()

        #close the connection
        dbconn.close()



#person_table = ['John','1']
#p = persondao()
#p.insertperson(person_table)
#p.selectpersonlist()

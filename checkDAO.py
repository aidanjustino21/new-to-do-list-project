from dbconnection import DBconnection

class CheckDAO:

    def insertCheck(self, listCheck):
        print('Print from Insert Operation')
        dbconnection = DBconnection()
        connection =dbconnection.getConnection()
        cursor = connection.cursor()
        statement =''' insert into sample (datetime, person_id) values (%s,%s)'''
        cursor.execute(statement, listCheck)
        connection.commit()
        print('Check Insert Operation Successfully Completed')
        cursor.close()
        connection.close()

    def selectCheck(self):
        print('Print from Select Operation')
        dbconnection = DBconnection()
        connection = dbconnection.getConnection()
        cursor = connection.cursor()
        statement = '''select * from sample'''
        cursor.execute(statement)
        result = cursor.fetchall()

        for r in result:
            print(r)

        print('Check Select Operation Successfully Completed')
        cursor.close()
        connection.close()

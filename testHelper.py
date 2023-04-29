import csv
from checkDAO import CheckDAO

class TestHelper:

    def readCsvFile(self):

        file = open('aidan.csv', mode = 'r')
        csvfile = csv.reader(file)
        return csvfile

    def insertCsvFile(self):

        file = self.readCsvFile()

        checkdao =CheckDAO()

        for csvlist in file:
            checkdao.insertCheck(csvlist)
        checkdao.selectCheck()

testhelper = TestHelper()
testhelper.insertCsvFile()

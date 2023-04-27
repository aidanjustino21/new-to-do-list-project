import csv

class Test:

    def readCsvFile(self):

        file = open('entrytime-aiden.csv', mode = 'r')
        csvfile = csv.reader(file)

        for cf in csvfile:
            print(cf)

test = Test()
test.readCsvFile()



import csv
from persondao import persondao

class personhelper:

    def insertpersonlist(self):
        print('person list insert')

        ctdao = persondao()
        personlist=self.readpersoncsv()

        for list in personlist:
            ctdao.insertperson(list)

        ctdao.selectpersonlist()

    def readpersoncsv(self):
        print("program started")
        fileref = open('person.csv','r')
        csvfile = csv.reader(fileref)
        return csvfile


ch=personhelper()
ch.insertpersonlist()

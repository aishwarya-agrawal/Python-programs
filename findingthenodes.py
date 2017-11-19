from xml.dom.minidom import parse
import csv
class Proc(object):
    def __init__(self,dom1,file):
        self._dom1=dom1
        self._file=file
    def processing(self,output):
        check = self._file.readlines()
        check = [name.rstrip('\n') for name in check]
        headers = self._dom1.getElementsByTagName("Header")
        for header in headers:
            conf_name = header.getAttribute("name")
            nodes = header.getElementsByTagName("Node")
            nodename = list()
            output.write(conf_name + "                   status \n")
            for node in nodes:
                text = node.getAttribute("name")
                nodename.append(text)
            for name in check:
                if name in nodename:
                    output.write(name + "                              found \n")
                else:
                    output.write(name + "                              not found \n")
            output.write("\n\n")
        output.close()
    def checkcsv(self,file):
        with open(file) as f:
            csvfile = csv.reader(f,delimiter=",")
            for row in csvfile:
                if row[2]=="Set point" or row[2]== "Set Point":
                    print(row[0]+"           0           "+row[2]+"\n")




def main():
    dom1=parse("big.xml")
    file= open("mandatory_headers.txt")
    output = open("output.txt","w")
    check = Proc(dom1,file)
    check.processing(output)
    #csv1 = csv.reader("schema.csv")
    check.checkcsv("schema.csv")


if __name__ == "__main__" :
    main()



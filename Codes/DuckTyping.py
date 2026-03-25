# Duck Typing : It is concept where the type of an object is determined
# by it's behaviour , not by it's class

class InkjetPrinter:
    def printdocument(self,document):
        print("Inkjet Printer Printing :",document)

class LaserPrinter:
    def printdocument(self,document):
        print("Laser Printer Printing :",document)

class PDFWriter:
    def printdocument(self,document):
        print(f"Saving {document} as PDF")

def StartPrinting(Device):
    Device.printdocument("Marvellous Notes")

def main():
    StartPrinting(InkjetPrinter()) 
    StartPrinting(LaserPrinter())    
    StartPrinting(PDFWriter()) 

main()    
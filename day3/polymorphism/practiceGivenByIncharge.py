class excelReport:
    def generate(self):
        print("generating excel report")
class pdfReport:
    def generate(self):
        print("generating pdf report")
        
excel=excelReport()
pdf=pdfReport()

excel.generate()
pdf.generate()
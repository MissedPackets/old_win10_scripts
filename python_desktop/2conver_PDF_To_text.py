import PyPDF2
 
pdfFileObject = open(r"C:\Users\jellycat\Downloads\Sylvan Barnet_ Hugo Bedau_ John O’Hara - Current Issues and Enduring Questions-Bedford_St. Martin’s (2016).pdf", 'rb')
 
pdfReader = PyPDF2.PdfFileReader(pdfFileObject)
 
print(" No. Of Pages :", pdfReader.numPages)

for i in range(0,1052-1):
    #print(i)
    pageObject = pdfReader.getPage(i)
    f = open("pdf_text.txt", "a", encoding='utf-8')
    f.write(pageObject.extractText())
    f.close()
    #print(pageObject.extractText())
 
pdfFileObject.close()
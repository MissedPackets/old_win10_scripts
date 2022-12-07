import PyPDF2
 
pdfFileObject = open(r"C:\Users\jellycat\Downloads\Eric Foner - Give Me Liberty!_ An American History, Third edition-W. W. Norton & Company Limited (2010).pdf", 'rb')
 
pdfReader = PyPDF2.PdfFileReader(pdfFileObject)
 
print(" No. Of Pages :", pdfReader.numPages)

for i in range(0,1389-1):
    #print(i)
    pageObject = pdfReader.getPage(i)
    f = open("2pdf_text.txt", "a", encoding='utf-8')
    f.write(pageObject.extractText())
    f.close()
    #print(pageObject.extractText())
 
pdfFileObject.close()
from PyPDF2 import PdfFileMerger
from PyPDF2 import PdfFileReader
merger = PdfFileMerger()
for f in ['Untitled_document.pdf', 'ya.pdf']:
    merger.append(PdfFileReader(f), 'rb')
with open('finished_copy.pdf', 'wb') as new_file:
    merger.write(new_file)
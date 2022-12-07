from PyPDF2 import PdfFileMerger
from PyPDF2 import PdfFileReader
merger = PdfFileMerger()
for f in ['1.pdf', '2.pdf']:
    merger.append(PdfFileReader(f), 'rb')
with open('finished_copy.pdf', 'wb') as new_file:
    merger.write(new_file)
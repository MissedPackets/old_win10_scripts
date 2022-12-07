from PyPDF2 import PdfFileMerger
from PyPDF2 import PdfFileReader
merger = PdfFileMerger()


import glob

#lets me pick which page i want to read


import os
#print(glob.glob(r"C:\Users\jellycat\.spyder-py3\*"))#this prints entire directory's files

img_path=(glob.glob(r'*'))
print(img_path)

for pg_num in range(10):
    for f in (img_path[pg_num],img_path[pg_num]):
        merger.append(PdfFileReader(f), 'rb')
    with open('finished_copy.pdf', 'ab') as new_file:
        merger.write(new_file)
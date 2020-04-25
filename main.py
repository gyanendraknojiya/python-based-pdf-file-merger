import PyPDF2
import sys

source_file = PyPDF2.PdfFileReader(sys.argv[1], 'rb')

watermark_file = PyPDF2.PdfFileReader(sys.argv[2], 'rb')
output = PyPDF2.PdfFileWriter()
number_page = source_file.getNumPages()
for i in range(number_page):
    page = source_file.getPage(i)
    page.mergePage(watermark_file.getPage(0))
    output.addPage(page)
#dhukyo
with open('wmfile.pdf', 'wb') as file:
    output.write(file)
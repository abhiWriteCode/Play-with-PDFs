from PyPDF2 import PdfFileWriter, PdfFileReader


output = PdfFileWriter()
input1 = PdfFileReader(open("pdfs/file1.pdf", "rb"))
input2 = PdfFileReader(open("pdfs/file2.pdf", "rb"))

n_page = input1.getNumPages()
print(n_page)
page1 = input1.getPage(n_page-1)
output.addPage(page1)

n_page = input2.getNumPages()
page2 = input2.getPage(n_page-1)
output.addPage(page2)

outputStream = open("PyPDF2-output.pdf", "wb")
output.write(outputStream)

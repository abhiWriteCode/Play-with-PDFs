from PyPDF2 import PdfFileMerger


merger = PdfFileMerger()

input1 = open("pdfs/file1.pdf", "rb")
input2 = open("pdfs/file2.pdf", "rb")

# add the first 3 pages of input1 document to output
n_page = input1.getNumPages()
pages = (n_page-2, n_page-1)
merger.append(fileobj = input1, pages = pages)

# insert the first page of input2 into the output beginning after the second page
n_page = input1.getNumPages()
pages = (n_page-2, n_page-1)
merger.merge(position = 2, fileobj = input2, pages = (0,1))

# Write to an output PDF document
output = open("document-output.pdf", "wb")
merger.write(output)
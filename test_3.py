from PyPDF2 import PdfFileWriter, PdfFileReader
from glob import glob


dir_name = 'pdfs'
output_filename = 'weekly.pdf'
output = PdfFileWriter()


# for filename in glob(f'{dir_name}/*.pdf'):  # Not working
# 	with open(filename, "rb") as fp:
# 		input_stream = PdfFileReader(fp)
# 		n_page = input_stream.getNumPages()
# 		page = input_stream.getPage(n_page-1)
# 		output.addPage(page)


for filename in glob(f'{dir_name}/*.pdf'):
	fp = open(filename, "rb")
	input_stream = PdfFileReader(fp)
	n_page = input_stream.getNumPages()
	page = input_stream.getPage(n_page-1)
	output.addPage(page)


with open(output_filename, "wb") as fp:
	output.write(fp)

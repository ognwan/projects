#Trying to create my own PDF reader. But it is still a work in progress
import PyPDF2
import sys


def main_function():
	
	msg = '''
        Choose from the option listed:
        [1] - Combine pdf
        [2] - Merge PDF

    '''
	selected = input(msg)
	validate_selection = True
	while True:
		
		if selected == "1":
			print("you selected number " + selected)
			inputs = input("Please enter each individual file path separated by comma: ")
			x = inputs.split(",")[1]
			pdf_combiner(x)
		elif selected == "2":
			print("you selected number " + selected)
			inputs = input("Please Enter the watermark file followed by the file to watermark (separated by comma): ")
			watermark_file, input_file = inputs.split(".")[0], inputs.split(".")[1]
			pdf_watermark(watermark_file, input_file)
		else:
			print("invalid selection. Please try again!")
			validate_selection = False
			selected = input(msg)
def pdf_combiner(files):
    merger = PyPDF2.PdfFileMerger()
    for pdf in files:
        merger.appendfiles(pdf)
    merger.write(f'{files[0]}_1.pdf')

def pdf_watermark(watermark_file, input_file):
	
	watermark = PyPDF2.PdfFileReader(watermark_file)
	reader = PyPDF2.PdfFileReader(input_file)

	watermark_page = watermark.getPage(0)
	writer = PyPDF2.PdfFileWriter()

	for page in reader.pages:
		page.mergePage(watermark_page)
		writer.addPage(page)

	with open("output_file.pdf", "wb") as new_file:
	    writer.write(new_file)

main_function()

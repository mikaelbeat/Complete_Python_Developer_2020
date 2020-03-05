
import PyPDF2, os, sys

data_directory = ".\\Data\\"

pdf_file = sys.argv[1]


def pdf_watermarker(pdf_file):
    input_pdf = PyPDF2.PdfFileReader(open(data_directory + pdf_file, "rb"))
    watermark = PyPDF2.PdfFileReader(open(data_directory + "watermark.pdf", "rb"))
    output = PyPDF2.PdfFileWriter()

    for i in range(input_pdf.getNumPages()):
        page = input_pdf.getPage(i)
        page.mergePage(watermark.getPage(0))
        output.addPage(page)

        with open(data_directory + "watermarked_pdf.pdf", "wb") as file:
            output.write(file)

pdf_watermarker(pdf_file)
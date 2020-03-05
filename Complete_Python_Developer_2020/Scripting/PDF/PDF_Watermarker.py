
import PyPDF2, os, sys

data_directory = ".\\Data\\"

pdf_file = data_directory + sys.argv[1]
watermark = data_directory + "watermark.pdf"


def pdf_watermarker(pdf_file):
    input_file = open(pdf_file, "rb")
    input_pdf = PyPDF2.PdfFileReader(pdf_file)

    watermark_file = open(watermark, "rb")
    watermark_pdf = PyPDF2.PdfFileReader(watermark_file)

    pdf_page = input_pdf.getPage(0)
    watermark_page = watermark_pdf.getPage(0)
    pdf_page.mergePage(watermark_page)

    output = PyPDF2.PdfFileWriter()
    output.addPage(pdf_page)

    merged_file = open(data_directory + "watermarked.pdf", "wb")
    output.write(merged_file)

    merged_file.close()
    watermark_file.close()
    input_file.close()

pdf_watermarker(pdf_file)
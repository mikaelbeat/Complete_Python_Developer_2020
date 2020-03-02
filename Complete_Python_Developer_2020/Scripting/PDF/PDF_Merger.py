
import PyPDF2, os, sys


pdf_files = sys.argv[1:]


data_directory = ".\\Data\\"


def pdf_merger(pdf_list):
    merger = PyPDF2.PdfFileMerger()
    for pdf in pdf_files:
        print(pdf)
        merger.append(data_directory + pdf)
    merger.write(data_directory + "Super.pdf")

pdf_merger(pdf_files)

import PyPDF2, os

data_directory = ".\\Scripting\\PDF\\Data\\"
data_file = "dummy.pdf"

# "rb" -> Read binary need to be used for reading pdf files in binary mode

with open(data_directory + data_file, "rb") as file:
    reader = PyPDF2.PdfFileReader(file)
    print(f"Number of pages in PDF file {data_file} is {reader.numPages}.")

    page = reader.getPage(0)
    page.rotateCounterClockwise(90)

    writer = PyPDF2.PdfFileWriter()
    writer.addPage(page)

    with open(data_directory + "tilted.pdf", "wb") as new_file:
        writer.write(new_file)

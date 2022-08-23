import PyPDF2
import os
import sys

os.chdir("PDFs")

name = input("File name of merged PDF: ") + ".pdf"

fileMerger = PyPDF2.PdfFileMerger()

for file in os.listdir(os.curdir):
    if file.endswith(".pdf"):
        fileMerger.append(file)
        os.remove(file)

fileMerger.write(name)
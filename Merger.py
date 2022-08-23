import PyPDF2
import os
import sys

os.chdir("PDFs")                                    # changes current directory to "PDFs" folder

name = input("File name of merged PDF: ") + ".pdf"  # file name input

fileMerger = PyPDF2.PdfFileMerger()                 # creates new PdfFileMerger object

for file in os.listdir(os.curdir):                  # iterates through files in current directory ("PDFs" folder)
    if file.endswith(".pdf"):
        fileMerger.append(file)                     # appends file to PdfFileMerger object
        os.remove(file)                             # removes file from "PDFs" folder

fileMerger.write(name)                              # writes PdfFileMerger object to PDF with inputted file name
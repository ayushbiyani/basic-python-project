import PyPDF2

merger = PyPDF2.PdfMerger()

pdfFiles = ["1.pdf" , "2.pdf"]

for pdf_file in pdfFiles :
    merger.append(pdf_file)

merger.write("merged.pdf")
merger.close()
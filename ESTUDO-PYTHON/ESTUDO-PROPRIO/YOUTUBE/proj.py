import PyPDF2, os

merger = PyPDF2.PdfMerger()
lista_de_arquivos = os.listdir("ESTUDO-PYTHON")
lista_de_arquivos.sort()
print(lista_de_arquivos)

for arquivo in lista_de_arquivos:
    if ".pdf" in arquivo:
        merger.append(f"ESTUDO-PYTHON/{arquivo}")
merger.write("PDFfinal.pdf")

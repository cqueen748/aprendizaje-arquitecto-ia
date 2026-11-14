archivos = [
    "contrato.pdf",
    "acta.docx",
    "anexo.PDF",
    "informe.docx",
    "resolucion.pdf"
]
contador = {"pdf": 0, "docx": 0}

for extension in archivos:
    if extension.lower().endswith(".pdf"):
        contador["pdf"] = contador["pdf"] + 1
    if extension.lower().endswith(".docx"):
        contador["docx"] = contador["docx"] + 1

print("contador de Archivos PDF:", contador["pdf"])
print("contador de Archivos DOCX:", contador["docx"])
print("total de Archivos:", len(archivos))


documento = {"nombre": "Contratos.pdf", "extension": ".pdf","tamaño": 250}
print(documento["extension"])
print(documento["tamaño"] + 10)
print(documento["tamaño"])

# Ejercicio 2: contador de pdfs
archivos = ["Contratos.pdf","acta.pdf","informe.docx"]
conteo={"pdf": 0}
for nombre in archivos:
    if nombre.endswith(".pdf"):
        conteo["pdf"] = conteo["pdf"] + 1   

print("Contador de PDFs:", conteo["pdf"])

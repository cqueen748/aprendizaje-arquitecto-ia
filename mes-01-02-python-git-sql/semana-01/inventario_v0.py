from pathlib import Path

carpeta = Path(r"C:\Users\CREINA\CRAI-OS\lab\aprendizaje-arquitecto-ia\datos\expediente_prueba")
total_pdf = {".pdf": 0,}

for elemento in carpeta.rglob("*"):
    if elemento.is_file() and elemento.suffix.lower() == ".pdf":
        print(elemento.name, elemento.stat().st_size)
        total_pdf[".pdf"] += 1
print("Total de PDF:", total_pdf[".pdf"])


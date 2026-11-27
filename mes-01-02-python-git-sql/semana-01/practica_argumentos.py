import sys
from pathlib import Path

if len(sys.argv) != 2:
    print("Debes Indicar Una Carpeta Como argumento")
    sys.exit(1)

carpeta = Path(sys.argv[1])

if not carpeta.is_dir():
    print("La carpeta no existe o no es una carpeta")
    sys.exit(1)
print(f"Se encontró la carpeta: {carpeta}")


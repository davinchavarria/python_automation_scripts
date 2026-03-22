import pandas as pd
import os
import sys

if len(sys.argv) < 2:
    print("Uso: python main.py <ruta_carpeta>")
    exit()

folder_path = sys.argv[1]

if not os.path.exists(folder_path):
    print("❌ La carpeta no existe")
    exit()

print("🔄 Procesando archivos...")

all_data = []

for file in os.listdir(folder_path):
    if file.endswith(".xlsx"):
        file_path = os.path.join(folder_path, file)
        print(f"📄 Leyendo: {file}")
        try:
            df = pd.read_excel(file_path)
            all_data.append(df)
        except Exception as e:
            print(f"Error leyendo {file}: {e}")


if not all_data:
    print("❌ No se encontraron archivos Excel en la carpeta")
    exit()

merged_data = pd.concat(all_data, ignore_index=True)

output_file = "merged_output.xlsx"
merged_data.to_excel(output_file, index=False)

print(f"✅ Archivos combinados en {output_file}")

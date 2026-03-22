import pandas as pd
import os

folder_path = "input_excels"

if not os.path.exists(folder_path):
    print("❌ La carpeta 'input_excels' no existe")
    exit()

all_data = []

for file in os.listdir(folder_path):
    if file.endswith(".xlsx"):
        file_path = os.path.join(folder_path, file)
        print(f"📄 Leyendo: {file}")
        df = pd.read_excel(file_path)
        all_data.append(df)

if not all_data:
    print("❌ No se encontraron archivos Excel en la carpeta")
    exit()

merged_data = pd.concat(all_data, ignore_index=True)

output_file = "merged_output.xlsx"
merged_data.to_excel(output_file, index=False)

print(f"✅ Archivos combinados en {output_file}")

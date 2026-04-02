import pandas as pd
import sys


# Archivo de entrada(Usuario elige el archivo)

if len(sys.argv) < 2:
    print("❌ Uso: python main.py <archivo.xlsx>")
    exit()

input_file = sys.argv[1]

# Archivo de salida
output_file = "cleaned_output.xlsx"

print("📥 Leyendo archivo...")
df = pd.read_excel(input_file)

print("🧹 Limpiando datos...")

# Eliminar filas completamente vacías
df = df.dropna(how='all')

# Eliminar duplicados
df = df.drop_duplicates()

print("💾 Guardando archivo limpio...")
df.to_excel(output_file, index=False)

print("✅ Proceso completado")

import pandas as pd
import sys
import os

if len(sys.argv) < 2:
    print("❌ Uso: python main.py <archivo.xlsx> [salida.xlsx]")
    exit()

input_file = sys.argv[1]

if not os.path.exists(input_file):
    print("❌ El archivo no existe")
    exit()

if len(sys.argv) >= 3:
    output_file = sys.argv[2]
else:
    output_file = "cleaned_" + input_file

print("📥 Leyendo archivo...")

try:
    df = pd.read_excel(input_file)
except Exception as e:
    print("❌ Error al leer archivo:", e)
    exit()

print("🧹 Limpiando datos...")

df = df.dropna(how='all')
df = df.drop_duplicates()

df = df.apply(lambda col: col.map(lambda x: x.strip() if isinstance(x, str) else x))

print(f"📊 Filas finales: {len(df)}")
print(f"📊 Columnas: {len(df.columns)}")

print("💾 Guardando archivo limpio...")

try:
    df.to_excel(output_file, index=False)
except Exception as e:
    print("❌ Error al guardar:", e)
    exit()

print(f"✅ Archivo generado: {output_file}")

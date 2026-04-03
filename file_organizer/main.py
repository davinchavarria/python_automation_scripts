import os
import shutil
import sys

if len(sys.argv) < 2:
    print("❌ Uso: python main.py <carpeta>")
    exit()

folder_path = sys.argv[1]

if not os.path.exists(folder_path):
    print("❌ La carpeta no existe")
    exit()

print("📂 Organizando archivos...")

# Tipos de archivos
file_types = {
    "imagenes": [".jpg", ".png", ".jpeg"],
    "pdf": [".pdf"],
    "musica": [".mp3"],
    "videos": [".mp4"],
    "otros": []
}

for file in os.listdir(folder_path):
    file_path = os.path.join(folder_path, file)

    if os.path.isfile(file_path):
        moved = False

        for folder_name, extensions in file_types.items():
            if any(file.endswith(ext) for ext in extensions):
                target_folder = os.path.join(folder_path, folder_name)
                os.makedirs(target_folder, exist_ok=True)

                shutil.move(file_path, os.path.join(target_folder, file))
                print(f"📁 {file} → {folder_name}")
                moved = True
                break

        if not moved:
            target_folder = os.path.join(folder_path, "otros")
            os.makedirs(target_folder, exist_ok=True)
            shutil.move(file_path, os.path.join(target_folder, file))
            print(f"📁 {file} → otros")

print("✅ Organización completa")

import os
import shutil
from tkinter import Tk, filedialog

# Ocultar ventana principal
root = Tk()
root.withdraw()

# Seleccionar carpeta
folder_path = filedialog.askdirectory(title="Selecciona una carpeta")

if not folder_path:
    print("❌ No se seleccionó carpeta")
    exit()

print("📂 Organizando archivos...")

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
                moved = True
                break

        if not moved:
            target_folder = os.path.join(folder_path, "otros")
            os.makedirs(target_folder, exist_ok=True)
            shutil.move(file_path, os.path.join(target_folder, file))

print("✅ Organización completa")

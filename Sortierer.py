# Dieses Programm erstellt drei Ordner ("Bilder", "Dokumente" und "Rest") im Download-Verzeichnis des Benutzers,
# falls sie noch nicht existieren. Es sucht dann alle Dateien im Download-Verzeichnis und verschiebt sie in den
# entsprechenden Ordner basierend auf ihrem Dateityp.
# Kann beliebig angepasst werden. Gegebenenfalls src_folder ersetzen.

import os
import shutil

try:
    src_folder = os.path.expanduser("~\Downloads") # src_folder = "C:\\Anderer\Pfad"

    image_folder = os.path.join(src_folder, "Bilder")
    txt_folder = os.path.join(src_folder, "Dokumente")
    other_folder = os.path.join(src_folder, "Rest")

    if not os.path.isdir(image_folder):
        os.makedirs(image_folder)

    if not os.path.isdir(txt_folder):
        os.makedirs(txt_folder)

    if not os.path.isdir(other_folder):
        os.makedirs(other_folder)

    image_files = []
    txt_files = []
    other_files = []

    for filename in os.listdir(src_folder):
        if os.path.isfile(os.path.join(src_folder, filename)):
            if filename.lower().endswith((".jpg", ".jpeg", ".png", ".gif")):
                image_files.append(filename)
                shutil.move(os.path.join(src_folder, filename), os.path.join(image_folder, filename))
            elif filename.lower().endswith((".txt", ".doc", ".pdf")):
                txt_files.append(filename)
                shutil.move(os.path.join(src_folder, filename), os.path.join(txt_folder, filename))
            else:
                other_files.append(filename)
                shutil.move(os.path.join(src_folder, filename), os.path.join(other_folder, filename))

    print(f"{len(image_files)} Bilddateien wurden in den Ordner '{image_folder}' verschoben.")
    print(f"{len(txt_files)} Textdateien wurden in den Ordner '{txt_folder}' verschoben.")
    print(f"{len(other_files)} andere Dateien wurden in den Ordner '{other_folder}' verschoben.")

except Exception as e:
    print(f"Ein Fehler ist aufgetreten: {e}")

input("Enter!")

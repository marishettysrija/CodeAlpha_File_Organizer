import os
import shutil

source_folder = "source_folder"
destination_folder = "destination_folder"

files_moved = 0

for filename in os.listdir(source_folder):

    if filename.lower().endswith(".jpg"):

        source_path = os.path.join(source_folder, filename)
        destination_path = os.path.join(destination_folder, filename)

        shutil.move(source_path, destination_path)

        print(f"Moved: {filename}")

        files_moved += 1

print("\nTask Completed!")
print(f"Total JPG files moved: {files_moved}")
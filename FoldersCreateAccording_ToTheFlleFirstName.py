import os
import shutil

path = input("Enter the path: ")
files = os.listdir(path)

for file in files:

    if os.path.isdir(os.path.join(path, file)):
        continue

    filename, extension = os.path.splitext(file)
    
    second_letter = filename[2].lower() if len(filename) > 1 else None

    if second_letter and second_letter.isalpha():  
        target_folder = os.path.join(path, second_letter)
    else:
        target_folder = os.path.join(path, "others")  
    unique_folder = os.path.join(target_folder, filename)

    if not os.path.exists(unique_folder):
        os.makedirs(unique_folder)

    # Move the file to its unique folder
    shutil.move(os.path.join(path, file), os.path.join(unique_folder, file))
    print(f"Moved {file} to {unique_folder}")


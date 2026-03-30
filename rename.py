import json
import os
import glob

files = glob.glob('complex_*')

for file in files:
    try:
        with open(file, 'r') as f:
            d = json.load(f)
            for k, v in d.items():
                if k == "unique_id":
                    df = d[k]
                    new_name = df[0:4]  # Extract the first 4 characters from 'unique_id'
                    new_file_path = os.path.join(os.path.dirname(file), new_name)
                    os.rename(file, new_file_path)
                    print(f"Renamed {file} to {new_file_path}")
                else:
                    pass
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON in file {file}: {e}")
    except OSError as e:
        print(f"Error renaming file {file}: {e}")
def add_extension_to_non_py_files(folder_path):
    # Check all files in folder
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)

        # Check if it is a file, if not a folder, continue
        if os.path.isfile(file_path):
            # Check if it is a file with .py extension
            if not filename.endswith('.py'):
                # If not with .py extension, add .txt suffix
                new_file_path = file_path + '.txt'
                os.rename(file_path, new_file_path)
                print(f"Added '.txt' suffix to '{filename}' file.")

# Specify folder path without enclosing in extra quotes
folder_path = '/YOUR PATH/CAMEO/example2026.02.21/result/'

# Call function
add_extension_to_non_py_files(folder_path)


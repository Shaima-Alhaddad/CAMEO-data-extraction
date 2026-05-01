import json
import os
import glob

# --- Part 1: Rename JSON files based on "unique_id" ---

files = glob.glob('complex_*')

for file in files:
    try:
        with open(file, 'r') as f:
            data = json.load(f)

        if "unique_id" in data:
            unique_id = data["unique_id"]
            new_name = unique_id[:4]  # first 4 characters

            # rename to .json first (same as your logic)
            new_file_path = os.path.join(os.path.dirname(file), new_name + ".json")

            os.rename(file, new_file_path)
            print(f"Renamed {file} → {new_file_path}")

    except json.JSONDecodeError as e:
        print(f"JSON error in {file}: {e}")
    except OSError as e:
        print(f"Rename error for {file}: {e}")


# --- Part 2: Fix extensions → ensure ONLY .txt remains ---

def add_extension_to_non_py_files(folder_path):
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)

        if os.path.isfile(file_path) and not filename.endswith('.py'):

            # remove ALL extensions (handles .json, .json.txt, etc.)
            base_name = file_path
            while True:
                base_name_no_ext = os.path.splitext(base_name)[0]
                if base_name_no_ext == base_name:
                    break
                base_name = base_name_no_ext

            new_file_path = base_name + '.txt'

            # avoid renaming if already correct
            if file_path != new_file_path:
                os.rename(file_path, new_file_path)
                print(f"Fixed → {filename} → {os.path.basename(new_file_path)}")


# --- Use Linux-style path ---
folder_path = "/Yourpath/CAMEO/example2026.04.18/result"

add_extension_to_non_py_files(folder_path)


# CAMEO Data Extraction and Renaming

This repository provides a Python script to extract and rename files from downloaded CAMEO website: https://cameo3d.org/downloads 

---

## 📂 Folder Structure

Place the **extract.py** script in the same directory as your downloaded CAMEO folder:
Create a folder name "result" inside the "example 2026.02.21 folder" 
place the **rename.py** script in the result folder

```
CAMEO folder
│
├ extract.py file
│
└ example 2026.02.21 folder
    │
    ├── target1 file
    ├── target2 file
    │
    ├── result folder
          └── rename.py file
```

---

## 🔧 Modifications Setup

Open the scripts and modify the files locattions

```python
source_directory = '/YOUR PATH/CAMEO/example2026.02.21/*/servers/server5/model-1/scores/'
destination_directory = '/YOUR PATH/CAMEO/example2026.02.21/result/'
```

Replace `/YOUR PATH/` with your actual system path.

### Examples

#### macOS

```python
destination_directory = '/Users/yourname/Desktop/CAMEO/example2026.02.21/result/'
```

#### Windows

```python
destination_directory = 'C:/Users/YourName/Desktop/CAMEO/example2026.02.21/result/'
```

#### Linux

```python
destination_directory = '/home/yourname/CAMEO/example2026.02.21/result/'
```

---


Note:
**In the extract.py file**

```bash
Edit the script to specify the server number that you wish to extract.
Replace the server# with the server number such as /server5/, without space.

source_directory = '/YOUR PATH/CAMEO/example2026.02.21/*/servers/server#/model-1/scores/'
```

```bash
The second line should be the path of the result folder

destination_directory = '/YOUR PATH/CAMEO/example2026.02.28/result/'
```


Note:
**In the rename.py file**
Replace the folder path to your result folder path

```bash
folder_path = '/YOUR PATH/CAMEO/example2026.02.28/result/'
```

---

## ▶️ Usage
**Run the scripts from the terminal ensuring the script path location is set in the terminal before calling the scripts.**

```bash
# For extracting the file from CAMEO folder
python3 extract.py    

```

```bash
 # For renaming the files based on their PDB ID
python3 rename.py    

```

---



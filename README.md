
# CAMEO Data Extraction and Renaming

This repository provides a Python script to extract and rename files from downloaded CAMEO website: https://cameo3d.org/downloads 

---

## 📂 Folder Structure

Place the **extract.py** script in the same directory as your downloaded CAMEO folder:
Create a foulder name "result" inside the "example 2026.02.21 foulder" 
place the **rename.py** script in the result foulder

```
CAMEO foulder
│
├ extract.py file
│
└ example 2026.02.21 foulder
    │
    ├── target1 file
    ├── target2 file
    │
    ├── result foulder
          └── rename.py file
```

---

## 🔧 Setup

Open the scripts and modify **only this line**:

```python
base_path = '/YOUR PATH/CAMEO/example2026.02.21'
```

Replace `/YOUR PATH/` with your actual system path.

### Examples

#### macOS

```python
base_path = '/Users/yourname/Desktop/CAMEO/example2026.02.21'
```

#### Windows

```python
base_path = 'C:/Users/YourName/Desktop/CAMEO/example2026.02.21'
```

#### Linux

```python
base_path = '/home/yourname/CAMEO/example2026.02.21'
```

---

## ▶️ Usage

Run the scripts from the terminal ensuring the script path location. 

```bash
# For extracting the file from CAMEO foulder
python3 extract.py    

```

```bash
 # For renaming the files based on their PDB ID
python3 rename.py    

```

---



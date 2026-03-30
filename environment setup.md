# Environment Setup 

This section shows how to prepare a Python environment before running the "rename.py" script.

You may use two separate terminal windows to run the "extract" and "rename" steps.

---

## 🧾 Step-by-step setup

### 1. Upgrade pip

```bash
python3 -m pip install --upgrade pip
```

---

### 2. Create a virtual environment

```bash
python3 -m venv myenv
```

---

### 3. Activate the environment

#### macOS / Linux

```bash
source myenv/bin/activate
```

#### Windows

```bash
myenv\Scripts\activate
```

---

### 4. Upgrade pip again (inside environment)

```bash
pip install --upgrade pip
```

---

### 5. Install additional packages

Create a file inside the "result" folder called `requirements.txt`:

```text
numpy
pandas
openpyxl
```

Then run:

```bash
pip install -r requirements.txt
```

---

### 6. Run the Extract Script in the First Terminal
This terminal does not need the above steps for enviroment preparation

```bash
python3 extract.py
```
---

### 7. Run the Rename Script in the Second Terminal 
This terminal needs the above steps for enviroment preparation 

The renaming script must be run from the folder where the extracted files are located.

Step 1 — "cd" locate your result folder
```bash
cd /YOUR PATH/CAMEO/example2026.02.21/result
```
Step 2 — Run the rename script
```bash
python3 rename.py
```
---

## Notes

* You do NOT need to repeat these steps every time
* Only activate the environment when working on the project
* Do not run both scripts at the same time. Run the "rename" step only after the "extract" step has finished
* The "rename" script must be inside the "result" folder

---

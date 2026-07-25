# 🧭 Installation Guide

This guide walks you through setting up the Automated Ticket Checking System from scratch, including Python, VS Code, required libraries, and running the project.

---

## 1. Install Python

1. Download Python 3.8 or above from [python.org/downloads](https://www.python.org/downloads/).
2. During installation, **check the box "Add Python to PATH"** — this is essential.
3. Verify installation by opening a terminal/command prompt and running:
   ```bash
   python --version
   ```
   You should see something like `Python 3.10.6`.

---

## 2. Set Up VS Code

1. Download and install [Visual Studio Code](https://code.visualstudio.com/).
2. Open VS Code and install the **Python extension** (by Microsoft) from the Extensions Marketplace (`Ctrl+Shift+X`).
3. Open the project folder in VS Code via `File → Open Folder`.
4. Select the correct Python interpreter: `Ctrl+Shift+P → Python: Select Interpreter`.

---

## 3. Clone the Repository

```bash
git clone https://github.com/<your-username>/Automated-Ticket-Checking-System.git
cd Automated-Ticket-Checking-System
```

If you don't have Git installed, download it from [git-scm.com](https://git-scm.com/downloads), or simply download the repository as a ZIP from GitHub and extract it.

---

## 4. Create a Virtual Environment (Recommended)

A virtual environment keeps this project's dependencies isolated from other Python projects.

```bash
python -m venv venv
```

Activate it:

- **Windows (Command Prompt):**
  ```bash
  venv\Scripts\activate
  ```
- **Windows (PowerShell):**
  ```bash
  venv\Scripts\Activate.ps1
  ```
- **macOS/Linux:**
  ```bash
  source venv/bin/activate
  ```

You should see `(venv)` appear at the start of your terminal prompt once activated.

---

## 5. Install Required Libraries

With the virtual environment active, install all dependencies from `requirements.txt`:

```bash
pip install -r requirements.txt
```

This installs:
- `qrcode`
- `opencv-python`
- `Pillow`
- `tabulate`

You can verify installation with:
```bash
pip list
```

---

## 6. Run the Project

### Generate a Ticket QR Code
```bash
python generate_qr.py
```

### Scan and Verify a Ticket
```bash
python scan_qr.py
```

Make sure your webcam is connected and not being used by another application (like Zoom or Teams) before running `scan_qr.py`.

---

## 7. Common Installation Issues & Solutions

| Issue | Solution |
|---|---|
| `python` is not recognized as a command | Reinstall Python and ensure "Add Python to PATH" is checked during setup |
| `pip install` fails with permission errors | Run terminal as Administrator (Windows) or use `pip install --user` |
| `ModuleNotFoundError: No module named 'cv2'` | Run `pip install opencv-python` (not just `opencv`) |
| Webcam does not open in `scan_qr.py` | Ensure no other app is using the camera; try changing `cv2.VideoCapture(0)` to `cv2.VideoCapture(1)` |
| QR code image doesn't save | Ensure you have write permissions in the project folder |
| `QR-CODE DATA.txt not found` during scanning | Run `generate_qr.py` at least once first to create the file |

For more detailed troubleshooting, see [`Troubleshooting.md`](Troubleshooting.md).

---

## 8. Arduino Setup (Optional Hardware Extension)

1. Install the [Arduino IDE](https://www.arduino.cc/en/software).
2. Connect the Arduino Uno via USB.
3. Select the correct board (`Tools → Board → Arduino Uno`) and port (`Tools → Port`).
4. Wire the IR sensor and servo motor as per [`hardware/Hardware_Setup_Diagram.png`](../hardware/Hardware_Setup_Diagram.png).
5. Upload your control sketch to the Arduino Uno.

---

✅ You're all set! Head back to the [README](../README.md) for usage instructions.

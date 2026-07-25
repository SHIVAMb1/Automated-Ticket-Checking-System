# 🗺️ Flowchart Explanation

This document explains, step by step, the flowchart used for QR code generation in this project.

<p align="center">
  <img src="../images/Flowchart.png" alt="QR Code Generation Flowchart" width="650">
</p>

---

## Step-by-Step Breakdown

### 1. Start
The process begins when the ticket generation script (`generate_qr.py`) is executed and the user provides journey details.

### 2. Receive Message to be Encoded in QR Code
The system compiles all ticket information — date, time, source, destination, fare, and the generated Unique ID — into a single structured text message. This is the "message" that will ultimately be embedded in the QR code.

### 3. Convert QR Message to Bytestring
Before encoding, the text message is converted into a bytestring representation. This is a necessary internal step because QR codes are fundamentally a binary/bit-level encoding format, not a plain-text one.

### 4. Add Header Information and Error Correction Bytes to Bytestring
The QR standard requires additional metadata to be prepended to the raw data:
- **Header information** specifies the QR version, encoding mode, and data length.
- **Error correction bytes** (Reed-Solomon codes) are added so the QR code remains readable even if part of it is damaged, dirty, or poorly lit. This project uses error correction level `L` (Low), which can recover from up to ~7% data loss.

### 5. Apply Masking Element
A masking pattern is applied across the QR matrix to avoid large blocks of similar-looking modules (black/white squares), which could otherwise confuse scanners. Masking ensures a good balance of light and dark modules for reliable optical detection.

### 6. Generate QR Code
With headers, error correction, and masking applied, the final QR code image is rendered — a matrix of black and white squares that visually represents the encoded ticket data. This is handled internally by the `qrcode` Python library and saved as a `.png` image file.

### 7. End
The QR code image is saved locally and is now ready to be issued to the passenger (displayed on a screen, printed, or sent digitally) and later scanned for verification.

---

## Why This Matters

Understanding this pipeline highlights *why* QR codes are a great fit for this project:
- They can hold enough data (date, time, route, fare, unique ID) in a small, printable/scannable format.
- Built-in error correction means the codes remain scannable even under non-ideal, real-world lighting and camera conditions.
- The encoding/decoding process is fast enough for real-time verification at a boarding gate.

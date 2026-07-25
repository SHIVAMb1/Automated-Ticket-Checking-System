# ⚙️ Working Principle

This document explains, step by step, how the **Automated Ticket Checking System** works from the moment a passenger books a ticket to the moment they are granted entry.

---

## Step 1: User Enters Ticket Information

The passenger (or an operator on their behalf) runs `generate_qr.py` and enters:
- Boarding Point (Source)
- Destination Point
- Bus Fare (Amount)

This is collected through simple terminal prompts using Python's built-in `input()` function.

---

## Step 2: QR Code Generation

Once the details are collected, the system prepares a text payload containing the date, time, source, destination, fare, and unique ID. This payload is passed to the `qrcode` library, which encodes it into a scannable QR image using error-correction level `L` for reliable scanning even under mild image distortion.

---

## Step 3: Unique ID Generation

To make every ticket distinguishable — even if two passengers book the exact same route at the exact same time — the system generates a **Unique ID**:

```
Unique ID = <Current Timestamp (YYYYMMDDHHMMSS)> + "_" + <6-character random alphanumeric string>
```

This combination makes accidental duplication statistically almost impossible.

---

## Step 4: Ticket Storage

All ticket details, including the Unique ID, are appended to a local file named `QR-CODE DATA.txt` (stored on the Desktop) in a clean, tabulated format using the `tabulate` library. This file acts as the **source of truth** for verification later.

---

## Step 5: QR Scanning

At the boarding point, the passenger presents their QR code to a webcam running `scan_qr.py`. The script continuously reads frames from the camera using `cv2.VideoCapture(0)`.

---

## Step 6: QR Decoding

Each captured frame is passed to OpenCV's built-in `cv2.QRCodeDetector().detectAndDecode()` method, which locates the QR code within the frame and decodes its embedded text payload.

---

## Step 7: Verification

From the decoded payload, the system extracts the substring following `"Unique ID: "`. This extracted ID is what will be checked against the stored ticket log.

---

## Step 8: Validation

The extracted Unique ID is searched for within `QR-CODE DATA.txt`:

- ✅ **If found** → the ticket is marked as **VALID**, and the passenger may proceed (in the hardware-integrated version, the Arduino Uno rotates the servo motor to open the gate).
- ❌ **If not found** → the ticket is marked as **INVALID**, and entry is denied.

---

## Step 9: Output

The result — VALID or INVALID — is printed to the console for the operator/conductor to see, along with the decoded ticket details. This provides an immediate, human-readable confirmation of the verification outcome.

---

### 🔁 Summary Flow

```
User Input → QR Generation → Unique ID Creation → Ticket Storage
     → (at gate) → QR Scanning → QR Decoding → ID Verification
     → Validation Result → Gate Action / Output
```

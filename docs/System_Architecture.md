# 🏗️ System Architecture

This document describes the overall architecture of the Automated Ticket Checking System, covering both the software and hardware components and how they interact.

---

## Architectural Components

| Component | Responsibility |
|---|---|
| **User** | Provides ticket details (source, destination, fare) at booking time, and presents the QR code at the gate |
| **Python Program** | Orchestrates ticket generation, storage, scanning, and verification logic |
| **QR Generator** | Encodes ticket data (via the `qrcode` library) into a scannable QR image |
| **File Storage** | Local text file (`QR-CODE DATA.txt`) that acts as the ticket record database |
| **Camera** | Captures a live video feed of the QR code at the checkpoint |
| **QR Scanner** | Decodes the QR image back into its original text payload using OpenCV |
| **Verification Module** | Cross-checks the extracted Unique ID against stored ticket records |
| **Output** | Displays VALID/INVALID result and (optionally) triggers hardware (servo motor via Arduino Uno) |

---

## ASCII Block Diagram

```
                        ┌────────────────────┐
                        │        USER         │
                        │ (enters ticket info)│
                        └──────────┬──────────┘
                                   │
                                   ▼
                        ┌────────────────────┐
                        │   PYTHON PROGRAM    │
                        │   (generate_qr.py)  │
                        └──────────┬──────────┘
                                   │
                     ┌─────────────┼─────────────┐
                     ▼                           ▼
           ┌───────────────────┐       ┌───────────────────┐
           │   QR GENERATOR     │       │   FILE STORAGE     │
           │  (qrcode library)   │      │ (QR-CODE DATA.txt) │
           └─────────┬──────────┘       └──────────┬─────────┘
                     │                              │
                     ▼                              │
           ┌───────────────────┐                    │
           │   QR CODE IMAGE     │                   │
           │ (given to passenger)│                   │
           └─────────┬──────────┘                    │
                      │                               │
        ── At the boarding gate ─────────────────────┤
                      ▼                               │
           ┌───────────────────┐                      │
           │       CAMERA        │                     │
           │  (captures QR feed)  │                    │
           └─────────┬──────────┘                      │
                      ▼                                 │
           ┌───────────────────┐                        │
           │    QR SCANNER        │                     │
           │   (scan_qr.py +      │                     │
           │  OpenCV detector)     │                    │
           └─────────┬──────────┘                       │
                      ▼                                  │
           ┌────────────────────┐                        │
           │ VERIFICATION MODULE  │◄──────────────────────┘
           │ (matches Unique ID)   │
           └─────────┬───────────┘
                      ▼
           ┌───────────────────┐
           │       OUTPUT         │
           │ VALID / INVALID +     │
           │ Servo Motor Action     │
           │ (via Arduino Uno)       │
           └───────────────────┘
```

---

## Hardware Interaction Layer

<p align="center">
  <img src="../hardware/Hardware_Setup_Diagram.png" alt="Hardware Setup Diagram" width="600">
</p>

The Arduino Uno acts as the bridge between the software verification result and physical access control:

1. The **IR Sensor** detects when a passenger approaches the gate.
2. The **laptop/PC** running `scan_qr.py` scans and verifies the ticket.
3. Upon a **VALID** result, a signal can be sent to the Arduino Uno (via serial communication in an extended version of this project) to rotate the **Servo Motor** and open the gate.
4. Upon an **INVALID** result, the gate remains closed and access is denied.

> 📌 **Note:** In the current version of this project, verification and hardware actuation are demonstrated as separate modules. Full serial communication between `scan_qr.py` and the Arduino sketch is listed as a future enhancement — see [`Future_Improvements.md`](Future_Improvements.md).

---

## Data Flow Summary

```
Input (User) → Processing (Python + qrcode) → Storage (Text File)
   → Capture (Camera) → Decode (OpenCV) → Verify (Python)
   → Output (Console) → Actuate (Arduino + Servo Motor)
```

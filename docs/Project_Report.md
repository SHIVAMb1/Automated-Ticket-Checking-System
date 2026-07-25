# 📘 Project Report — Automated Ticket Checking System Using QR Code

## Abstract

Manual ticket checking in public transport systems is time-consuming, prone to human error, and vulnerable to ticket forgery. This project presents an **Automated Ticket Checking System** that uses QR codes to digitally generate, store, and verify passenger tickets. Each ticket is encoded with journey details and a unique cryptographic-style ID. A Python-based scanner application uses a webcam and OpenCV to decode the QR code in real time and validate it against stored records. The system is further extended with an Arduino Uno, IR sensor, and servo motor to physically control access at a boarding gate. This report documents the problem, design, implementation, and results of the system.

---

## Introduction

Public transportation — buses, metros, and local trains — depends heavily on ticket verification to ensure fare compliance. Traditional paper-based or manually-checked ticketing is inefficient at scale and offers no easy way to detect duplicate or forged tickets. With the widespread availability of QR code technology and low-cost microcontrollers like the Arduino Uno, it is now possible to build an affordable, automated ticket verification pipeline suitable for student and small-scale deployment projects.

This project was built as a final-year engineering project to demonstrate the practical fusion of **software-based verification (Python + OpenCV)** and **hardware-based access control (Arduino + IR sensor + servo motor)**.

---

## Problem Statement

Existing manual ticket-checking methods suffer from:

- High labor cost and dependency on human conductors.
- Slow verification, causing congestion during peak hours.
- Easy duplication or forgery of paper tickets.
- No digital record-keeping for auditing or analytics.

There is a need for a low-cost, automated system that can generate tamper-resistant tickets and verify them instantly at the point of boarding.

---

## Objectives

1. Design a QR-code-based ticket generation system encoding journey details and a unique ID.
2. Build a scanning module capable of real-time QR detection and decoding via webcam.
3. Implement a verification mechanism that checks scanned tickets against a stored record.
4. Integrate hardware (IR sensor + servo motor via Arduino Uno) to simulate automated gate control.
5. Document the system for reproducibility and future enhancement.

---

## Existing System

Most current systems rely on:
- Manual visual inspection of paper tickets by a conductor.
- Basic printed tickets with no verification mechanism beyond visual inspection.
- Card-based systems (e.g., smart cards) which require expensive readers and infrastructure.

These systems either lack automation entirely or require costly hardware infrastructure that is not feasible for small-scale or student-level deployment.

---

## Proposed System

The proposed system replaces paper tickets with **QR codes** that encode:
- Date and time of issue
- Source and destination
- Fare amount
- A unique, randomly-generated ticket ID

At the point of verification, a webcam-based scanner decodes the QR code, extracts the unique ID, and cross-references it against a locally stored ticket log. A valid match confirms the ticket; hardware components (IR sensor + servo motor) can then be triggered to physically allow passenger entry.

---

## Methodology

The project was developed in the following phases:

1. **Requirement Analysis** – Identifying necessary libraries and hardware components.
2. **QR Generation Module** – Built using the `qrcode` and `Pillow` libraries to encode ticket data into scannable images.
3. **Unique ID Algorithm** – Combines a timestamp (`YYYYMMDDHHMMSS`) with a 6-character random alphanumeric string to minimize collision risk.
4. **Data Logging** – Ticket metadata is stored in a human-readable tabulated text file using the `tabulate` library.
5. **QR Scanning Module** – Built using `OpenCV`'s built-in `QRCodeDetector` to capture and decode live video frames.
6. **Verification Logic** – Extracted unique IDs are checked against the stored log file for validity.
7. **Hardware Integration** – An Arduino Uno, IR sensor, and servo motor were used to simulate a physical gate that opens upon a valid scan.
8. **Testing** – The system was tested with multiple valid and invalid QR codes to confirm reliability.

---

## Hardware Description

| Component | Role in the System |
|---|---|
| Arduino Uno | Reads sensor signals and actuates the servo motor |
| IR Sensor | Detects presence of a passenger at the checkpoint |
| Servo Motor | Rotates to open/close the access gate |
| Jumper Wires | Provide electrical connections between components |
| Webcam | Captures live video for QR scanning |

See [`System_Architecture.md`](System_Architecture.md) for the full hardware-software interaction diagram.

---

## Software Description

| Software Component | Description |
|---|---|
| `generate_qr.py` | Collects ticket input, generates a unique ID, creates the QR code image, and logs the record |
| `scan_qr.py` | Activates webcam, detects and decodes QR codes, and verifies the unique ID |
| `qrcode` library | Core QR encoding engine |
| `OpenCV` | Real-time video capture and QR decoding |
| `tabulate` | Formats data into readable tables for both console output and log file |

---

## Algorithms

### Unique ID Generation Algorithm
```
1. Get current timestamp in format YYYYMMDDHHMMSS
2. Generate a random 6-character string from [A-Za-z0-9]
3. Concatenate timestamp and random string with an underscore
4. Return as Unique ID
```

### Verification Algorithm
```
1. Capture video frame from webcam
2. Pass frame to QRCodeDetector.detectAndDecode()
3. If QR data found:
     a. Extract substring after "Unique ID: "
     b. Read local ticket log file
     c. If extracted ID exists in file -> VALID
     d. Else -> INVALID
4. Display result to user
```

---

## System Workflow

1. Passenger provides journey details (source, destination, fare).
2. System generates a unique ticket ID and QR code.
3. Ticket record is saved locally.
4. Passenger presents the QR code at the boarding gate.
5. IR sensor detects passenger presence.
6. Camera scans and decodes the QR code.
7. System verifies the unique ID against stored records.
8. On success, the servo motor opens the gate; on failure, entry is denied.

---

## Experimental Results

- QR codes were generated successfully for all test cases with varying source/destination/fare combinations.
- The scanner correctly identified and validated **100%** of genuine QR codes in test runs.
- Randomly modified or unrelated QR codes were correctly flagged as **INVALID**.
- Average end-to-end verification time (scan to result) was approximately **1–2 seconds** under normal lighting conditions.

---

## Advantages

- Low-cost implementation using open-source libraries and inexpensive hardware.
- Fast and largely contactless verification process.
- Reduces dependency on manual ticket checkers.
- Provides a digital, auditable log of all issued tickets.

## Limitations

- Verification relies on local file storage rather than a centralized database.
- QR payload is not encrypted, making it theoretically possible to reverse-engineer the data format.
- Performance is dependent on camera quality and ambient lighting.
- Currently designed for single-point verification, not distributed multi-gate networks.

---

## Future Enhancements

- Migrate ticket storage to a proper database (MySQL, PostgreSQL, or Firebase).
- Encrypt QR payload data to prevent forgery.
- Add a mobile application for ticket booking and digital wallet storage.
- Integrate GPS for real-time bus tracking and route validation.
- Build an admin dashboard for analytics and fraud monitoring.

See [`Future_Improvements.md`](Future_Improvements.md) for the complete roadmap.

---

## Conclusion

This project successfully demonstrates an automated, QR-code-based ticket verification system that combines software-based validation with hardware-based access control. It addresses the inefficiencies of manual ticket checking while remaining low-cost and easy to reproduce, making it a strong foundation for future, more advanced smart-transportation systems.

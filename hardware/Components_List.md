# 🔩 Hardware Components List

The table below lists all hardware components used in the physical (Arduino-based) extension of this project.

<p align="center">
  <img src="Components_List_Photo.png" alt="Components List" width="600">
</p>

| Component Name | Quantity | Purpose | Specifications |
|---|---|---|---|
| Arduino Uno | 1 | Central microcontroller that reads the IR sensor and drives the servo motor | ATmega328P, 5V logic, 14 digital I/O pins |
| IR Sensor | 1 | Detects the presence of a passenger/vehicle at the checkpoint to trigger scanning/gate logic | Infrared obstacle detection module, ~2–30 cm range |
| Servo Motor | 1 | Physically rotates to open/close the access gate upon valid ticket verification | SG90 (or equivalent), 4.8V–6V, ~180° rotation |
| Jumper Wires | As required | Provide electrical connections between Arduino, IR sensor, and servo motor | Male-to-male / Male-to-female, standard 0.1" pitch |
| Power Supply | 1 | Powers the Arduino Uno and connected peripherals | 5V DC (USB or external adapter) |
| Webcam / USB Camera | 1 | Captures the live video feed used for QR code scanning | Any standard USB webcam, 720p or higher recommended |

---

## Approximate Cost Breakdown

| Sr. No | Component | Price (₹) |
|---|---|---|
| 1 | IR Sensor | 300 |
| 2 | Arduino Uno | 700 |
| 3 | Servo Motor | 300 |
| 4 | Jumper Wires | 100 |
| 5 | Power Supply | 200 |
| | **Total (approx.)** | **₹1,600** |

> 💡 Prices are approximate and based on standard component costs at the time of this project's development; actual prices may vary by vendor and region.

---

## Wiring Overview

<p align="center">
  <img src="Hardware_Setup_Diagram.png" alt="Hardware Setup Diagram" width="600">
</p>

- The **IR Sensor** is mounted at the entry point to detect passenger presence.
- The **Servo Motor** is mechanically linked to the gate/barrier arm.
- The **Arduino Uno** reads the IR sensor's digital output and, based on verification results from the Python scanner, commands the servo motor to rotate.
- The **laptop/PC** running `generate_qr.py` and `scan_qr.py` handles all QR generation, scanning, and verification logic.

For full system-level interaction between hardware and software, see [`../docs/System_Architecture.md`](../docs/System_Architecture.md).

import cv2
import os


def check_unique_code_in_file(unique_code):

    desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
    filepath = os.path.join(desktop_path, "QR-CODE DATA.txt")

    if not os.path.exists(filepath):
        print("QR-CODE DATA.txt not found.")
        return False

    with open(filepath, "r") as file:
        data = file.read()

    return unique_code in data


cap = cv2.VideoCapture(0)

detector = cv2.QRCodeDetector()

print("Scanning QR Code...")
print("Press 'q' to Quit.\n")

qr_processed = False

while True:

    ret, img = cap.read()

    if not ret:
        break

    if not qr_processed:

        data, vertices_array, _ = detector.detectAndDecode(img)

        if vertices_array is not None:

            if data:

                print("\nQR Code Detected!\n")
                print(data)

                try:
                    unique_code = data.split("Unique ID: ")[1].strip()

                    print("\nExtracted Unique ID:")
                    print(unique_code)

                    if check_unique_code_in_file(unique_code):

                        print("\n✅ VALID QR CODE")
                        print("Unique ID matched successfully.")

                    else:

                        print("\n❌ INVALID QR CODE")
                        print("Unique ID not found.")

                except IndexError:
                    print("Unable to extract Unique ID.")

                qr_processed = True

    cv2.imshow("QR Code Scanner", img)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
import qrcode
import datetime
import random
import string
import os
from tabulate import tabulate


def generate_qr_code(data, filename):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )

    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save(filename)


def generate_unique_id():
    current_time = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    random_string = ''.join(
        random.choices(string.ascii_letters + string.digits, k=6)
    )
    unique_id = f"{current_time}_{random_string}"
    return unique_id


def save_information_to_file(date, time, unique_id, source, destination, amount, filename):

    desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
    filepath = os.path.join(desktop_path, "QR-CODE DATA.txt")

    data = [
        ["Date", date],
        ["Time", time],
        ["Unique ID", unique_id],
        ["Source", source],
        ["Destination", destination],
        ["Amount", amount],
        ["QR Code Filename", filename],
    ]

    headers = ["Field", "Value"]

    with open(filepath, "a") as file:
        file.write(tabulate(data, headers=headers, tablefmt="grid"))
        file.write("\n\n")


def main():

    date = datetime.datetime.now().strftime("%Y-%m-%d")
    time = datetime.datetime.now().strftime("%H:%M:%S")

    source = input("Enter Bus Boarding Point : ")
    destination = input("Enter Destination Point : ")
    amount = input("Enter Bus Fare : ")

    unique_id = generate_unique_id()

    qr_data = (
        f"Date: {date}\n"
        f"Time: {time}\n"
        f"Source: {source}\n"
        f"Destination: {destination}\n"
        f"Amount: {amount}\n"
        f"Unique ID: {unique_id}"
    )

    filename = f"{source}_{destination}_qr_code.png"

    generate_qr_code(qr_data, filename)

    table = [
        ["Date", date],
        ["Time", time],
        ["Unique ID", unique_id],
        ["Source", source],
        ["Destination", destination],
        ["Amount", amount],
        ["QR Code Filename", filename],
    ]

    print("\nQR Code Generated Successfully!\n")
    print(tabulate(table, headers=["Field", "Value"], tablefmt="grid"))

    save_information_to_file(
        date,
        time,
        unique_id,
        source,
        destination,
        amount,
        filename,
    )


if __name__ == "__main__":
    main()
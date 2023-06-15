import cv2
from pyzbar.pyzbar import decode

image_path = 'qr_code.JPG'
image = cv2.imread(image_path)

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

barcodes = decode(gray)

for barcode in barcodes:
    barcode_data = barcode.data.decode("utf-8")
    print("Barcode data:", barcode_data)


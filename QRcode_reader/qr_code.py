import cv2
from pyzbar.pyzbar import decode

# Đọc ảnh từ file
image_path = 'qr_code.JPG'  # Thay đổi đường dẫn tới ảnh của bạn
image = cv2.imread(image_path)

# Chuyển đổi ảnh sang định dạng grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Sử dụng thư viện pyzbar để giải mã mã vạch
barcodes = decode(gray)

# Lặp qua tất cả các mã vạch tìm được
for barcode in barcodes:
    # Lấy nội dung của mã vạch và in ra màn hình
    barcode_data = barcode.data.decode("utf-8")
    print("Barcode data:", barcode_data)


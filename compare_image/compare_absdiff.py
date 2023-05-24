import cv2

def detect_abnormality(original_image_path, compared_image_path):
    # read image and convert format grayscale
    original_image = cv2.imread(original_image_path)
    compared_image = cv2.imread(compared_image_path)

    original_gray = cv2.cvtColor(original_image, cv2.COLOR_BGR2GRAY)
    compared_gray = cv2.cvtColor(compared_image, cv2.COLOR_BGR2GRAY)

    # Calculate the difference between two images
    diff = cv2.absdiff(original_gray, compared_gray)

    # Calculate total difference value
    diff_sum = diff.sum()

    # Calculate percentage difference
    diff_percent = (diff_sum / (original_gray.shape[0] * original_gray.shape[1])) * 100

    # Print the result
    if diff_percent > 80:
        print("NG")
    else:
        print("OK")

original_image_path = "./data_compare/check_11gio_02phut_19giay.jpg"
compared_image_path = "/data_compare/check_09gio_24phut_11giay.jpg"

detect_abnormality(original_image_path, compared_image_path)

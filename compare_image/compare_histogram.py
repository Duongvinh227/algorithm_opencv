import cv2

def compare_histograms(image1_path, image2_path):
    # read image and convert format grayscale
    image1_ = cv2.imread(image1_path)
    image2_ = cv2.imread(image2_path)

    image1 = cv2.cvtColor(image1_, cv2.COLOR_BGR2GRAY)
    image2 = cv2.cvtColor(image2_, cv2.COLOR_BGR2GRAY)
    # Calculate the histogram of the image
    hist1 = cv2.calcHist([image1], [0], None, [256], [0, 256])
    hist2 = cv2.calcHist([image2], [0], None, [256], [0, 256])

    # Normalize histogram
    cv2.normalize(hist1, hist1, alpha=0, beta=1, norm_type=cv2.NORM_MINMAX)
    cv2.normalize(hist2, hist2, alpha=0, beta=1, norm_type=cv2.NORM_MINMAX)

    # Compare histograms by correlation method
    correlation = cv2.compareHist(hist1, hist2, cv2.HISTCMP_CORREL)

    # Print the result
    if correlation > 0.8:
        print("OK")
    else:
        print("NG")

image1_path = "./data_compare/check_11gio_02phut_19giay.jpg"
image2_path = "/data_compare/check_09gio_24phut_11giay.jpg"

compare_histograms(image1_path, image2_path)

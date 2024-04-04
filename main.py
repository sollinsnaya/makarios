from kritis import app

import os
import cv2
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
from sklearn.cluster import KMeans

# Folder where images are uploaded
path=("./images/")
# read the image

img = os.path.join(path,"/Users/sdennis/Desktop/Makarios/images/uploaded_image.jpg")
image = cv2.imread(img,1)

# Convert the image to RGB (OpenCV uses BGR by default)
#image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# convert it to grayscale
#gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply Gaussian blur
#kernel_size = (5, 5)  # Adjust the kernel size as needed
#smoothed_image = cv2.GaussianBlur(gray, kernel_size, 0)

# perform the canny edge detector to detect image edges
#edges = cv2.Canny(smoothed_image, threshold1=30, threshold2=100)

#plt.imshow(edges), plt.title('grayscale_BGR + smoothed')
#plt.show()


def quantify_colors(image_path, num_colors=200): #this function is shit
    # Load the image
    image = Image.open(image_path)

    # Convert image to numpy array
    image_np = np.array(image)


    # Reshape the image array to be a list of RGB pixels
    pixels = image_np.reshape((-1, 3))

    # Use KMeans to cluster pixels into 'num_colors' clusters
    kmeans = KMeans(n_clusters=num_colors)
    kmeans.fit(pixels)

    # Get the cluster centers
    colors = kmeans.cluster_centers_.astype(int)

    return colors


def reconstruct_image(quantized_colors): #this function is shit
    # Convert the quantized colors to a NumPy array
    quantized_colors = np.array(quantized_colors)

    # Create a new image with the same shape as the quantized colors matrix
    reconstructed_image = np.zeros((quantized_colors.shape[0], quantized_colors.shape[1], 3), dtype=np.uint8)

    # Iterate through each pixel in the original image
    for i in range(reconstructed_image.shape[0]):
        for j in range(reconstructed_image.shape[1]):
            # Assign the quantized color to the corresponding pixel in the reconstructed image
            reconstructed_image[i, j] = quantized_colors[i, j]

    # Convert the NumPy array back to an image
    reconstructed_image = Image.fromarray(reconstructed_image)

    return reconstructed_image


def find_contours(img):

    gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    thresh = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 115, 1)

    cv2.imshow("Binary", thresh)

    contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    img2 = img.copy()

    index = -1
    thickness = 4
    color = (255, 0, 255)

    objects = np.zeros([img.shape[0], img.shape[1], 3], 'uint8')

    for c in contours:
        cv2.drawContours(objects, [c], -1, color, -1)

        area = cv2.contourArea(c)
        perimeter = cv2.arcLength(c, True)

        M = cv2.moments(c)

        if M["m00"] == 0.0:
            M["m00"] = 0.1
        cx = int(M['m10'] / M['m00'])
        cy = int(M['m01'] / M['m00'])
        cv2.circle(objects, (cx, cy), 4, (0, 0, 255), -1)

        #print(f"Area: {area}, perimeter: {perimeter}")
    cv2.imshow("Contours", objects)
    edges = cv2.Canny(objects, threshold1=30, threshold2=100)
    cv2.imshow('edges', edges)

cv2.imshow("Original", image)
original_edges = cv2.Canny(image, threshold1=30, threshold2=100)
cv2.imshow('original_edges', original_edges)
find_contours(image)
cv2.waitKey(0)
cv2.destroyAllWindows()








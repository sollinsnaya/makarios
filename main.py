from kritis import app

#Below is just for testing stuff

import cv2
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

image = cv2.imread("/Users/sdennis/Downloads/dogballoon.png")
cv2.namedWindow("Image", cv2.WINDOW_NORMAL)


def generate_palette(image, num_colors=24):

    original_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    # Reshape the image to be a list of pixels
    pixels = original_image.reshape((-1, 3))

    # Step 2: Color Quantization
    kmeans = KMeans(n_clusters=num_colors)
    kmeans.fit(pixels)
    # Get the cluster centers
    colors = kmeans.cluster_centers_

    # Step 3: Color Analysis (Count the frequency of each color)
    # In this basic example, we don't calculate frequencies, but in a more advanced approach,
    # you can count the occurrences of each cluster label and use that as a weight to determine the frequency.

    # Step 4: Palette Generation
    palette = colors.astype(int)

    # Create a blank image to display the palette
    palette_image = np.zeros((50, len(palette) * 50, 3), dtype=np.uint8)

    # Fill the palette image with colors from the palette
    for i, color in enumerate(palette):
        palette_image[:, i * 50:(i + 1) * 50, :] = color

    plt.imshow(palette_image)
    plt.axis('off')
    plt.show()

    return palette

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

#Show the original image
cv2.imshow("Original", image)

#show the original image if applied canny edges directly
original_edges = cv2.Canny(image, threshold1=30, threshold2=100)
cv2.imshow('original_edges', original_edges)

#find binary of the image, find the countours, apply edges to the countour.
find_contours(image)

print(generate_palette(image))

cv2.waitKey(0)
cv2.destroyAllWindows()








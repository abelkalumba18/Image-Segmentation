import cv2
import numpy as np
from sklearn.cluster import KMeans
# import warnings filter
from warnings import simplefilter
# ignore all future warnings
simplefilter(action='ignore', category=FutureWarning)

# Load the image
image = cv2.imread("terrain_image.png")

# Reshape the image to a 2D array of pixels
pixels = image.reshape((-1, 3))

# Apply k-means clustering
k = 3 # Number of clusters for drought and non-drought colors
kmeans = KMeans(n_clusters=k)
kmeans.fit(pixels)

# Get the labels and cluster centers
labels = kmeans.labels_
centers = kmeans.cluster_centers_

# Assign each pixel to the nearest cluster center
segmented_image = centers[labels].reshape(image.shape)

# Display the segmented image
cv2.imshow("Segmented Image", segmented_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

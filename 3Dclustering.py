import numpy as np
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Generate random 3D data for testing
np.random.seed(42)
num_samples = 100
data = np.random.rand(num_samples, 3)

# Perform K-means clustering
num_clusters = 3
kmeans = KMeans(n_clusters=num_clusters)
kmeans.fit(data)
labels = kmeans.labels_
centroids = kmeans.cluster_centers_

# Plot the clustered data
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot data points
for i in range(num_clusters):
    cluster_data = data[labels == i]
    ax.scatter(cluster_data[:, 0], cluster_data[:, 1], cluster_data[:, 2], label=f'Cluster {i+1}')

# Plot centroids
ax.scatter(centroids[:, 0], centroids[:, 1], centroids[:, 2], c='black', marker='*', s=200, label='Centroids')

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('K-means Clustering')
ax.legend()

plt.show()

import numpy as np 
import random
import scipy.spatial.distance as dist
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)

import load_data
import visualize_centroids as vis

# np.random.seed(42)
number_of_clusters = [20]
iteration = 3

train, valid, test  = load_data.load_data('./mnist.pkl.gz')
train_data = train[0]
# train_data = train_data[0:10,:]
labels = np.zeros(train_data.shape[0])
# print labels.shape

for cluster in number_of_clusters:
	directory_path = './'+str(cluster)+'_centroids_images/'
	centroid_index = random.sample(range(1,train_data.shape[0]),cluster)
	centroid  =  train_data[centroid_index]
	# print centroid[0].shape

	for iterations in range(0, iteration):
		print "Iteration " + str(iterations)
		for idx, data in enumerate(train_data):
			dist = []
			for center in centroid:
				dist.append(np.linalg.norm(data-center))
			labels[idx] = dist.index(min(dist))
		print labels
		#Update Clusterss
		for cluster_number in range(0,cluster):
			index = []
			for idx, label in enumerate(labels):
				if label == cluster_number:
					index.append(idx)
			temp_data = train_data[index]
			print 'Updating cluster ' + str(cluster_number)
			centroid[cluster_number] = np.mean(temp_data, axis = 0)
	print centroid	
	np.savez(str(cluster)+'_centroids.npz', centroids = centroid)
	vis.visualize(cluster)
	


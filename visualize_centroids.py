import numpy as np
import scipy.misc 
import os

def toimg(X,name):
	Y = np.reshape(X,(-1,28))
	scipy.misc.imsave(name,Y)


def visualize(clusters):
	data = np.load(str(clusters)+'_centroids.npz')
	centroids = data['centroids']
	directory_path = './'+str(clusters)+'_centroids_images/'
	if not os.path.exists(directory_path):
			os.makedirs(directory_path)

	for i in range(0, clusters):
		name  = directory_path +'image'+str(i)+'.png'
		print 'saving image', name
		toimg(centroids[i], name)
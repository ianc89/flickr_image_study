# My data object
from dataset import dataset
# kNN algorithm
from sklearn.neighbors import NearestNeighbors
# Tools
from utils import generate_similar_image, write_results, initialise_results

# Preamble - Load data
d = dataset()
d.construct_dataset(1000)
d.initialise_images()
# Check
print (d.photos[0].name, d.photos[0].data.shape)

# Unsupervised knn
X_val, X_train = d.get_train_valid(10)
X_train_data   = [x.data for x in X_train]
X_val_data     = [x.data for x in X_val]

# Set up a nearest neighbour model with 10 neighbours
nbrs = NearestNeighbors(n_neighbors=10, algorithm='ball_tree').fit(X_train_data)

# Query an image
distances, indices = nbrs.kneighbors(X_val_data)

# Initialise result folder
initialise_results("forTableau/","results.csv",10)

# Loop over the zipped validation file and associated neighbour indices
for x,ind in zip(X_val, indices):
	# Produce an output image
	generate_similar_image(x, ind, X_train)
	write_results(x, [X_train[y] for y in ind], "forTableau/","results.csv")










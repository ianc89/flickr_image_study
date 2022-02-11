from dataset import dataset
import numpy as np
from sklearn.neighbors import NearestNeighbors
from utils import generate_similar_image

# Embedding weights
embedding_dict  = dict(np.load("embedding.npz"))
# one-hot encode vocab
embedding_vocab = np.load("vocab.npy", allow_pickle=True)

# Within the text vector space, the sum of weights should point to a location
# which is similar to other captions

d = dataset()
d.construct_dataset(1000)
d.calculate_embedding(embedding_dict)
X_val, X_train = d.get_train_valid(10)
X_val_data     = [x.embedding_sum for x in X_val]
X_train_data   = [x.embedding_sum for x in X_train]


nbrs = NearestNeighbors(n_neighbors=10, algorithm='ball_tree').fit(X_train_data)

distances, indices = nbrs.kneighbors(X_val_data)

# Loop over the zipped validation file and associated neighbour indices
for x,ind in zip(X_val, indices):
	# Produce an output image
	generate_similar_image(x, ind, X_train, text=True)



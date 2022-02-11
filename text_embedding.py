# Useful information: https://towardsdatascience.com/creating-word-embeddings-coding-the-word2vec-algorithm-in-python-using-deep-learning-b337d0ba17a8
from dataset import dataset
import tensorflow as tf
from utils import get_unique_words
from tensorflow.keras.utils import to_categorical  
import numpy as np

# Load dataset (no need to initialise images)
d = dataset()
d.construct_dataset(1000)

# Get unique words
unique_words_dict, all_words = get_unique_words(d)
num_words = len(unique_words_dict)

# Convert to one-hot encoding
print ("Prepare one-hot encoding")
X = []
Y = []
for p in d.photos:
	for x,y in p.pair:
		X.append(to_categorical(unique_words_dict[x], num_words))
		Y.append(to_categorical(unique_words_dict[y], num_words))

X = np.asarray(X)
Y = np.asarray(Y)

# Defining the neural network
embed_size = 10 #2
inp   = tf.keras.layers.Input(shape=(X.shape[1],))
x     = tf.keras.layers.Dense(units=embed_size, activation='linear')(inp)
x     = tf.keras.layers.Dense(units=Y.shape[1], activation='softmax')(x)
model = tf.keras.models.Model(inputs=inp, outputs=x)
model.compile(loss = 'categorical_crossentropy', optimizer = 'adam')

# Optimizing the network weights
model.fit(
    x=X, 
    y=Y, 
    batch_size=10,
    epochs=10
    )

# Obtaining the weights from the neural network -> word embedding

# The input layer 
weights = model.get_weights()[0]

# Creating a dictionary to store the embeddings in. The key is a unique word and 
# the value is the numeric vector
embedding_dict = {}
for word in all_words: 
    embedding_dict.update({
        word: weights[unique_words_dict.get(word)]
        })

# Plot
#import matplotlib.pyplot as plt
#plt.figure(figsize=(10, 10))
#for word in list(unique_words_dict.keys()):
#	coord = embedding_dict.get(word)
#	plt.scatter(coord[0], coord[1])
#	plt.annotate(word, (coord[0], coord[1]))
#plt.savefig("word_embedding.png")

print (type(embedding_dict))
print (type(unique_words_dict))

# np.load("embedding.npz")
np.savez("embedding.npz", **embedding_dict)
# np.load("vocab.npy", allow_pickle=True)
np.save("vocab.npy", unique_words_dict)


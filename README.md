# Flickr Image Study - Kaggle

Showing some examples for image and NLP processing.

# Data

Data taken from https://www.kaggle.com/hsankesara/flickr-image-dataset/download

# Classes

| *Filename* | *Usage* |
| --- | --- |
| `dataset.py` | Class structure to hold data information |
| `image_clustering_knn.py` | Processing to perform k-nearest neighbour algorithm |
| `text_embedding.py` | Processing to generate text embedding space weights |
| `vocab_clustering_knn.py` | Processing to perform knn using word embeddings |
| `utils.py` | Useful utility functions to be loaded and reduce bloat across scripts |
| `embedding.npz` | Text embedding dictionary stored in npz format |

# Results

Running on 990 data points, the clustering results in the following example results. The pixel clustering only required the images to be loaded and normalised for pixel intensity. The text embedding first required an embedding to be trained (here I only used 10 nodes) and these weights are then loaded and summed to give a point in vector space for each caption which is subsequently used for the clustering.

When using pixel information for clustering...

![example](similar_images/similar_1423997242.jpg.png)

When using text embedding for clustering...

![example](similar_text/similar_1423997242.jpg.png)


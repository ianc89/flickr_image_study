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

# Usage

With the flickr dataset downloaded and placed in a `data/` folder, these scripts can be run simply with `python3 image_clustering_knn.py`, `python3 text_embedding.py` and `python3 vocab_clustering_knn.py`.

# Results

Running on 990 data points, the clustering results in the following example results. The pixel clustering only required the images to be loaded and normalised for pixel intensity. The text embedding first required an embedding to be trained (here I only used 10 nodes) and these weights are then loaded and summed to give a point in vector space for each caption which is subsequently used for the clustering.

When using pixel information for clustering...

![example](similar_images/similar_1423997242.jpg.png)

When using text embedding for clustering...

![example](similar_text/similar_1423997242.jpg.png)

# Tableau

<div class='tableauPlaceholder' id='viz1644846886696' style='position: relative'><object class='tableauViz'  style='display:none;'><param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> <param name='embed_code_version' value='3' /> <param name='path' value='views&#47;flickr_image_display&#47;Dashboard1?:language=en-GB&amp;:embed=true&amp;publish=yes' /> <param name='toolbar' value='yes' /><param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' /><param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' /><param name='display_count' value='yes' /><param name='language' value='en-GB' /><param name='filter' value='publish=yes' /></object></div>                <script type='text/javascript'>                    var divElement = document.getElementById('viz1644846886696');                    var vizElement = divElement.getElementsByTagName('object')[0];                    if ( divElement.offsetWidth > 800 ) { vizElement.style.minWidth='420px';vizElement.style.maxWidth='650px';vizElement.style.width='100%';vizElement.style.minHeight='587px';vizElement.style.maxHeight='887px';vizElement.style.height=(divElement.offsetWidth*0.75)+'px';} else if ( divElement.offsetWidth > 500 ) { vizElement.style.minWidth='420px';vizElement.style.maxWidth='650px';vizElement.style.width='100%';vizElement.style.minHeight='587px';vizElement.style.maxHeight='887px';vizElement.style.height=(divElement.offsetWidth*0.75)+'px';} else { vizElement.style.width='100%';vizElement.style.height='727px';}                     var scriptElement = document.createElement('script');                    scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';                    vizElement.parentNode.insertBefore(scriptElement, vizElement);                </script>


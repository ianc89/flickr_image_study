import numpy as np

embedding_dict  = dict(np.load("embedding.npz"))

for key in embedding_dict:
	v = embedding_dict[key]
	v = v.tolist()
	v = [str(x) for x in v]
	f.write(key+","+",".join(v)+"\n")


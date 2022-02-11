def generate_pairs(text):
	window = 2
	word_list = []
	text = text.split()
	
	for i, word in enumerate(text):
		for w in range(window):
			if i + 1 + w < len(text): 
				word_list.append([word] + [text[(i + 1 + w)]])
			if i - w - 1 >= 0:
				word_list.append([word] + [text[(i - w - 1)]])
	return word_list

def get_unique_words(dataset):
	print ("Assessing unique words...")
	all_words = []
	for p in dataset.photos:
		for caption in p.cleaned_text:
			all_words.extend(caption.split())

	# Take all words, remove duplicates and return to a sorted list
	all_words = list(set(all_words))
	all_words.sort()

	# Generate a dictionary
	unique_word_dict = {}

	for i,word in enumerate(all_words):
		#unique_word_dict[word] = i
		unique_word_dict.update({
        	word: i
        	})

	print (f"{len(unique_word_dict)} unique words")
	return unique_word_dict, all_words

def generate_similar_image(x, ind, X_train, text=False):
	import cv2
	from matplotlib import pyplot as plt

	# Generate a visual display for each query image
	fig     = plt.figure(figsize=(10, 7))
	rows    = 3
	columns = 5
	image = cv2.imread(x.name)
	fig.add_subplot(rows, columns, 3)
	plt.imshow(image)
	plt.axis('off')
	plt.title("Query")
	if text:
		plt.title("Query \n"+x.text[0])
	print (f"{x.name} similar to ")
	for iim,i in enumerate(ind):
		print (f"  {i} ... {X_train[i].name}")
		image = cv2.imread(X_train[i].name)
		fig.add_subplot(rows, columns, iim+6)
		plt.imshow(image)
		plt.axis('off')
		#if text:
		#	plt.title(X_train[i].text[0])
	# Save
	img_name = x.name.split("/")[-1]
	if text:
		plt.savefig(f"similar_text/similar_{img_name}.png")
	else:		
		plt.savefig(f"similar_images/similar_{img_name}.png")


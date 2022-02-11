import glob
import re
from utils import generate_pairs


class photo(object):
	"""
	Object to data about each image in dataset (filename, caption)
	"""
	def __init__(self, name, text):
		self.name = name
		self.text = text
		self.data = None

		# Additional manipulation
		self.pair = []
		self.cleaned_text = []

		# Clean text
		for i,t in enumerate(self.text):
			cleaned_text = self.clean_text(t)
			self.pair.extend(generate_pairs(cleaned_text))
			self.cleaned_text.append(cleaned_text)

	def info(self):
		# Small function to check the data
		print (self.name)
		for t in self.text:
			print (f" - {t}")
		if self.data is None:
			print ("... No pixel infomation loaded")
		else:
			print ("... Pixel information loaded")


	def clean_text(self, string: str, 
		punctuations=r'''!()-[]{};:'"\,<>./?@#$%^&*_~''',
		stop_words=['.',',','the','a','and','is','be','will','of','at','to','in','on','off','all','are']) -> str:
	    
		# Cleaning the urls
		string = re.sub(r'https?://\S+|www\.\S+', '', string)
		# Cleaning the html elements
		string = re.sub(r'<.*?>', '', string)

		# Removing the punctuations
		for x in string.lower(): 
			if x in punctuations: 
				string = string.replace(x, "") 
		

		# Converting the text to lower
		string = string.lower()
		# Removing stop words
		string = ' '.join([word for word in string.split() if word not in stop_words])
		# Cleaning the whitespaces
		string = re.sub(r'\s+', ' ', string).strip()
	
		return string 


class dataset(object):
	"""
	Object to hold the dataset of photos which have been loaded
	"""
	def __init__(self):
		self.photos       = []
		self.base         = "data/"
		self.desc_path    = "results.csv"
		self.image_folder = "flickr30k_images/"
		self.set_images   = True

	def get_descriptions(self):
		# Function to parse description file where it has the format
		# imageXXX#captionNum "caption"
		description_dict = {}
		description_file = open(self.base+self.desc_path,"r")
		# Read file
		for line in description_file.readlines():
			# Split to get the image name and caption number
			try:
				key,val,description = line.split("|")
			except:
				print (line)
				continue
			# Construct list in dictionary
			if key not in description_dict:
				description_dict[key] = []
			# Append caption 
			description_dict[key].append(description.strip())
		# Return the object
		return description_dict


	def construct_dataset(self, entries=-1):
		# Construct an object which can hold the data that has been provided
		list_of_images = glob.glob(self.base+self.image_folder+"*.jpg")
		descriptions = self.get_descriptions()

		for i,img in enumerate(list_of_images):
			if entries >= 0 and i < entries:
				key = img.split("/")[-1]
				if key in descriptions:
					desc = descriptions[key]
					self.photos.append(photo(img,desc))
				else:
					print (f"Error for image {img} to access captions")
					continue

		print (f"Loaded {len(self.photos)} entries")

	def initialise_images(self):
		# Method to load the image into pixel array
		from PIL import Image
		import numpy as np
		for p in self.photos:
			# Open the image
			img = Image.open(p.name)
			# Resize for consistency
			img = img.resize((256, 256), Image.ANTIALIAS)
			p.data = np.asarray(img)
			p.data = p.data.flatten()
			p.data = p.data / 255

	def check_shapes(self):
		# Method to check structure
		for p in self.photos:
			print (p.data.shape)

	def get_train_valid(self, nVal):
		# Split our dataset into a training and validation set
		return self.photos[:nVal], self.photos[nVal:]


					
			





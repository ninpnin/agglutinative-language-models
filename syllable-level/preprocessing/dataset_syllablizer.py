import numpy as np
from vocab_builder import syllablize

def convert_to_syllables(data_filename, vocab_filename):
	print("Convert to syllables...")
	vocab = open(vocab_filename, "r").read().split(";")
	l = len(vocab)
	data = open(data_filename, "r").read().lower().split()

	data_arr = ""

	for d in data:
		d, s = syllablize(d, vocab)
		data_arr += " | " + s

	data_arr = data_arr[3:]
	data_arr = data_arr.replace("-", " ")
	print("Done!")
	print(data_arr)
	data_arr = data_arr.split()

	vocab_a = vocab + ["|"]
	index_arr = []
	for elem in data_arr:
		print(elem)
		index_arr.append(vocab_a.index(elem))

	return index_arr

def convert_to_indices(syllables, out_filename):
	# the model will take as input an integer matrix
	# of size (batch, input_length). The integers range
	# from 0 to syllable set size

	# This function converts dataset of syllables
	# into a list of syllable indices

	# The input matrix X is a list of lists of syllable indices
	# X := [[1,3,2,0,0,3], ... , [5,5,6,0,1,0]]
	# Size: (batch_size, input_length)

	# The output/labels matrix Y is is list of syllables
	# Y := [6,7,3, ... ,0,12,2]
	# Size: (batch_size)
	return []

def write_processed_data(syllables, filename):
	print("Write preprocessed data...")
	print(syllables)
	print("Done!")

def main():
	data_file = "testidata.txt"
	vocab_file = "vocab.txt"
	out_file = "data_preprocessed.txt"
	syllables = convert_to_syllables(data_file, vocab_file)
	write_processed_data(syllables, out_file)

if __name__ == "__main__":
	main()

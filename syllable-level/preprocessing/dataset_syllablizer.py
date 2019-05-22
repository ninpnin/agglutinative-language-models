import numpy as np

def convert_to_syllables(data_filename, vocab_filename, out_filename):
	print("Convert to syllables...")
	print("Done!")
	return []

def write_processed_data(syllables, filename):
	print("Write preprocessed data...")
	print("Done!")

def main():
	data_file = "data.txt"
	vocab_file = "vocab.txt"
	out_file = "data_preprocessed.txt"
	syllables = convert_to_syllables(data_file, vocab_file)
	write_processed_data(syllables, out_file)

if __name__ == "__main__":
	main()

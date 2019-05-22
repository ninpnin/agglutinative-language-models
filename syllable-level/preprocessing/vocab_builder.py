import numpy as np

def generate_vocab(in_filename):
	print("Generate vocab...")
	print("Done!")
	return []

def write_vocab(vocab, out_filename):
	print("Write vocab...")
	print("Done!")

def main():
	in_file = "data.txt"
	vocab_file = "vocab.txt"
	vocab = generate_vocab(in_file)
	write_vocab(vocab, vocab_file)


if __name__ == "__main__":
	main()

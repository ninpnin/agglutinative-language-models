import numpy as np
import re

def naive_syl_search(s):
	split = s.split()

	syllables = {}
	for word in split:
		l = len(word)
		for i in range(0, l):
			for j in range(i+1, l+1):
				substring = word[i:j]
				if substring in syllables:
					syllables[substring] = syllables[substring] + 1
				else:
					syllables[substring] = 1

	d = syllables.items()
	d = sorted(d, key=lambda x: x[1], reverse=True)
	return d[:5000]

def syllable_dijkstra(word, syls):
	available_syls = []
	l = len(word)
	for i in range(0, l):
		for j in range(i+1, l+1):
			substring = word[i:j]
			print(substring)
			if substring not in available_syls and substring in syls:
				available_syls.append(substring)
	print(syls)
	print(available_syls)

def generate_vocab(in_filename):
	print("Generate vocab...")
	print("Done!")
	f = open("whole_dataset.txt","r").read().lower()
	f = re.sub("[^a-zäö] ", "", f)
	syls = naive_syl_search(f)

	syls2 = []
	for el, val in syls:
		syls2.append(el)

	syllable_dijkstra("hegeisevä", syls2)
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

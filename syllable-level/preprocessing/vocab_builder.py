import numpy as np
import re

def custom_count(s1,s2):
	counter = 0
	l1, l2 = len(s1), len(s2)
	for i in range(l1-l2+1):
		s1_mod = s1[i:][:l2]
		if s1_mod == s2:
			counter += 1

	return counter

print(custom_count("ajaja", "aja"))
print(custom_count("jaja", "aja"))

print(custom_count("iiii", "iii"))
print(custom_count("iiiii", "iii"))
#math.log(0)
MAX_LEN = 4
def possible_syls(word, allow_multiple=False):
	syls = []
	l = len(word)
	for i in range(0, l):
		for j in range(i+1, min(i+1 + MAX_LEN, l+1)):
			substring = word[i:j]
			if substring not in syls or allow_multiple:
				syls.append(substring)
	return syls


def naive_syl_search(s):
	split = s.split()

	syllables = {}
	for word in split:
		possible = list(set(possible_syls(word, allow_multiple=True)))
		for syl in possible:
			if syl in syllables:
				syllables[syl] = syllables[syl] + custom_count(word, syl)
			else:
				syllables[syl] = custom_count(word, syl)

	d = syllables.items()
	d = sorted(d, key=lambda x: x[1], reverse=True)
	d = d[:5000]

	return d

def address_subsyls(s, syl_tuples):
	d = sorted(syl_tuples, key=lambda x: len(x[0]) * 1000000 + x[1]/1000, reverse=True)
	#print(d)

	d_2 = {}

	for ix, elems in enumerate(d):
		syllable, number = elems
		d_2[syllable] = s.count(syllable)
		s = s.replace(syllable, "")
		if syllable == "sinul" or syllable == "inull":
			print(syllable, d_2[syllable])

	d = sorted(d_2.items(), key=lambda x: x[1], reverse=True)[:500]
	print("<NEGATIVE>")
	for a,b in d:
		if b < 0 or True:
			print(a, b)
	print("</NEGATIVE>")


def syllablize(word, all_syls):
	possible = possible_syls(word)
	possible = set(possible) & set(all_syls)
	return syllable_dijkstra(word, list(possible))

def syllable_dijkstra(word, syls):
	interlap = syls

	def get_poss(subword):
		wordend = word[len(subword.replace("-","")):]

		curr_interlap = []
		for elem in interlap:
			if wordend[:len(elem)] == elem:
				#print(subword, elem, wordend[len(elem):])
				curr_interlap.append(subword + "-" + elem)

		return curr_interlap

	done = []
	subwords = list(interlap)
	for i in range(len(word)):

		filtered_subwords = []
		for subword in subwords:
			subword_r = subword.replace("-","")
			if subword_r == word:
				return i + 1, subword
			elif subword_r not in done:
				filtered_subwords.append(subword)
				done.append(subword_r)

		subwords = filtered_subwords


		#print(subwords)
		new_subwords = []
		for s in subwords:
			new_subwords = new_subwords + get_poss(s)

		subwords = new_subwords

	return -1, "none"




def generate_vocab(in_filename):
	print("Generate vocab...")
	print("Done!")
	f = open("whole_dataset.txt","r").read().lower()
	f = re.sub("[^a-zäö] \n", "", f)
	f = f.replace("\n", " ")
	f = f.replace(",", " ,")
	f = f.replace("-", "")
	syls = naive_syl_search(f)
	#address_subsyls(f, syls)

	syls_keys = []

	s = f.split()

	for syl, number in syls:
		syls_keys.append(syl)

	used_syls = {}
	for ix, word in enumerate(s):
		distance, split_str = syllablize(word, syls_keys)
		#print("Syllables needed", distance, split_str, len(word)/distance)

		split_str = split_str.split("-")
		for syl in split_str:
			if syl in used_syls:
				used_syls[syl] += 1
			else:
				used_syls[syl] = 1

		if ix % 1000 == 0:
			print("Index", ix, ", syls", len(used_syls))
			d_trunc = sorted(used_syls.items(), key=lambda x: x[1], reverse=True)[:50]
			print(d_trunc)

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

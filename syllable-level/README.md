# Syllable Level Models for Agglutinative Languages

```
sa-tun-nais-ge-ne-roi-tu-a teks-ti-ä
```

This folder is dedicated for the __syllable-level__ solutions for agglutinative language models.

As in the _stem_ and _word_ level counterparts, the primary goal of this module is to implement decent text generation.

## Why go with syllable level?

The pros in comparison with _stem_ and _word_ level models include

* __Easy and comprehensive representation of data:__ it is easy to convert any text into substrings or syllables, and if there are a sufficient number of them, nothing has to be excluded. Also, the trivial char-level representation exists as a subset of syllable level representation. These are true for pretty much any natural language dataset. 

* __Reasonable number of classes:__ syllable level representations are very unlikely to have a crazy number of classes to try to guess from. The linear transformations from the hidden state to the class space are tolerable, and there are tons of instances of each class in a reasonably large dataset.

Cons:

* __The need for longer RNN models:__ in terms of the number of the building blocks, syllable level representations are bound to be longer than their stem or word level counterparts. This inevitably leads to longer RNN chains that have more difficulties retaining information from _n_ characters ago.


## Approach

### Embedding 

## Things to Experiment with

### Syllable Embeddings

The number of syllables for a syllable level model is so high that inputting plain class vectors is unfeasible. Therefore, the binary class vectors of syllables have to be embedded into a subspace.


#### Word2Vec – Syllable2Vec?

With decent preprocessing, it might be possible to extend the Word2Vec methodology to syllables. This would provide a nice way to 

Some potential problems to tackle include what to do with the most common syllables, as well as how to address word borders and linebreaks.

### Syllable Set Size


### Neural Network Structure

#### Type of Neural Network




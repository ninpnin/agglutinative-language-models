# Stem Level Models for Agglutinative Languages

```
satunnaisgeneroi-tua teksti-ä
```

This folder is dedicated for the __stem-level__ solutions for agglutinative language models.

As in the _syllable_ and _word_ level counterparts, the primary goal of this module is to implement decent text generation.

## Why go with stem level?

The pros in comparison with _syllable_ and _word_ level models include

* __Mimicking of analytic languages:__ the stem level splits words into the stem and the inflection suffix. This largely resembles the structure of an analytic language: it's basically a bunch of uninflectable words and postpositions. As a consequence, models that work well with analytic languages should work well with stem level data as well. And due to English being the current _lingua franca_, these are plentiful.

* __Word2Vec (probably) works like a charm__: due to the analytic-like structure, stem level is bound to yield a great _word2vec_ embedding, probably an even better one than at word level. Experiments can be done with taking out inflections, word separators and/or punctuation.

Cons:

* __Complex and unpredictable preprocessing:__ A stem is not well defined for arbitrary datasets. It's not sure whether exception cases are rare enough not to screw up everything. Moreover, a plethora of options for heuristics are possible, which complicates the experimentation process. Linguistic knowledge is also relatively useless if dataset/vocabulary invariance is the objective.


## Approach

### Embedding 

## Things to experiment with

### Defining the concept 'stem'

In the grammatical sense, the stem of a word is the invariable basic structure, while inflections are variable suffixes that convey grammatical information. Hence, the stem-level approach tries to split the word up into two pieces. However, the stem might be the only component.

In order for the model to work, the definition of a stem does not need to match the grammatical definition. Instead, the broad grammatical logic of words that have variable endings works as a starting point for preprocessing. Different heuristics can be used and their performance can be compared.

### Stem vocabulary size

### Neural network structure

#### Type of the neural network





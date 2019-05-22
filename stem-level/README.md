# Stem Level Models for Agglutinative Languages

This folder is dedicated for the stem-level solutions for agglutinative language models.

As in the syllable and word level counterparts, the primary goal of this module is to implement decent text generation.

## Why go with stem level?

The pros in comparison with _syllable_ and _word_ level models include

* __Mimicing of analytic languages:__ stem level splits words into the stem and the inflection suffix. This largely resembles the structure of an analytic language: it's basically a bunch of uninflectable words and postpositions. As a consequence, models that work well with analytic should work well with the . And due to English being the current _lingua franca_, these are plentiful.

Cons:

* __Complex preprocessing:__ . Theoretically, this can be addressed with linguistic knowledge, but stuff like colloquialisms and new words make it unfeasible.


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




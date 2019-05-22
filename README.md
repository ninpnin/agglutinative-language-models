# Agglutinative Language Models

## Introduction

Due to a plethora of inflections, agglutinative languages, eg. Finnish, tend to have more words than analytic languages, eg. English. What is conveyed in word order and choice in an analytic language is the word changing up a bit in agglutinative languages:

'''
to (the) cup 
kuppi-in
'''

Even though these two phrases have the same meaning, they have a different number of words. This translates into larger vocabulary sizes of the training datasets, and thus a more difficult classification task.

## Objectives

* Produce meaningful text
* Understand words that are outside common vocabulary
* Be able to 

## Solution approaches

The core problem of too large vocabularies can be tackled with several strategies.

### Syllable level solutions

'''
kup-piin
sii-vo-an
'''

A suitable number of syllables should be chosen as a set of core syllables. The choice of syllables should minimize the redundance of the data: some letter combinations are more common than others, and some are impossible. The better this information can be directly included into the set of syllables, the more resources the neural network can use for understanding higher level patterns

Options to consider
* Syllable embedding using word2vec or similar
* Language specific properties that can be included in the syllable embedding
* What to do with uncommon syllables

### Stem level solutions

'''
kuppi-in
siivo-an
'''

### Word level solutions

'''
kuppiin
siivoan
'''

## Implementation and performance metrics

All of the solutions are implemented as an LSTM neural network in keras.

The task is 



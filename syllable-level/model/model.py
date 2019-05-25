import numpy as np
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import Dropout
from keras.layers import LSTM
from keras.layers import Embedding
from keras.callbacks import ModelCheckpoint
from keras.utils import np_utils
import keras
from math import log

# prefix of the data path
prefix = ""

# Toy data for quick testing
toydata = False
if toydata:
	# the model will take as input an integer matrix
	# of size (batch, input_length). The integers range
	# from 0 to syllable set size
	X = np.load(prefix + "keras-model/X_0.npy")[:500,:][:,:,0]
	Y = np.load(prefix + "keras-model/Y_0.npy")[:500,:]
else:
	X = np.load(prefix + "keras-model/X.npy")[:,:,0]
	Y = np.load(prefix + "keras-model/Y.npy")

print("Convert labels into categorical data...")
Y = np_utils.to_categorical(Y)
print("Done.")
#print(X.shape, Y.shape, y.shape)

print(Y)




random_embedding = True

if not random_embedding:
	# NOT RELEVANT ATM
	e_beginning = np.load(prefix + "data/embeddings/embedding-beginning.npy")
	e_end = np.load(prefix + "data/embeddings/embedding-end.npy")[:,:64]

	embedding_matrix = np.concatenate((e_beginning, e_end), axis=1)
	embedding_matrix = np.concatenate((embedding_matrix, np.random.rand(1,128)), axis=0)
	vocab_size = len(embedding_matrix)

	print(embedding_matrix.shape, vocab_size)
else:
	embedding_matrix = np.random.rand(syllable_num, 128)

e = Embedding(vocab_size, 128, weights=[embedding_matrix], input_length=20, trainable=False)


# define the LSTM model
model = Sequential()
model.add(e)
model.add(LSTM(256))
model.add(Dropout(0.1))

d = Dense(syllable_num, activation='softmax')
model.add(d)

# Import weights from earlier training
filename = "data/keras-checkpoints/weights-improvement-07-5.1608.hdf5"
model.load_weights(filename)

# Set weights for different classes
d.set_weights([embedding_matrix.T, U_log * 1.0])


model.compile(loss='categorical_crossentropy', optimizer='adam')
filepath = prefix + "data/keras-checkpoints/weights-improvement-{epoch:02d}-{loss:.4f}.hdf5"
checkpoint = ModelCheckpoint(filepath, monitor='loss', verbose=1, save_best_only=True, mode='min')
callbacks_list = [checkpoint]

model.fit(X, Y, epochs=20, batch_size=128, callbacks=callbacks_list)


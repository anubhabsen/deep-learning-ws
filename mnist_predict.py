import keras

(data_train, label_train), (data_test, label_test) = keras.datasets.mnist.load_data()

data_train = data_train.reshape(60000, 28 * 28)
data_test = data_test.reshape(10000, 28 * 28)

data_train = data_train.astype('float32')
data_test = data_test.astype('float32')

data_train /= 255.0
data_test /= 255.0

label_train = keras.utils.to_categorical(label_train, 10)
label_test = keras.utils.to_categorical(label_test, 10)

model = keras.models.Sequential()
model.add(keras.layers.Dense(512, activation='relu', input_shape=(28 * 28, )))
model.add(keras.layers.Dropout(0.25))
model.add(keras.layers.Dense(512, activation='relu'))
model.add(keras.layers.Dropout(0.25))
model.add(keras.layers.Dense(10, activation='softmax'))

model.summary()

model.compile(loss=keras.losses.categorical_crossentropy,
optimizer=keras.optimizers.Adadelta(),
metrics=['accuracy'])

model.fit(data_train, label_train,
			batch_size=128,
			epochs=25,
			verbose=2,
			validation_data=(data_test, label_test))

score = model.evaluate(data_test, label_test, verbose=2)
print('Test loss:', score[0])
print('Test accuracy:', score[1])

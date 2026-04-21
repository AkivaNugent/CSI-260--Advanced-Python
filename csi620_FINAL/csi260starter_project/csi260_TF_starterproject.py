import tensorflow as tf
import tensorflow_datasets as tfds
from PIL import Image
import numpy as np


"""MODEL STUFF"""
mnist = tf.keras.datasets.mnist

(x_train, y_train), (x_test, y_test) = mnist.load_data()
x_train, x_test = x_train / 255.0, x_test / 255.0

model = tf.keras.models.Sequential([
    tf.keras.layers.Flatten(input_shape=(28,28)),
    tf.keras.layers.Dense(128, activation = 'relu'),
    tf.keras.layers.Dropout(0.2),
    tf.keras.layers.Dense(10)
])

predictions = model(x_train[:1]).numpy()
tf.nn.softmax(predictions).numpy()

loss_fn = tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True)
loss_fn(y_train[:1], predictions).numpy()

model.compile(optimizer='adam',
              loss=loss_fn,
              metrics=['accuracy'])

model.fit(x_train, y_train, epochs=15)

model.evaluate(x_test, y_test, verbose=2)


"""IMAGE STUFF"""
img = Image.open("model_test_image.png").convert("L")
img = img.resize((28,28))

img_array = np.array(img) / 255
img_array = img_array[np.newaxis, ...]


"""PREDICTION"""
prediction = model(img_array)
predicted_digit = tf.argmax(prediction, axis=1).numpy()
print(predicted_digit)
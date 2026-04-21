import tensorflow as tf
import numpy as np
from tensorflow import keras

def house_model(y_new):
    """House pricing based on number of bedrooms. (50k + 50k/bedroom)"""
    xs = np.array([1.0, 2.0, 3.0, 4.0, 5.0, 10.0], dtype=float)
    ys = np.array([1.0, 1.5, 2.0, 2.5, 3.0,  5.5], dtype=float)

    model = tf.keras.Sequential([keras.layers.Dense(units=1, input_shape=[1])])
    model.compile(optimizer='sgd', loss='mean_squared_error')
    model.fit(xs, ys, epochs=500)

    return model.predict(np.array([y_new])).item()

prediction = 100000 * house_model([7]) # 7 bedrooms = ~400k
print(f"${prediction:,.0f}")
import tensorflow as tf

# Importing Keras from TensorFlow
from tensorflow import keras

fashion_mnist = keras.datasets.fashion_mnist
(train_images, train_labels), (test_images, test_labels) = fashion_mnist.load_data()

model = keras.Sequential([
    keras.layers.Flatten(input_shape=(28, 28)),
    keras.layers.Dense(128, activation=tf.nn.relu),
    keras.layers.Dense(10, activation=tf.nn.softmax)])

model.compile(optimizer=tf.optimizers.Adam(),  # Change tf.train.AdamOptimizer() to tf.optimizers.Adam()
              loss='sparse_categorical_crossentropy')

model.fit(train_images, train_labels, epochs=5)

test_loss, test_acc = model.evaluate(test_images, test_labels)

# Define my_images before predicting
# For example:
my_images = test_images[:5]
predictions = model.predict(my_images)
print(predictions)

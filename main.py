import tensorflow as tf
import numpy as np

print("TensorFlow version:", tf.__version__)
print("NumPy version:", np.__version__)
print("GPU available:", tf.config.list_physical_devices('GPU'))


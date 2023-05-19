import tensorflow as tf
from tensorflow import keras
from keras import layers
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split


# Prepare the data
# X is your input data, y is your target variable
# split your data into training and test sets
# normalize your data
# convert your data into tensors

# Load your data into a Pandas DataFrame
df = pd.read_csv('data.csv')

# Split your data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(df[['weight', 'surface_area', 'form', 'air_pressure', 'time']], df['time_to_hit_ground'], test_size=0.2, random_state=42)

# Normalize your data
X_train = (X_train - X_train.mean()) / X_train.std()
X_test = (X_test - X_train.mean()) / X_train.std()



x_train = np.array(X_train)
y_train = np.array(y_train)
x_test = np.array(X_test)
y_test = np.array(y_test)
X_train = tf.convert_to_tensor(X_train)
y_train = tf.convert_to_tensor(y_train)
X_test = tf.convert_to_tensor(X_test)
y_test = tf.convert_to_tensor(y_test)

# Build the model
model = keras.Sequential([
    layers.Dense(64, activation='relu', input_shape=[5]),
    layers.Dense(64, activation='relu'),
    layers.Dense(1)
])
model.compile(loss='mse', optimizer=tf.keras.optimizers.RMSprop(0.001), metrics=['mae'])

# Train the model
history = model.fit(X_train, y_train, epochs=500, batch_size=10, validation_split=0.2)

# Evaluate the model
test_loss, test_mae = model.evaluate(X_test, y_test)

# Make predictions
predictions = model.predict(X_test)

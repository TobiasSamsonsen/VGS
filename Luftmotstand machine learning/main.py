import tensorflow as tf
from tensorflow import keras
from keras import layers
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
import chardet


# Prepare the data
# X is your input data, y is your target variable
# split your data into training and test sets
# normalize your data
# convert your data into tensors

with open('Luftmotstand machine learning\Luftmotstand data for usage.csv', 'rb') as f:
    result = chardet.detect(f.read())

# Load your data into a Pandas DataFrame
df = pd.read_csv('Luftmotstand machine learning\Luftmotstand data for usage.csv', encoding=result['encoding'])

# Check for missing values
print(df.isnull().sum())

# Drop rows with missing values
df = df.dropna()

# Split your data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(df[['Vekt i gram', 'Areal i cm^2', 'Slipphoyde i cm']], df['Tid'], test_size=0.2, random_state=42)

# Normalize your data
# X_train = (X_train - X_train.mean()) / X_train.std()
# X_test = (X_test - X_train.mean()) / X_train.std()



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
    layers.Dense(4, activation='relu', input_shape=[3]),
    layers.Dense(16, activation='linear'),
    layers.Dense(8, activation='relu')
])
model.compile(loss='mse', optimizer=tf.keras.optimizers.Adam(0.001), metrics=['mae'])

# Train the model
history = model.fit(X_train, y_train, epochs=100, batch_size=64, validation_split=0.2, verbose=0)

# Evaluate the model
test_loss, test_mae = model.evaluate(X_test, y_test)

# Make predictions
while True:
    vekt = float(input("Vekt i gram: "))
    areal = float(input("Areal i cm^2: "))
    høyde = float(input("Høyde i cm: "))

    input_data = np.array([[vekt, areal, høyde]])

    predictions = model.predict(input_data)

    print("Beregnet tid til å treffe bakken:", predictions[0][0], "sekunder")
    print("-----------------------------------------------------")
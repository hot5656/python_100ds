import csv
import tensorflow as tf

from sklearn.model_selection import train_test_split

# Read data in from file
with open("banknotes.csv") as f:
    reader = csv.reader(f)
    next(reader)

    data = []
    for row in reader:
        data.append({
            "evidence": [float(cell) for cell in row[:4]],
            "label": 1 if row[4] == "0" else 0
        })

# Separate data into training and testing groups
evidence = [row["evidence"] for row in data]
labels = [row["label"] for row in data]
X_training, X_testing, y_training, y_testing = train_test_split(
    evidence, labels, test_size=0.4
)

# Create a neural network
# models : one API
# Sequential : 多層
model = tf.keras.models.Sequential()

# Add a hidden layer with 8 units, with ReLU activation
# 8 : 8 hide unit
# 4 : 4 input data
# relu : active function
model.add(tf.keras.layers.Dense(8, input_shape=(4,), activation="relu"))

# Add output layer with 1 unit, with sigmoid activation
# 1 : 1 output
model.add(tf.keras.layers.Dense(1, activation="sigmoid"))

# Train neural network
# optimizer="adam" :　select optimizer model
# loss="binary_crossentropy" : select loss model
# metrics=["accuracy"] : 評估準確性
model.compile(
    optimizer="adam",
    loss="binary_crossentropy",
    metrics=["accuracy"]
)
# training 20 times
model.fit(X_training, y_training, epochs=20)

# Evaluate how well model performs
model.evaluate(X_testing, y_testing, verbose=2)

import tensorflow as tf

def load_model(path):
    def mish(inputs):
        x = tf.nn.softplus(inputs)
        x = tf.nn.tanh(x)
        x = tf.multiply(x, inputs)
        return x

    model = tf.keras.Sequential([
        tf.keras.layers.Input(shape=(160, 160, 3)),
        tf.keras.layers.Conv2D(64, kernel_size=(3, 3), activation=mish, padding='same'),
        tf.keras.layers.Conv2D(64, kernel_size=(3, 3), activation=mish, padding='same'),
        tf.keras.layers.MaxPool2D(pool_size=(2, 2), strides=(2, 2)),
        tf.keras.layers.Conv2D(128, kernel_size=(3, 3), activation=mish, padding='same'),
        tf.keras.layers.Conv2D(128, kernel_size=(3, 3), activation=mish, padding='same'),
        tf.keras.layers.MaxPool2D(pool_size=(2, 2), strides=(2, 2)),
        tf.keras.layers.Dropout(0.1),
        tf.keras.layers.Conv2D(128, kernel_size=(3, 3), activation=mish, padding='same'),
        tf.keras.layers.Conv2D(128, kernel_size=(3, 3), activation=mish, padding='same'),
        tf.keras.layers.MaxPool2D(pool_size=(2, 2), strides=(2, 2)),
        tf.keras.layers.Conv2D(256, kernel_size=(3, 3), activation=mish, padding='same'),
        tf.keras.layers.Conv2D(256, kernel_size=(3, 3), activation=mish, padding='same'),
        tf.keras.layers.Conv2D(256, kernel_size=(3, 3), activation=mish, padding='same'),
        tf.keras.layers.MaxPool2D(pool_size=(2, 2), strides=(2, 2)),
        tf.keras.layers.Dropout(0.2),
        #tf.keras.layers.BatchNormalization(),
        tf.keras.layers.Flatten(),
        tf.keras.layers.Dense(512, activation=mish),
        tf.keras.layers.Dense(1024, activation=mish, kernel_regularizer=tf.keras.regularizers.l1_l2(0.0001)),
        #tf.keras.layers.Dense(1024, activation=mish, kernel_regularizer=tf.keras.regularizers.l1_l2(0.001)),
        tf.keras.layers.Dropout(0.5),
        tf.keras.layers.Dense(7, activation='softmax')
    ])

    model.load_weights(path)

    return model


import matplotlib.pyplot as plt
import tensorflow as tf
import numpy as np
import pathlib
import os

from tensorflow import keras
from tensorflow.keras import layers
from tensorflow.keras.models import Sequential, load_model


# Define uma altura e comprimento padrao para as imagens
img_width = 260
img_height = 180
batch_size = 32

# Carrega um dataset de um link
def load_dataset_from_link(dataset_url):
    # Baixa a pasta zipada e extrai
    data_dir = tf.keras.utils.get_file('imagens_escola', origin=dataset_url, untar=True)
    data_dir = pathlib.Path(data_dir)

    # Retorna a lista de diretorios (classes) com suas imagens
    return data_dir


# Configura os datasets de treino e validação
def configure_dataset_data(data_dir):
 # Pega 80% das imagens do dataset para treinamento
    train_ds = tf.keras.utils.image_dataset_from_directory(
        data_dir,
        validation_split = 0.2,
        subset = "training",
        seed = 123,
        image_size = (img_height, img_width),
        batch_size = batch_size,
    )

    # Pega 20% para validacao
    val_ds = tf.keras.utils.image_dataset_from_directory(
        data_dir,
        validation_split = 0.2,
        subset = "validation",
        seed = 123,
        image_size = (img_height, img_width),
        batch_size = batch_size
    )

    # Pega as classes que existem no DS
    class_names = train_ds.class_names

    # Deixa as imagens normalizadas com AUTOTUNE
    AUTOTUNE = tf.data.AUTOTUNE
    train_ds = train_ds.cache().shuffle(1000).prefetch(buffer_size=AUTOTUNE)
    val_ds = val_ds.prefetch(buffer_size=AUTOTUNE)

    # Retorna os datasets e o nome das classes
    return {
        "train_ds": train_ds, 
        "val_ds": val_ds,
        "class_names": class_names,
    }


# Cria um modelo
def create_model(train_ds, val_ds, class_names):
    # --> Define as etapas do model
    model = Sequential([
        layers.Rescaling(1./255, input_shape=(img_height, img_width, 3)),
        layers.Conv2D(16, 3, padding="same", activation="relu"),
        layers.MaxPooling2D(),
        layers.Conv2D(32, 3, padding="same", activation="relu"),
        layers.MaxPooling2D(),
        layers.Conv2D(64, 3, padding="same", activation="relu"),
        layers.MaxPooling2D(),
        layers.Flatten(),
        layers.Dense(len(class_names))
    ])

    # --> Compila
    model.compile(optimizer="adam",
                loss = tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
                metrics=['accuracy'])
    
    # --> Treina
    epochs = 7
    model.fit(
    train_ds,
        validation_data = val_ds,
        epochs = epochs
    )

    return model


def load_saved_model(model_dir):
    return load_model(model_dir)


# Faz uma prediction
def predict(img_path, model, labels):
    model = load_model(model)

    img = tf.keras.utils.load_img(
        img_path, target_size=(img_height, img_width)
    )

    img_array = tf.keras.utils.img_to_array(img)
    img_array = tf.expand_dims(img_array, 0)

    # --> Prediz
    prediction = model.predict(img_array)
    score = tf.nn.softmax(prediction[0])

    # --> Retorna a prediction
    return (
        "Você está na '{}' com uma probabilidade de {:.2f}"
        .format(labels[np.argmax(score)], 100 * np.max(score))
    )
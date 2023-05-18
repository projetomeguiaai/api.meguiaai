import matplotlib.pyplot as plt
import PIL
import os
import numpy as np
import tensorflow as tf
import pathlib

from tensorflow import keras
from tensorflow.keras import layers
from tensorflow.keras.models import Sequential

def run_model():
    # Baixa Dataset das imagens a serem treinadas
    dataset_url = "https://drive.google.com/uc?export=download&id=1DUtezZYuhaYJCagw4yfcRRfDsEbYB3-9"
    data_dir = tf.keras.utils.get_file('imagens_escola', origin=dataset_url, untar=True)
    data_dir = pathlib.Path(data_dir)

    # Lista e conta as imagens
    images_list = list(data_dir.glob('*/*'))
    images_count = len(images_list)

    print(images_count)

    # Define uma altura e comprimento padrao
    img_width = 260
    img_height = 180
    batch_size = 32

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

    print(class_names)


    # Deixa as imagens normalizadas com AUTOTUNE
    AUTOTUNE = tf.data.AUTOTUNE

    train_ds = train_ds.cache().shuffle(1000).prefetch(buffer_size=AUTOTUNE)
    val_ds = val_ds.prefetch(buffer_size=AUTOTUNE)

    normalization_layer = layers.Rescaling(1./255)

    normalized_ds = train_ds.map(lambda x, y: (normalization_layer(x), y))
    image_batch, labels_batch = next(iter(normalized_ds))
    first_image = image_batch[0]


    # Cria um model
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

    # --> Valida
    model.compile(optimizer="adam",
                loss = tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
                metrics=['accuracy'])

    # --> Sumariza
    model.summary()

    # --> Testa com 7 etapas (epochs)
    epochs = 7
    history = model.fit(
        train_ds,
        validation_data = val_ds,
        epochs = epochs
    )


    # Faz uma prediction

    ## Baixa a imagem
    pred_image_path = "https://drive.google.com/uc?export=download&id=1I3uzeJHQ0T0_DPKMs0n2S6K9ulZuF3gX"

    data_dir = tf.keras.utils.get_file('testes', origin=pred_image_path, untar=True)
    data_dir = pathlib.Path(data_dir)
    pred_images = list(data_dir.glob('*'))
    pred_images_count = len(pred_images)

    print(pred_images_count)

    img = tf.keras.utils.load_img(
        pred_images[5], target_size=(img_height, img_width)
    )

    img_array = tf.keras.utils.img_to_array(img)
    img_array = tf.expand_dims(img_array, 0)

    predictions = model.predict(img_array)
    score = tf.nn.softmax(predictions[0])

    return (
        "This image most likely belongs to '{}' with a {:.2f} percent confidence."
        .format(class_names[np.argmax(score)], 100 * np.max(score))
    )
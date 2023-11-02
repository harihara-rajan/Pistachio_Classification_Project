import os 
import urllib.request as request
from zipfile import ZipFile
import tensorflow as tf
from src.cnnClassifier.entity.config_entity import BaseModelConfig
from pathlib import Path

class BaseModel:
    def __init__(self,  config: BaseModelConfig):
        self.config = config
    
    def get_base_model(self):
        self.model = tf.keras.applications.vgg16.VGG16(input_shape=self.config.params_image_size,
            weights=self.config.params_weight,
            include_top=self.config.params_include_top,
        )
        self.save_model(path=self.config.base_model_path, model=self.model)

    # You call the static method using the class name BaseModel._full_model(...)
    # It doesn't require an instance of the class to be called and can be
    # accessed directly from the class itself.
    @staticmethod 
    def _full_model(model, classes, freezeall, freezetill, learning_rate):
        if freezeall:
            for layers in model.layers:
                layers.trainable = False
        elif (freezetill is not None) and (freezetill > 0):
            for layers in model.layers[:-freezetill]:
                layers.trainable = False
        
        dense1 = tf.keras.layers.Dense(5, activation='relu')(model.layers[-1].output)
        flatten = tf.keras.layers.Flatten()(dense1)
        final_layer = tf.keras.layers.Dense(classes, activation='softmax')(flatten)
        full_model = tf.keras.Model(inputs=model.input, outputs=final_layer)
        full_model.compile(optimizer=tf.keras.optimizers.Adam(learning_rate=learning_rate), 
        loss='categorical_crossentropy', metrics=['accuracy'])

        full_model.summary()
        return full_model

    def update_base_model(self):
        
        self.full_model = self._full_model(
            model=self.model,
            classes=self.config.params_classes,
            freezeall=True,
            freezetill=None,
            learning_rate=self.config.params_learning_rate
        )
        self.save_model(path=self.config.update_base_model_path, model=self.full_model)
    
    @staticmethod
    def save_model(path:Path, model:tf.keras.Model):
        model.save(path)
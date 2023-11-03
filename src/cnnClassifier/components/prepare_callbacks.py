import tensorflow as tf
from pathlib import Path
from src.cnnClassifier.entity.config_entity import PrepareCallbacksConfig
class PrepareCallbacks:
    def __init__(self,  config: PrepareCallbacksConfig):
        self.config = config
    
    def model_checkpoint_callbacks(self)-> tf.keras.callbacks.ModelCheckpoint:
        model_checkpoint = tf.keras.callbacks.ModelCheckpoint(
            filepath=self.config.checkpoint_model_file_path,
            monitor='val_loss',
            verbose=1,
            save_best_only=True,
            save_weights_only=True,
            mode='auto',
            save_freq="epoch")
        
        return model_checkpoint

    def early_stopping_callbacks(self)-> tf.keras.callbacks.EarlyStopping:
        early_stopping = tf.keras.callbacks.EarlyStopping(
            monitor='val_loss',
            min_delta=0,
            patience=self.config.patience,
            verbose=1,
            mode='auto',
            restore_best_weights=True)
        
        return early_stopping
    
    def tensorboard_callbacks(self)-> tf.keras.callbacks.TensorBoard:
        log_dir = str(Path(self.config.tensorboard_root_log_dir))
        tb_callbacks = tf.keras.callbacks.TensorBoard(log_dir=log_dir,write_images=True)
        return tb_callbacks
    
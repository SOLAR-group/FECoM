import matplotlib.pyplot as plt
import numpy as np
import os
import tensorflow as tf
import sys
from tool.patching.patching_config import EXPERIMENT_DIR
from tool.measurement.execution import before_execution as before_execution_INSERTED_INTO_SCRIPT
from tool.measurement.execution import after_execution as after_execution_INSERTED_INTO_SCRIPT
from tool.experiment.experiment_kinds import ExperimentKinds
experiment_number = sys.argv[1]
experiment_project = sys.argv[2]
EXPERIMENT_FILE_PATH = EXPERIMENT_DIR / ExperimentKinds.METHOD_LEVEL.value / experiment_project / f'experiment-{experiment_number}.json'
_URL = 'https://storage.googleapis.com/mledu-datasets/cats_and_dogs_filtered.zip'
start_times_INSERTED_INTO_SCRIPT = before_execution_INSERTED_INTO_SCRIPT(experiment_file_path=EXPERIMENT_FILE_PATH, function_to_run='tensorflow.keras.utils.get_file()')
path_to_zip = tf.keras.utils.get_file('cats_and_dogs.zip', origin=_URL, extract=True)
after_execution_INSERTED_INTO_SCRIPT(start_times=start_times_INSERTED_INTO_SCRIPT, experiment_file_path=EXPERIMENT_FILE_PATH, function_to_run='tensorflow.keras.utils.get_file()', method_object=None, function_args=['cats_and_dogs.zip'], function_kwargs={'origin': _URL, 'extract': True})
PATH = os.path.join(os.path.dirname(path_to_zip), 'cats_and_dogs_filtered')
train_dir = os.path.join(PATH, 'train')
validation_dir = os.path.join(PATH, 'validation')
BATCH_SIZE = 32
IMG_SIZE = (160, 160)
start_times_INSERTED_INTO_SCRIPT = before_execution_INSERTED_INTO_SCRIPT(experiment_file_path=EXPERIMENT_FILE_PATH, function_to_run='tensorflow.keras.utils.image_dataset_from_directory()')
train_dataset = tf.keras.utils.image_dataset_from_directory(train_dir, shuffle=True, batch_size=BATCH_SIZE, image_size=IMG_SIZE)
after_execution_INSERTED_INTO_SCRIPT(start_times=start_times_INSERTED_INTO_SCRIPT, experiment_file_path=EXPERIMENT_FILE_PATH, function_to_run='tensorflow.keras.utils.image_dataset_from_directory()', method_object=None, function_args=[train_dir], function_kwargs={'shuffle': True, 'batch_size': BATCH_SIZE, 'image_size': IMG_SIZE})
start_times_INSERTED_INTO_SCRIPT = before_execution_INSERTED_INTO_SCRIPT(experiment_file_path=EXPERIMENT_FILE_PATH, function_to_run='tensorflow.keras.utils.image_dataset_from_directory()')
validation_dataset = tf.keras.utils.image_dataset_from_directory(validation_dir, shuffle=True, batch_size=BATCH_SIZE, image_size=IMG_SIZE)
after_execution_INSERTED_INTO_SCRIPT(start_times=start_times_INSERTED_INTO_SCRIPT, experiment_file_path=EXPERIMENT_FILE_PATH, function_to_run='tensorflow.keras.utils.image_dataset_from_directory()', method_object=None, function_args=[validation_dir], function_kwargs={'shuffle': True, 'batch_size': BATCH_SIZE, 'image_size': IMG_SIZE})
class_names = train_dataset.class_names
plt.figure(figsize=(10, 10))
for (images, labels) in train_dataset.take(1):
    for i in range(9):
        ax = plt.subplot(3, 3, i + 1)
        plt.imshow(images[i].numpy().astype('uint8'))
        plt.title(class_names[labels[i]])
        plt.axis('off')
start_times_INSERTED_INTO_SCRIPT = before_execution_INSERTED_INTO_SCRIPT(experiment_file_path=EXPERIMENT_FILE_PATH, function_to_run='tensorflow.data.experimental.cardinality()')
val_batches = tf.data.experimental.cardinality(validation_dataset)
after_execution_INSERTED_INTO_SCRIPT(start_times=start_times_INSERTED_INTO_SCRIPT, experiment_file_path=EXPERIMENT_FILE_PATH, function_to_run='tensorflow.data.experimental.cardinality()', method_object=None, function_args=[validation_dataset], function_kwargs=None)
start_times_INSERTED_INTO_SCRIPT = before_execution_INSERTED_INTO_SCRIPT(experiment_file_path=EXPERIMENT_FILE_PATH, function_to_run='tensorflow.keras.utils.image_dataset_from_directory.take()')
test_dataset = validation_dataset.take(val_batches // 5)
after_execution_INSERTED_INTO_SCRIPT(start_times=start_times_INSERTED_INTO_SCRIPT, experiment_file_path=EXPERIMENT_FILE_PATH, function_to_run='tensorflow.keras.utils.image_dataset_from_directory.take()', method_object=validation_dataset, function_args=[val_batches // 5], function_kwargs=None)
start_times_INSERTED_INTO_SCRIPT = before_execution_INSERTED_INTO_SCRIPT(experiment_file_path=EXPERIMENT_FILE_PATH, function_to_run='tensorflow.keras.utils.image_dataset_from_directory.skip()')
validation_dataset = validation_dataset.skip(val_batches // 5)
after_execution_INSERTED_INTO_SCRIPT(start_times=start_times_INSERTED_INTO_SCRIPT, experiment_file_path=EXPERIMENT_FILE_PATH, function_to_run='tensorflow.keras.utils.image_dataset_from_directory.skip()', method_object=validation_dataset, function_args=[val_batches // 5], function_kwargs=None)
print('Number of validation batches: %d' % tf.data.experimental.cardinality(validation_dataset))
print('Number of test batches: %d' % tf.data.experimental.cardinality(test_dataset))
AUTOTUNE = tf.data.AUTOTUNE
start_times_INSERTED_INTO_SCRIPT = before_execution_INSERTED_INTO_SCRIPT(experiment_file_path=EXPERIMENT_FILE_PATH, function_to_run='tensorflow.keras.utils.image_dataset_from_directory.prefetch()')
train_dataset = train_dataset.prefetch(buffer_size=AUTOTUNE)
after_execution_INSERTED_INTO_SCRIPT(start_times=start_times_INSERTED_INTO_SCRIPT, experiment_file_path=EXPERIMENT_FILE_PATH, function_to_run='tensorflow.keras.utils.image_dataset_from_directory.prefetch()', method_object=train_dataset, function_args=None, function_kwargs={'buffer_size': AUTOTUNE})
start_times_INSERTED_INTO_SCRIPT = before_execution_INSERTED_INTO_SCRIPT(experiment_file_path=EXPERIMENT_FILE_PATH, function_to_run='tensorflow.keras.utils.image_dataset_from_directory.skip.prefetch()')
validation_dataset = validation_dataset.prefetch(buffer_size=AUTOTUNE)
after_execution_INSERTED_INTO_SCRIPT(start_times=start_times_INSERTED_INTO_SCRIPT, experiment_file_path=EXPERIMENT_FILE_PATH, function_to_run='tensorflow.keras.utils.image_dataset_from_directory.skip.prefetch()', method_object=validation_dataset, function_args=None, function_kwargs={'buffer_size': AUTOTUNE})
start_times_INSERTED_INTO_SCRIPT = before_execution_INSERTED_INTO_SCRIPT(experiment_file_path=EXPERIMENT_FILE_PATH, function_to_run='tensorflow.keras.utils.image_dataset_from_directory.take.prefetch()')
test_dataset = test_dataset.prefetch(buffer_size=AUTOTUNE)
after_execution_INSERTED_INTO_SCRIPT(start_times=start_times_INSERTED_INTO_SCRIPT, experiment_file_path=EXPERIMENT_FILE_PATH, function_to_run='tensorflow.keras.utils.image_dataset_from_directory.take.prefetch()', method_object=test_dataset, function_args=None, function_kwargs={'buffer_size': AUTOTUNE})
start_times_INSERTED_INTO_SCRIPT = before_execution_INSERTED_INTO_SCRIPT(experiment_file_path=EXPERIMENT_FILE_PATH, function_to_run='tensorflow.keras.Sequential()')
data_augmentation = tf.keras.Sequential([tf.keras.layers.RandomFlip('horizontal'), tf.keras.layers.RandomRotation(0.2)])
after_execution_INSERTED_INTO_SCRIPT(start_times=start_times_INSERTED_INTO_SCRIPT, experiment_file_path=EXPERIMENT_FILE_PATH, function_to_run='tensorflow.keras.Sequential()', method_object=None, function_args=[[tf.keras.layers.RandomFlip('horizontal'), tf.keras.layers.RandomRotation(0.2)]], function_kwargs=None)
for (image, _) in train_dataset.take(1):
    plt.figure(figsize=(10, 10))
    first_image = image[0]
    for i in range(9):
        ax = plt.subplot(3, 3, i + 1)
        start_times_INSERTED_INTO_SCRIPT = before_execution_INSERTED_INTO_SCRIPT(experiment_file_path=EXPERIMENT_FILE_PATH, function_to_run='tensorflow.keras.Sequential()')
        augmented_image = data_augmentation(tf.expand_dims(first_image, 0))
        after_execution_INSERTED_INTO_SCRIPT(start_times=start_times_INSERTED_INTO_SCRIPT, experiment_file_path=EXPERIMENT_FILE_PATH, function_to_run='tensorflow.keras.Sequential()', method_object=data_augmentation, function_args=[tf.expand_dims(first_image, 0)], function_kwargs=None)
        plt.imshow(augmented_image[0] / 255)
        plt.axis('off')
preprocess_input = tf.keras.applications.mobilenet_v2.preprocess_input
start_times_INSERTED_INTO_SCRIPT = before_execution_INSERTED_INTO_SCRIPT(experiment_file_path=EXPERIMENT_FILE_PATH, function_to_run='tensorflow.keras.layers.Rescaling()')
rescale = tf.keras.layers.Rescaling(1.0 / 127.5, offset=-1)
after_execution_INSERTED_INTO_SCRIPT(start_times=start_times_INSERTED_INTO_SCRIPT, experiment_file_path=EXPERIMENT_FILE_PATH, function_to_run='tensorflow.keras.layers.Rescaling()', method_object=None, function_args=[1.0 / 127.5], function_kwargs={'offset': -1})
IMG_SHAPE = IMG_SIZE + (3,)
start_times_INSERTED_INTO_SCRIPT = before_execution_INSERTED_INTO_SCRIPT(experiment_file_path=EXPERIMENT_FILE_PATH, function_to_run='tensorflow.keras.applications.MobileNetV2()')
base_model = tf.keras.applications.MobileNetV2(input_shape=IMG_SHAPE, include_top=False, weights='imagenet')
after_execution_INSERTED_INTO_SCRIPT(start_times=start_times_INSERTED_INTO_SCRIPT, experiment_file_path=EXPERIMENT_FILE_PATH, function_to_run='tensorflow.keras.applications.MobileNetV2()', method_object=None, function_args=None, function_kwargs={'input_shape': IMG_SHAPE, 'include_top': False, 'weights': 'imagenet'})
(image_batch, label_batch) = next(iter(train_dataset))
start_times_INSERTED_INTO_SCRIPT = before_execution_INSERTED_INTO_SCRIPT(experiment_file_path=EXPERIMENT_FILE_PATH, function_to_run='tensorflow.keras.applications.MobileNetV2()')
feature_batch = base_model(image_batch)
after_execution_INSERTED_INTO_SCRIPT(start_times=start_times_INSERTED_INTO_SCRIPT, experiment_file_path=EXPERIMENT_FILE_PATH, function_to_run='tensorflow.keras.applications.MobileNetV2()', method_object=base_model, function_args=[image_batch], function_kwargs=None)
print(feature_batch.shape)
base_model.trainable = False
start_times_INSERTED_INTO_SCRIPT = before_execution_INSERTED_INTO_SCRIPT(experiment_file_path=EXPERIMENT_FILE_PATH, function_to_run='tensorflow.keras.applications.MobileNetV2.summary()')
base_model.summary()
after_execution_INSERTED_INTO_SCRIPT(start_times=start_times_INSERTED_INTO_SCRIPT, experiment_file_path=EXPERIMENT_FILE_PATH, function_to_run='tensorflow.keras.applications.MobileNetV2.summary()', method_object=base_model, function_args=None, function_kwargs=None)
start_times_INSERTED_INTO_SCRIPT = before_execution_INSERTED_INTO_SCRIPT(experiment_file_path=EXPERIMENT_FILE_PATH, function_to_run='tensorflow.keras.layers.GlobalAveragePooling2D()')
global_average_layer = tf.keras.layers.GlobalAveragePooling2D()
after_execution_INSERTED_INTO_SCRIPT(start_times=start_times_INSERTED_INTO_SCRIPT, experiment_file_path=EXPERIMENT_FILE_PATH, function_to_run='tensorflow.keras.layers.GlobalAveragePooling2D()', method_object=None, function_args=None, function_kwargs=None)
start_times_INSERTED_INTO_SCRIPT = before_execution_INSERTED_INTO_SCRIPT(experiment_file_path=EXPERIMENT_FILE_PATH, function_to_run='tensorflow.keras.layers.GlobalAveragePooling2D()')
feature_batch_average = global_average_layer(feature_batch)
after_execution_INSERTED_INTO_SCRIPT(start_times=start_times_INSERTED_INTO_SCRIPT, experiment_file_path=EXPERIMENT_FILE_PATH, function_to_run='tensorflow.keras.layers.GlobalAveragePooling2D()', method_object=global_average_layer, function_args=[feature_batch], function_kwargs=None)
print(feature_batch_average.shape)
start_times_INSERTED_INTO_SCRIPT = before_execution_INSERTED_INTO_SCRIPT(experiment_file_path=EXPERIMENT_FILE_PATH, function_to_run='tensorflow.keras.layers.Dense()')
prediction_layer = tf.keras.layers.Dense(1)
after_execution_INSERTED_INTO_SCRIPT(start_times=start_times_INSERTED_INTO_SCRIPT, experiment_file_path=EXPERIMENT_FILE_PATH, function_to_run='tensorflow.keras.layers.Dense()', method_object=None, function_args=[1], function_kwargs=None)
start_times_INSERTED_INTO_SCRIPT = before_execution_INSERTED_INTO_SCRIPT(experiment_file_path=EXPERIMENT_FILE_PATH, function_to_run='tensorflow.keras.layers.Dense()')
prediction_batch = prediction_layer(feature_batch_average)
after_execution_INSERTED_INTO_SCRIPT(start_times=start_times_INSERTED_INTO_SCRIPT, experiment_file_path=EXPERIMENT_FILE_PATH, function_to_run='tensorflow.keras.layers.Dense()', method_object=prediction_layer, function_args=[feature_batch_average], function_kwargs=None)
print(prediction_batch.shape)
start_times_INSERTED_INTO_SCRIPT = before_execution_INSERTED_INTO_SCRIPT(experiment_file_path=EXPERIMENT_FILE_PATH, function_to_run='tensorflow.keras.Input()')
inputs = tf.keras.Input(shape=(160, 160, 3))
after_execution_INSERTED_INTO_SCRIPT(start_times=start_times_INSERTED_INTO_SCRIPT, experiment_file_path=EXPERIMENT_FILE_PATH, function_to_run='tensorflow.keras.Input()', method_object=None, function_args=None, function_kwargs={'shape': (160, 160, 3)})
start_times_INSERTED_INTO_SCRIPT = before_execution_INSERTED_INTO_SCRIPT(experiment_file_path=EXPERIMENT_FILE_PATH, function_to_run='tensorflow.keras.Sequential()')
x = data_augmentation(inputs)
after_execution_INSERTED_INTO_SCRIPT(start_times=start_times_INSERTED_INTO_SCRIPT, experiment_file_path=EXPERIMENT_FILE_PATH, function_to_run='tensorflow.keras.Sequential()', method_object=data_augmentation, function_args=[inputs], function_kwargs=None)
x = preprocess_input(x)
start_times_INSERTED_INTO_SCRIPT = before_execution_INSERTED_INTO_SCRIPT(experiment_file_path=EXPERIMENT_FILE_PATH, function_to_run='tensorflow.keras.applications.MobileNetV2()')
x = base_model(x, training=False)
after_execution_INSERTED_INTO_SCRIPT(start_times=start_times_INSERTED_INTO_SCRIPT, experiment_file_path=EXPERIMENT_FILE_PATH, function_to_run='tensorflow.keras.applications.MobileNetV2()', method_object=base_model, function_args=[x], function_kwargs={'training': False})
start_times_INSERTED_INTO_SCRIPT = before_execution_INSERTED_INTO_SCRIPT(experiment_file_path=EXPERIMENT_FILE_PATH, function_to_run='tensorflow.keras.layers.GlobalAveragePooling2D()')
x = global_average_layer(x)
after_execution_INSERTED_INTO_SCRIPT(start_times=start_times_INSERTED_INTO_SCRIPT, experiment_file_path=EXPERIMENT_FILE_PATH, function_to_run='tensorflow.keras.layers.GlobalAveragePooling2D()', method_object=global_average_layer, function_args=[x], function_kwargs=None)
start_times_INSERTED_INTO_SCRIPT = before_execution_INSERTED_INTO_SCRIPT(experiment_file_path=EXPERIMENT_FILE_PATH, function_to_run='tensorflow.keras.layers.Dropout(0.2)()')
x = tf.keras.layers.Dropout(0.2)(x)
after_execution_INSERTED_INTO_SCRIPT(start_times=start_times_INSERTED_INTO_SCRIPT, experiment_file_path=EXPERIMENT_FILE_PATH, function_to_run='tensorflow.keras.layers.Dropout(0.2)()', method_object=None, function_args=[x], function_kwargs=None)
start_times_INSERTED_INTO_SCRIPT = before_execution_INSERTED_INTO_SCRIPT(experiment_file_path=EXPERIMENT_FILE_PATH, function_to_run='tensorflow.keras.layers.Dense()')
outputs = prediction_layer(x)
after_execution_INSERTED_INTO_SCRIPT(start_times=start_times_INSERTED_INTO_SCRIPT, experiment_file_path=EXPERIMENT_FILE_PATH, function_to_run='tensorflow.keras.layers.Dense()', method_object=prediction_layer, function_args=[x], function_kwargs=None)
start_times_INSERTED_INTO_SCRIPT = before_execution_INSERTED_INTO_SCRIPT(experiment_file_path=EXPERIMENT_FILE_PATH, function_to_run='tensorflow.keras.Model()')
model = tf.keras.Model(inputs, outputs)
after_execution_INSERTED_INTO_SCRIPT(start_times=start_times_INSERTED_INTO_SCRIPT, experiment_file_path=EXPERIMENT_FILE_PATH, function_to_run='tensorflow.keras.Model()', method_object=None, function_args=[inputs, outputs], function_kwargs=None)
base_learning_rate = 0.0001
start_times_INSERTED_INTO_SCRIPT = before_execution_INSERTED_INTO_SCRIPT(experiment_file_path=EXPERIMENT_FILE_PATH, function_to_run='tensorflow.keras.Model.compile()')
model.compile(optimizer=tf.keras.optimizers.Adam(learning_rate=base_learning_rate), loss=tf.keras.losses.BinaryCrossentropy(from_logits=True), metrics=['accuracy'])
after_execution_INSERTED_INTO_SCRIPT(start_times=start_times_INSERTED_INTO_SCRIPT, experiment_file_path=EXPERIMENT_FILE_PATH, function_to_run='tensorflow.keras.Model.compile()', method_object=model, function_args=None, function_kwargs={'optimizer': tf.keras.optimizers.Adam(learning_rate=base_learning_rate), 'loss': tf.keras.losses.BinaryCrossentropy(from_logits=True), 'metrics': ['accuracy']})
start_times_INSERTED_INTO_SCRIPT = before_execution_INSERTED_INTO_SCRIPT(experiment_file_path=EXPERIMENT_FILE_PATH, function_to_run='tensorflow.keras.Model.summary()')
model.summary()
after_execution_INSERTED_INTO_SCRIPT(start_times=start_times_INSERTED_INTO_SCRIPT, experiment_file_path=EXPERIMENT_FILE_PATH, function_to_run='tensorflow.keras.Model.summary()', method_object=model, function_args=None, function_kwargs=None)
len(model.trainable_variables)
initial_epochs = 10
start_times_INSERTED_INTO_SCRIPT = before_execution_INSERTED_INTO_SCRIPT(experiment_file_path=EXPERIMENT_FILE_PATH, function_to_run='tensorflow.keras.Model.evaluate()')
(loss0, accuracy0) = model.evaluate(validation_dataset)
after_execution_INSERTED_INTO_SCRIPT(start_times=start_times_INSERTED_INTO_SCRIPT, experiment_file_path=EXPERIMENT_FILE_PATH, function_to_run='tensorflow.keras.Model.evaluate()', method_object=model, function_args=[validation_dataset], function_kwargs=None)
print('initial loss: {:.2f}'.format(loss0))
print('initial accuracy: {:.2f}'.format(accuracy0))
start_times_INSERTED_INTO_SCRIPT = before_execution_INSERTED_INTO_SCRIPT(experiment_file_path=EXPERIMENT_FILE_PATH, function_to_run='tensorflow.keras.Model.fit()')
history = model.fit(train_dataset, epochs=initial_epochs, validation_data=validation_dataset)
after_execution_INSERTED_INTO_SCRIPT(start_times=start_times_INSERTED_INTO_SCRIPT, experiment_file_path=EXPERIMENT_FILE_PATH, function_to_run='tensorflow.keras.Model.fit()', method_object=model, function_args=[train_dataset], function_kwargs={'epochs': initial_epochs, 'validation_data': validation_dataset})
acc = history.history['accuracy']
val_acc = history.history['val_accuracy']
loss = history.history['loss']
val_loss = history.history['val_loss']
plt.figure(figsize=(8, 8))
plt.subplot(2, 1, 1)
plt.plot(acc, label='Training Accuracy')
plt.plot(val_acc, label='Validation Accuracy')
plt.legend(loc='lower right')
plt.ylabel('Accuracy')
plt.ylim([min(plt.ylim()), 1])
plt.title('Training and Validation Accuracy')
plt.subplot(2, 1, 2)
plt.plot(loss, label='Training Loss')
plt.plot(val_loss, label='Validation Loss')
plt.legend(loc='upper right')
plt.ylabel('Cross Entropy')
plt.ylim([0, 1.0])
plt.title('Training and Validation Loss')
plt.xlabel('epoch')
plt.show()
base_model.trainable = True
print('Number of layers in the base model: ', len(base_model.layers))
fine_tune_at = 100
for layer in base_model.layers[:fine_tune_at]:
    layer.trainable = False
start_times_INSERTED_INTO_SCRIPT = before_execution_INSERTED_INTO_SCRIPT(experiment_file_path=EXPERIMENT_FILE_PATH, function_to_run='tensorflow.keras.Model.compile()')
model.compile(loss=tf.keras.losses.BinaryCrossentropy(from_logits=True), optimizer=tf.keras.optimizers.RMSprop(learning_rate=base_learning_rate / 10), metrics=['accuracy'])
after_execution_INSERTED_INTO_SCRIPT(start_times=start_times_INSERTED_INTO_SCRIPT, experiment_file_path=EXPERIMENT_FILE_PATH, function_to_run='tensorflow.keras.Model.compile()', method_object=model, function_args=None, function_kwargs={'loss': tf.keras.losses.BinaryCrossentropy(from_logits=True), 'optimizer': tf.keras.optimizers.RMSprop(learning_rate=base_learning_rate / 10), 'metrics': ['accuracy']})
start_times_INSERTED_INTO_SCRIPT = before_execution_INSERTED_INTO_SCRIPT(experiment_file_path=EXPERIMENT_FILE_PATH, function_to_run='tensorflow.keras.Model.summary()')
model.summary()
after_execution_INSERTED_INTO_SCRIPT(start_times=start_times_INSERTED_INTO_SCRIPT, experiment_file_path=EXPERIMENT_FILE_PATH, function_to_run='tensorflow.keras.Model.summary()', method_object=model, function_args=None, function_kwargs=None)
len(model.trainable_variables)
fine_tune_epochs = 10
total_epochs = initial_epochs + fine_tune_epochs
start_times_INSERTED_INTO_SCRIPT = before_execution_INSERTED_INTO_SCRIPT(experiment_file_path=EXPERIMENT_FILE_PATH, function_to_run='tensorflow.keras.Model.fit()')
history_fine = model.fit(train_dataset, epochs=total_epochs, initial_epoch=history.epoch[-1], validation_data=validation_dataset)
after_execution_INSERTED_INTO_SCRIPT(start_times=start_times_INSERTED_INTO_SCRIPT, experiment_file_path=EXPERIMENT_FILE_PATH, function_to_run='tensorflow.keras.Model.fit()', method_object=model, function_args=[train_dataset], function_kwargs={'epochs': total_epochs, 'initial_epoch': history.epoch[-1], 'validation_data': validation_dataset})
acc += history_fine.history['accuracy']
val_acc += history_fine.history['val_accuracy']
loss += history_fine.history['loss']
val_loss += history_fine.history['val_loss']
plt.figure(figsize=(8, 8))
plt.subplot(2, 1, 1)
plt.plot(acc, label='Training Accuracy')
plt.plot(val_acc, label='Validation Accuracy')
plt.ylim([0.8, 1])
plt.plot([initial_epochs - 1, initial_epochs - 1], plt.ylim(), label='Start Fine Tuning')
plt.legend(loc='lower right')
plt.title('Training and Validation Accuracy')
plt.subplot(2, 1, 2)
plt.plot(loss, label='Training Loss')
plt.plot(val_loss, label='Validation Loss')
plt.ylim([0, 1.0])
plt.plot([initial_epochs - 1, initial_epochs - 1], plt.ylim(), label='Start Fine Tuning')
plt.legend(loc='upper right')
plt.title('Training and Validation Loss')
plt.xlabel('epoch')
plt.show()
start_times_INSERTED_INTO_SCRIPT = before_execution_INSERTED_INTO_SCRIPT(experiment_file_path=EXPERIMENT_FILE_PATH, function_to_run='tensorflow.keras.Model.evaluate()')
(loss, accuracy) = model.evaluate(test_dataset)
after_execution_INSERTED_INTO_SCRIPT(start_times=start_times_INSERTED_INTO_SCRIPT, experiment_file_path=EXPERIMENT_FILE_PATH, function_to_run='tensorflow.keras.Model.evaluate()', method_object=model, function_args=[test_dataset], function_kwargs=None)
print('Test accuracy :', accuracy)
start_times_INSERTED_INTO_SCRIPT = before_execution_INSERTED_INTO_SCRIPT(experiment_file_path=EXPERIMENT_FILE_PATH, function_to_run='tensorflow.keras.utils.image_dataset_from_directory.take.prefetch.as_numpy_iterator().next()')
(image_batch, label_batch) = test_dataset.as_numpy_iterator().next()
after_execution_INSERTED_INTO_SCRIPT(start_times=start_times_INSERTED_INTO_SCRIPT, experiment_file_path=EXPERIMENT_FILE_PATH, function_to_run='tensorflow.keras.utils.image_dataset_from_directory.take.prefetch.as_numpy_iterator().next()', method_object=test_dataset, function_args=None, function_kwargs=None)
start_times_INSERTED_INTO_SCRIPT = before_execution_INSERTED_INTO_SCRIPT(experiment_file_path=EXPERIMENT_FILE_PATH, function_to_run='tensorflow.keras.Model.predict_on_batch(image_batch).flatten()')
predictions = model.predict_on_batch(image_batch).flatten()
after_execution_INSERTED_INTO_SCRIPT(start_times=start_times_INSERTED_INTO_SCRIPT, experiment_file_path=EXPERIMENT_FILE_PATH, function_to_run='tensorflow.keras.Model.predict_on_batch(image_batch).flatten()', method_object=model, function_args=None, function_kwargs=None)
start_times_INSERTED_INTO_SCRIPT = before_execution_INSERTED_INTO_SCRIPT(experiment_file_path=EXPERIMENT_FILE_PATH, function_to_run='tensorflow.nn.sigmoid()')
predictions = tf.nn.sigmoid(predictions)
after_execution_INSERTED_INTO_SCRIPT(start_times=start_times_INSERTED_INTO_SCRIPT, experiment_file_path=EXPERIMENT_FILE_PATH, function_to_run='tensorflow.nn.sigmoid()', method_object=None, function_args=[predictions], function_kwargs=None)
start_times_INSERTED_INTO_SCRIPT = before_execution_INSERTED_INTO_SCRIPT(experiment_file_path=EXPERIMENT_FILE_PATH, function_to_run='tensorflow.where()')
predictions = tf.where(predictions < 0.5, 0, 1)
after_execution_INSERTED_INTO_SCRIPT(start_times=start_times_INSERTED_INTO_SCRIPT, experiment_file_path=EXPERIMENT_FILE_PATH, function_to_run='tensorflow.where()', method_object=None, function_args=[predictions < 0.5, 0, 1], function_kwargs=None)
print('Predictions:\n', predictions.numpy())
print('Labels:\n', label_batch)
plt.figure(figsize=(10, 10))
for i in range(9):
    ax = plt.subplot(3, 3, i + 1)
    plt.imshow(image_batch[i].astype('uint8'))
    plt.title(class_names[predictions[i]])
    plt.axis('off')

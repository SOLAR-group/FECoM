import tensorflow as tf
import os
from pathlib import Path
import dill as pickle
import sys
from tool.client.client_config import EXPERIMENT_DIR, MAX_WAIT_S, WAIT_AFTER_RUN_S
from tool.server.send_request import send_request
from tool.server.function_details import FunctionDetails
current_path = os.path.abspath(__file__)
(immediate_folder, file_name) = os.path.split(current_path)
immediate_folder = os.path.basename(immediate_folder)
experiment_number = int(sys.argv[0])
experiment_file_name = os.path.splitext(file_name)[0]
EXPERIMENT_FILE_PATH = EXPERIMENT_DIR / 'method-level' / immediate_folder / experiment_file_name / f'experiment-{experiment_number}.json'

def custom_method(func, imports: str, function_to_run: str, method_object=None, function_args: list=None, function_kwargs: dict=None, max_wait_secs=MAX_WAIT_S, custom_class=None, wait_after_run_secs=WAIT_AFTER_RUN_S):
    result = send_request(imports=imports, function_to_run=function_to_run, function_args=function_args, function_kwargs=function_kwargs, max_wait_secs=max_wait_secs, method_object=method_object, custom_class=custom_class, experiment_file_path=EXPERIMENT_FILE_PATH)
    return func
if __name__ == '__main__':
    print(EXPERIMENT_FILE_PATH)
print('TensorFlow version:', tf.__version__)
from tensorflow.keras.layers import Dense, Flatten, Conv2D
from tensorflow.keras import Model
mnist = tf.keras.datasets.mnist
((x_train, y_train), (x_test, y_test)) = mnist.load_data()
(x_train, x_test) = (x_train / 255.0, x_test / 255.0)
x_train = custom_method(
x_train[..., tf.newaxis].astype('float32'), imports='from tensorflow.keras.layers import Dense, Flatten, Conv2D;from tensorflow.keras import Model;import tensorflow as tf', function_to_run='x_train[..., tf.newaxis].astype(*args)', method_object=None, function_args=[eval('"float32"')], function_kwargs={}, max_wait_secs=0)
x_test = custom_method(
x_test[..., tf.newaxis].astype('float32'), imports='from tensorflow.keras.layers import Dense, Flatten, Conv2D;from tensorflow.keras import Model;import tensorflow as tf', function_to_run='x_test[..., tf.newaxis].astype(*args)', method_object=None, function_args=[eval('"float32"')], function_kwargs={}, max_wait_secs=0)
train_ds = custom_method(
tf.data.Dataset.from_tensor_slices((x_train, y_train)).shuffle(10000).batch(32), imports='from tensorflow.keras.layers import Dense, Flatten, Conv2D;from tensorflow.keras import Model;import tensorflow as tf', function_to_run='tf.data.Dataset.from_tensor_slices((x_train, y_train)).shuffle(10000).batch(*args)', method_object=None, function_args=[eval('32')], function_kwargs={}, max_wait_secs=0)
test_ds = custom_method(
tf.data.Dataset.from_tensor_slices((x_test, y_test)).batch(32), imports='from tensorflow.keras.layers import Dense, Flatten, Conv2D;from tensorflow.keras import Model;import tensorflow as tf', function_to_run='tf.data.Dataset.from_tensor_slices((x_test, y_test)).batch(*args)', method_object=None, function_args=[eval('32')], function_kwargs={}, max_wait_secs=0)

class MyModel(Model):

    def __init__(self):
        custom_method(
        super(MyModel, self).__init__(), imports='from tensorflow.keras.layers import Dense, Flatten, Conv2D;from tensorflow.keras import Model;import tensorflow as tf', function_to_run='super(MyModel, self).__init__()', method_object=None, function_args=[], function_kwargs={}, max_wait_secs=0)
        self.conv1 = custom_method(
        Conv2D(32, 3, activation='relu'), imports='from tensorflow.keras.layers import Dense, Flatten, Conv2D;from tensorflow.keras import Model;import tensorflow as tf', function_to_run='Conv2D(*args, **kwargs)', method_object=None, function_args=[eval('32'), eval('3')], function_kwargs={'activation': eval("'relu'")}, max_wait_secs=0)
        self.flatten = custom_method(
        Flatten(), imports='from tensorflow.keras.layers import Dense, Flatten, Conv2D;from tensorflow.keras import Model;import tensorflow as tf', function_to_run='Flatten()', method_object=None, function_args=[], function_kwargs={}, max_wait_secs=0)
        self.d1 = custom_method(
        Dense(128, activation='relu'), imports='from tensorflow.keras.layers import Dense, Flatten, Conv2D;from tensorflow.keras import Model;import tensorflow as tf', function_to_run='Dense(*args, **kwargs)', method_object=None, function_args=[eval('128')], function_kwargs={'activation': eval("'relu'")}, max_wait_secs=0)
        self.d2 = custom_method(
        Dense(10), imports='from tensorflow.keras.layers import Dense, Flatten, Conv2D;from tensorflow.keras import Model;import tensorflow as tf', function_to_run='Dense(*args)', method_object=None, function_args=[eval('10')], function_kwargs={}, max_wait_secs=0)

    def call(self, x):
        x = self.conv1(x)
        x = self.flatten(x)
        x = self.d1(x)
        return self.d2(x)
model = custom_method(
MyModel(), imports='from tensorflow.keras.layers import Dense, Flatten, Conv2D;from tensorflow.keras import Model;import tensorflow as tf', function_to_run='MyModel()', method_object=None, function_args=[], function_kwargs={}, max_wait_secs=0)
loss_object = custom_method(
tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True), imports='from tensorflow.keras.layers import Dense, Flatten, Conv2D;from tensorflow.keras import Model;import tensorflow as tf', function_to_run='tf.keras.losses.SparseCategoricalCrossentropy(**kwargs)', method_object=None, function_args=[], function_kwargs={'from_logits': eval('True')}, max_wait_secs=0)
optimizer = custom_method(
tf.keras.optimizers.Adam(), imports='from tensorflow.keras.layers import Dense, Flatten, Conv2D;from tensorflow.keras import Model;import tensorflow as tf', function_to_run='tf.keras.optimizers.Adam()', method_object=None, function_args=[], function_kwargs={}, max_wait_secs=0)
train_loss = custom_method(
tf.keras.metrics.Mean(name='train_loss'), imports='from tensorflow.keras.layers import Dense, Flatten, Conv2D;from tensorflow.keras import Model;import tensorflow as tf', function_to_run='tf.keras.metrics.Mean(**kwargs)', method_object=None, function_args=[], function_kwargs={'name': eval("'train_loss'")}, max_wait_secs=0)
train_accuracy = custom_method(
tf.keras.metrics.SparseCategoricalAccuracy(name='train_accuracy'), imports='from tensorflow.keras.layers import Dense, Flatten, Conv2D;from tensorflow.keras import Model;import tensorflow as tf', function_to_run='tf.keras.metrics.SparseCategoricalAccuracy(**kwargs)', method_object=None, function_args=[], function_kwargs={'name': eval("'train_accuracy'")}, max_wait_secs=0)
test_loss = custom_method(
tf.keras.metrics.Mean(name='test_loss'), imports='from tensorflow.keras.layers import Dense, Flatten, Conv2D;from tensorflow.keras import Model;import tensorflow as tf', function_to_run='tf.keras.metrics.Mean(**kwargs)', method_object=None, function_args=[], function_kwargs={'name': eval("'test_loss'")}, max_wait_secs=0)
test_accuracy = custom_method(
tf.keras.metrics.SparseCategoricalAccuracy(name='test_accuracy'), imports='from tensorflow.keras.layers import Dense, Flatten, Conv2D;from tensorflow.keras import Model;import tensorflow as tf', function_to_run='tf.keras.metrics.SparseCategoricalAccuracy(**kwargs)', method_object=None, function_args=[], function_kwargs={'name': eval("'test_accuracy'")}, max_wait_secs=0)

@tf.function
def train_step(images, labels):
    with custom_method(
    tf.GradientTape(), imports='from tensorflow.keras.layers import Dense, Flatten, Conv2D;from tensorflow.keras import Model;import tensorflow as tf', function_to_run='tf.GradientTape()', method_object=None, function_args=[], function_kwargs={}, max_wait_secs=0) as tape:
        predictions = custom_method(
        model(images, training=True), imports='from tensorflow.keras.layers import Dense, Flatten, Conv2D;from tensorflow.keras import Model;import tensorflow as tf', function_to_run='obj(*args, **kwargs)', method_object=eval('model'), function_args=[eval('images')], function_kwargs={'training': eval('True')}, max_wait_secs=0, custom_class="class MyModel(Model):\n  def __init__(self):\n    super(MyModel, self).__init__()\n    self.conv1 = Conv2D(32, 3, activation='relu')\n    self.flatten = Flatten()\n    self.d1 = Dense(128, activation='relu')\n    self.d2 = Dense(10)\n\n  def call(self, x):\n    x = self.conv1(x)\n    x = self.flatten(x)\n    x = self.d1(x)\n    return self.d2(x)")
        loss = custom_method(
        loss_object(labels, predictions), imports='from tensorflow.keras.layers import Dense, Flatten, Conv2D;from tensorflow.keras import Model;import tensorflow as tf', function_to_run='obj(*args)', method_object=eval('loss_object'), function_args=[eval('labels'), eval('predictions')], function_kwargs={}, max_wait_secs=0, custom_class=None)
    gradients = tape.gradient(loss, model.trainable_variables)
    custom_method(
    optimizer.apply_gradients(zip(gradients, model.trainable_variables)), imports='from tensorflow.keras.layers import Dense, Flatten, Conv2D;from tensorflow.keras import Model;import tensorflow as tf', function_to_run='obj.apply_gradients(*args)', method_object=eval('optimizer'), function_args=[eval('zip(gradients, model.trainable_variables)')], function_kwargs={}, max_wait_secs=0, custom_class=None)
    custom_method(
    train_loss(loss), imports='from tensorflow.keras.layers import Dense, Flatten, Conv2D;from tensorflow.keras import Model;import tensorflow as tf', function_to_run='obj(*args)', method_object=eval('train_loss'), function_args=[eval('loss')], function_kwargs={}, max_wait_secs=0, custom_class=None)
    custom_method(
    train_accuracy(labels, predictions), imports='from tensorflow.keras.layers import Dense, Flatten, Conv2D;from tensorflow.keras import Model;import tensorflow as tf', function_to_run='obj(*args)', method_object=eval('train_accuracy'), function_args=[eval('labels'), eval('predictions')], function_kwargs={}, max_wait_secs=0, custom_class=None)

@tf.function
def test_step(images, labels):
    predictions = custom_method(
    model(images, training=False), imports='from tensorflow.keras.layers import Dense, Flatten, Conv2D;from tensorflow.keras import Model;import tensorflow as tf', function_to_run='obj(*args, **kwargs)', method_object=eval('model'), function_args=[eval('images')], function_kwargs={'training': eval('False')}, max_wait_secs=0, custom_class="class MyModel(Model):\n  def __init__(self):\n    super(MyModel, self).__init__()\n    self.conv1 = Conv2D(32, 3, activation='relu')\n    self.flatten = Flatten()\n    self.d1 = Dense(128, activation='relu')\n    self.d2 = Dense(10)\n\n  def call(self, x):\n    x = self.conv1(x)\n    x = self.flatten(x)\n    x = self.d1(x)\n    return self.d2(x)")
    t_loss = custom_method(
    loss_object(labels, predictions), imports='from tensorflow.keras.layers import Dense, Flatten, Conv2D;from tensorflow.keras import Model;import tensorflow as tf', function_to_run='obj(*args)', method_object=eval('loss_object'), function_args=[eval('labels'), eval('predictions')], function_kwargs={}, max_wait_secs=0, custom_class=None)
    custom_method(
    test_loss(t_loss), imports='from tensorflow.keras.layers import Dense, Flatten, Conv2D;from tensorflow.keras import Model;import tensorflow as tf', function_to_run='obj(*args)', method_object=eval('test_loss'), function_args=[eval('t_loss')], function_kwargs={}, max_wait_secs=0, custom_class=None)
    custom_method(
    test_accuracy(labels, predictions), imports='from tensorflow.keras.layers import Dense, Flatten, Conv2D;from tensorflow.keras import Model;import tensorflow as tf', function_to_run='obj(*args)', method_object=eval('test_accuracy'), function_args=[eval('labels'), eval('predictions')], function_kwargs={}, max_wait_secs=0, custom_class=None)
EPOCHS = 5
for epoch in range(EPOCHS):
    custom_method(
    train_loss.reset_states(), imports='from tensorflow.keras.layers import Dense, Flatten, Conv2D;from tensorflow.keras import Model;import tensorflow as tf', function_to_run='obj.reset_states()', method_object=eval('train_loss'), function_args=[], function_kwargs={}, max_wait_secs=0, custom_class=None)
    custom_method(
    train_accuracy.reset_states(), imports='from tensorflow.keras.layers import Dense, Flatten, Conv2D;from tensorflow.keras import Model;import tensorflow as tf', function_to_run='obj.reset_states()', method_object=eval('train_accuracy'), function_args=[], function_kwargs={}, max_wait_secs=0, custom_class=None)
    custom_method(
    test_loss.reset_states(), imports='from tensorflow.keras.layers import Dense, Flatten, Conv2D;from tensorflow.keras import Model;import tensorflow as tf', function_to_run='obj.reset_states()', method_object=eval('test_loss'), function_args=[], function_kwargs={}, max_wait_secs=0, custom_class=None)
    custom_method(
    test_accuracy.reset_states(), imports='from tensorflow.keras.layers import Dense, Flatten, Conv2D;from tensorflow.keras import Model;import tensorflow as tf', function_to_run='obj.reset_states()', method_object=eval('test_accuracy'), function_args=[], function_kwargs={}, max_wait_secs=0, custom_class=None)
    for (images, labels) in train_ds:
        train_step(images, labels)
    for (test_images, test_labels) in test_ds:
        test_step(test_images, test_labels)
    print(f'Epoch {epoch + 1}, Loss: {train_loss.result()}, Accuracy: {train_accuracy.result() * 100}, Test Loss: {test_loss.result()}, Test Accuracy: {test_accuracy.result() * 100}')
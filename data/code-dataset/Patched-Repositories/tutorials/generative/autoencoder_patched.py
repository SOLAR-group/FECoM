import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import tensorflow as tf
from sklearn.metrics import accuracy_score, precision_score, recall_score
from sklearn.model_selection import train_test_split
from tensorflow.keras import layers, losses
from tensorflow.keras.datasets import fashion_mnist
from tensorflow.keras.models import Model
import os
from pathlib import Path
import dill as pickle
from tool.client.client_config import EXPERIMENT_DIR, EXPERIMENT_TAG, MAX_WAIT_S, WAIT_AFTER_RUN_S
from tool.server.send_request import send_request
from tool.server.function_details import FunctionDetails
current_path = os.path.abspath(__file__)
(immediate_folder, file_name) = os.path.split(current_path)
immediate_folder = os.path.basename(immediate_folder)
experiment_file_name = os.path.splitext(file_name)[0]
EXPERIMENT_FILE_PATH = EXPERIMENT_DIR / immediate_folder / EXPERIMENT_TAG / (experiment_file_name + '-energy.json')

def custom_method(func, imports: str, function_to_run: str, method_object=None, function_args: list=None, function_kwargs: dict=None, max_wait_secs=MAX_WAIT_S, custom_class=None, wait_after_run_secs=WAIT_AFTER_RUN_S):
    result = send_request(imports=imports, function_to_run=function_to_run, function_args=function_args, function_kwargs=function_kwargs, max_wait_secs=max_wait_secs, method_object=method_object, custom_class=custom_class, experiment_file_path=EXPERIMENT_FILE_PATH)
    return func
if __name__ == '__main__':
    print(EXPERIMENT_FILE_PATH)
((x_train, _), (x_test, _)) = custom_method(
fashion_mnist.load_data(), imports='from tensorflow.keras.datasets import fashion_mnist;from tensorflow.keras import layers, losses;import pandas as pd;from sklearn.metrics import accuracy_score, precision_score, recall_score;from tensorflow.keras.models import Model;import tensorflow as tf;from sklearn.model_selection import train_test_split;import numpy as np;import matplotlib.pyplot as plt', function_to_run='fashion_mnist.load_data()', method_object=None, function_args=[], function_kwargs={}, max_wait_secs=0)
x_train = x_train.astype('float32') / 255.0
x_test = x_test.astype('float32') / 255.0
print(x_train.shape)
print(x_test.shape)
latent_dim = 64

class Autoencoder(Model):

    def __init__(self, latent_dim):
        super(Autoencoder, self).__init__()
        self.latent_dim = latent_dim
        self.encoder = custom_method(
        tf.keras.Sequential([layers.Flatten(), layers.Dense(latent_dim, activation='relu')]), imports='from tensorflow.keras.datasets import fashion_mnist;from tensorflow.keras import layers, losses;import pandas as pd;from sklearn.metrics import accuracy_score, precision_score, recall_score;from tensorflow.keras.models import Model;import tensorflow as tf;from sklearn.model_selection import train_test_split;import numpy as np;import matplotlib.pyplot as plt', function_to_run='tf.keras.Sequential(*args)', method_object=None, function_args=[eval("[\n      layers.Flatten(),\n      layers.Dense(latent_dim, activation='relu'),\n    ]")], function_kwargs={}, max_wait_secs=0)
        self.decoder = custom_method(
        tf.keras.Sequential([layers.Dense(784, activation='sigmoid'), layers.Reshape((28, 28))]), imports='from tensorflow.keras.datasets import fashion_mnist;from tensorflow.keras import layers, losses;import pandas as pd;from sklearn.metrics import accuracy_score, precision_score, recall_score;from tensorflow.keras.models import Model;import tensorflow as tf;from sklearn.model_selection import train_test_split;import numpy as np;import matplotlib.pyplot as plt', function_to_run='tf.keras.Sequential(*args)', method_object=None, function_args=[eval("[\n      layers.Dense(784, activation='sigmoid'),\n      layers.Reshape((28, 28))\n    ]")], function_kwargs={}, max_wait_secs=0)

    def call(self, x):
        encoded = self.encoder(x)
        decoded = self.decoder(encoded)
        return decoded
autoencoder = Autoencoder(latent_dim)
custom_method(
autoencoder.compile(optimizer='adam', loss=losses.MeanSquaredError()), imports='from tensorflow.keras.datasets import fashion_mnist;from tensorflow.keras import layers, losses;import pandas as pd;from sklearn.metrics import accuracy_score, precision_score, recall_score;from tensorflow.keras.models import Model;import tensorflow as tf;from sklearn.model_selection import train_test_split;import numpy as np;import matplotlib.pyplot as plt', function_to_run='obj.compile(**kwargs)', method_object=eval('autoencoder'), function_args=[], function_kwargs={'optimizer': eval("'adam'"), 'loss': eval('losses.MeanSquaredError()')}, max_wait_secs=0, custom_class='class AnomalyDetector(Model):\n  def __init__(self):\n    super(AnomalyDetector, self).__init__()\n    self.encoder = tf.keras.Sequential([\n      layers.Dense(32, activation="relu"),\n      layers.Dense(16, activation="relu"),\n      layers.Dense(8, activation="relu")])\n    \n    self.decoder = tf.keras.Sequential([\n      layers.Dense(16, activation="relu"),\n      layers.Dense(32, activation="relu"),\n      layers.Dense(140, activation="sigmoid")])\n    \n  def call(self, x):\n    encoded = self.encoder(x)\n    decoded = self.decoder(encoded)\n    return decoded')
custom_method(
autoencoder.fit(x_train, x_train, epochs=10, shuffle=True, validation_data=(x_test, x_test)), imports='from tensorflow.keras.datasets import fashion_mnist;from tensorflow.keras import layers, losses;import pandas as pd;from sklearn.metrics import accuracy_score, precision_score, recall_score;from tensorflow.keras.models import Model;import tensorflow as tf;from sklearn.model_selection import train_test_split;import numpy as np;import matplotlib.pyplot as plt', function_to_run='obj.fit(*args, **kwargs)', method_object=eval('autoencoder'), function_args=[eval('x_train'), eval('x_train')], function_kwargs={'epochs': eval('10'), 'shuffle': eval('True'), 'validation_data': eval('(x_test, x_test)')}, max_wait_secs=0, custom_class='class AnomalyDetector(Model):\n  def __init__(self):\n    super(AnomalyDetector, self).__init__()\n    self.encoder = tf.keras.Sequential([\n      layers.Dense(32, activation="relu"),\n      layers.Dense(16, activation="relu"),\n      layers.Dense(8, activation="relu")])\n    \n    self.decoder = tf.keras.Sequential([\n      layers.Dense(16, activation="relu"),\n      layers.Dense(32, activation="relu"),\n      layers.Dense(140, activation="sigmoid")])\n    \n  def call(self, x):\n    encoded = self.encoder(x)\n    decoded = self.decoder(encoded)\n    return decoded')
encoded_imgs = autoencoder.encoder(x_test).numpy()
decoded_imgs = autoencoder.decoder(encoded_imgs).numpy()
n = 10
plt.figure(figsize=(20, 4))
for i in range(n):
    ax = plt.subplot(2, n, i + 1)
    plt.imshow(x_test[i])
    plt.title('original')
    plt.gray()
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)
    ax = plt.subplot(2, n, i + 1 + n)
    plt.imshow(decoded_imgs[i])
    plt.title('reconstructed')
    plt.gray()
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)
plt.show()
((x_train, _), (x_test, _)) = custom_method(
fashion_mnist.load_data(), imports='from tensorflow.keras.datasets import fashion_mnist;from tensorflow.keras import layers, losses;import pandas as pd;from sklearn.metrics import accuracy_score, precision_score, recall_score;from tensorflow.keras.models import Model;import tensorflow as tf;from sklearn.model_selection import train_test_split;import numpy as np;import matplotlib.pyplot as plt', function_to_run='fashion_mnist.load_data()', method_object=None, function_args=[], function_kwargs={}, max_wait_secs=0)
x_train = x_train.astype('float32') / 255.0
x_test = x_test.astype('float32') / 255.0
x_train = x_train[..., tf.newaxis]
x_test = x_test[..., tf.newaxis]
print(x_train.shape)
noise_factor = 0.2
x_train_noisy = x_train + noise_factor * custom_method(
tf.random.normal(shape=x_train.shape), imports='from tensorflow.keras.datasets import fashion_mnist;from tensorflow.keras import layers, losses;import pandas as pd;from sklearn.metrics import accuracy_score, precision_score, recall_score;from tensorflow.keras.models import Model;import tensorflow as tf;from sklearn.model_selection import train_test_split;import numpy as np;import matplotlib.pyplot as plt', function_to_run='tf.random.normal(**kwargs)', method_object=None, function_args=[], function_kwargs={'shape': eval('x_train.shape')}, max_wait_secs=0)
x_test_noisy = x_test + noise_factor * custom_method(
tf.random.normal(shape=x_test.shape), imports='from tensorflow.keras.datasets import fashion_mnist;from tensorflow.keras import layers, losses;import pandas as pd;from sklearn.metrics import accuracy_score, precision_score, recall_score;from tensorflow.keras.models import Model;import tensorflow as tf;from sklearn.model_selection import train_test_split;import numpy as np;import matplotlib.pyplot as plt', function_to_run='tf.random.normal(**kwargs)', method_object=None, function_args=[], function_kwargs={'shape': eval('x_test.shape')}, max_wait_secs=0)
x_train_noisy = custom_method(
tf.clip_by_value(x_train_noisy, clip_value_min=0.0, clip_value_max=1.0), imports='from tensorflow.keras.datasets import fashion_mnist;from tensorflow.keras import layers, losses;import pandas as pd;from sklearn.metrics import accuracy_score, precision_score, recall_score;from tensorflow.keras.models import Model;import tensorflow as tf;from sklearn.model_selection import train_test_split;import numpy as np;import matplotlib.pyplot as plt', function_to_run='tf.clip_by_value(*args, **kwargs)', method_object=None, function_args=[eval('x_train_noisy')], function_kwargs={'clip_value_min': eval('0.'), 'clip_value_max': eval('1.')}, max_wait_secs=0)
x_test_noisy = custom_method(
tf.clip_by_value(x_test_noisy, clip_value_min=0.0, clip_value_max=1.0), imports='from tensorflow.keras.datasets import fashion_mnist;from tensorflow.keras import layers, losses;import pandas as pd;from sklearn.metrics import accuracy_score, precision_score, recall_score;from tensorflow.keras.models import Model;import tensorflow as tf;from sklearn.model_selection import train_test_split;import numpy as np;import matplotlib.pyplot as plt', function_to_run='tf.clip_by_value(*args, **kwargs)', method_object=None, function_args=[eval('x_test_noisy')], function_kwargs={'clip_value_min': eval('0.'), 'clip_value_max': eval('1.')}, max_wait_secs=0)
n = 10
plt.figure(figsize=(20, 2))
for i in range(n):
    ax = plt.subplot(1, n, i + 1)
    plt.title('original + noise')
    plt.imshow(tf.squeeze(x_test_noisy[i]))
    plt.gray()
plt.show()

class Denoise(Model):

    def __init__(self):
        super(Denoise, self).__init__()
        self.encoder = custom_method(
        tf.keras.Sequential([layers.Input(shape=(28, 28, 1)), layers.Conv2D(16, (3, 3), activation='relu', padding='same', strides=2), layers.Conv2D(8, (3, 3), activation='relu', padding='same', strides=2)]), imports='from tensorflow.keras.datasets import fashion_mnist;from tensorflow.keras import layers, losses;import pandas as pd;from sklearn.metrics import accuracy_score, precision_score, recall_score;from tensorflow.keras.models import Model;import tensorflow as tf;from sklearn.model_selection import train_test_split;import numpy as np;import matplotlib.pyplot as plt', function_to_run='tf.keras.Sequential(*args)', method_object=None, function_args=[eval("[\n      layers.Input(shape=(28, 28, 1)),\n      layers.Conv2D(16, (3, 3), activation='relu', padding='same', strides=2),\n      layers.Conv2D(8, (3, 3), activation='relu', padding='same', strides=2)]")], function_kwargs={}, max_wait_secs=0)
        self.decoder = custom_method(
        tf.keras.Sequential([layers.Conv2DTranspose(8, kernel_size=3, strides=2, activation='relu', padding='same'), layers.Conv2DTranspose(16, kernel_size=3, strides=2, activation='relu', padding='same'), layers.Conv2D(1, kernel_size=(3, 3), activation='sigmoid', padding='same')]), imports='from tensorflow.keras.datasets import fashion_mnist;from tensorflow.keras import layers, losses;import pandas as pd;from sklearn.metrics import accuracy_score, precision_score, recall_score;from tensorflow.keras.models import Model;import tensorflow as tf;from sklearn.model_selection import train_test_split;import numpy as np;import matplotlib.pyplot as plt', function_to_run='tf.keras.Sequential(*args)', method_object=None, function_args=[eval("[\n      layers.Conv2DTranspose(8, kernel_size=3, strides=2, activation='relu', padding='same'),\n      layers.Conv2DTranspose(16, kernel_size=3, strides=2, activation='relu', padding='same'),\n      layers.Conv2D(1, kernel_size=(3, 3), activation='sigmoid', padding='same')]")], function_kwargs={}, max_wait_secs=0)

    def call(self, x):
        encoded = self.encoder(x)
        decoded = self.decoder(encoded)
        return decoded
autoencoder = Denoise()
custom_method(
autoencoder.compile(optimizer='adam', loss=losses.MeanSquaredError()), imports='from tensorflow.keras.datasets import fashion_mnist;from tensorflow.keras import layers, losses;import pandas as pd;from sklearn.metrics import accuracy_score, precision_score, recall_score;from tensorflow.keras.models import Model;import tensorflow as tf;from sklearn.model_selection import train_test_split;import numpy as np;import matplotlib.pyplot as plt', function_to_run='obj.compile(**kwargs)', method_object=eval('autoencoder'), function_args=[], function_kwargs={'optimizer': eval("'adam'"), 'loss': eval('losses.MeanSquaredError()')}, max_wait_secs=0, custom_class='class AnomalyDetector(Model):\n  def __init__(self):\n    super(AnomalyDetector, self).__init__()\n    self.encoder = tf.keras.Sequential([\n      layers.Dense(32, activation="relu"),\n      layers.Dense(16, activation="relu"),\n      layers.Dense(8, activation="relu")])\n    \n    self.decoder = tf.keras.Sequential([\n      layers.Dense(16, activation="relu"),\n      layers.Dense(32, activation="relu"),\n      layers.Dense(140, activation="sigmoid")])\n    \n  def call(self, x):\n    encoded = self.encoder(x)\n    decoded = self.decoder(encoded)\n    return decoded')
custom_method(
autoencoder.fit(x_train_noisy, x_train, epochs=10, shuffle=True, validation_data=(x_test_noisy, x_test)), imports='from tensorflow.keras.datasets import fashion_mnist;from tensorflow.keras import layers, losses;import pandas as pd;from sklearn.metrics import accuracy_score, precision_score, recall_score;from tensorflow.keras.models import Model;import tensorflow as tf;from sklearn.model_selection import train_test_split;import numpy as np;import matplotlib.pyplot as plt', function_to_run='obj.fit(*args, **kwargs)', method_object=eval('autoencoder'), function_args=[eval('x_train_noisy'), eval('x_train')], function_kwargs={'epochs': eval('10'), 'shuffle': eval('True'), 'validation_data': eval('(x_test_noisy, x_test)')}, max_wait_secs=0, custom_class='class AnomalyDetector(Model):\n  def __init__(self):\n    super(AnomalyDetector, self).__init__()\n    self.encoder = tf.keras.Sequential([\n      layers.Dense(32, activation="relu"),\n      layers.Dense(16, activation="relu"),\n      layers.Dense(8, activation="relu")])\n    \n    self.decoder = tf.keras.Sequential([\n      layers.Dense(16, activation="relu"),\n      layers.Dense(32, activation="relu"),\n      layers.Dense(140, activation="sigmoid")])\n    \n  def call(self, x):\n    encoded = self.encoder(x)\n    decoded = self.decoder(encoded)\n    return decoded')
custom_method(
autoencoder.encoder.summary(), imports='from tensorflow.keras.datasets import fashion_mnist;from tensorflow.keras import layers, losses;import pandas as pd;from sklearn.metrics import accuracy_score, precision_score, recall_score;from tensorflow.keras.models import Model;import tensorflow as tf;from sklearn.model_selection import train_test_split;import numpy as np;import matplotlib.pyplot as plt', function_to_run='obj.encoder.summary()', method_object=eval('autoencoder'), function_args=[], function_kwargs={}, max_wait_secs=0, custom_class='class AnomalyDetector(Model):\n  def __init__(self):\n    super(AnomalyDetector, self).__init__()\n    self.encoder = tf.keras.Sequential([\n      layers.Dense(32, activation="relu"),\n      layers.Dense(16, activation="relu"),\n      layers.Dense(8, activation="relu")])\n    \n    self.decoder = tf.keras.Sequential([\n      layers.Dense(16, activation="relu"),\n      layers.Dense(32, activation="relu"),\n      layers.Dense(140, activation="sigmoid")])\n    \n  def call(self, x):\n    encoded = self.encoder(x)\n    decoded = self.decoder(encoded)\n    return decoded')
custom_method(
autoencoder.decoder.summary(), imports='from tensorflow.keras.datasets import fashion_mnist;from tensorflow.keras import layers, losses;import pandas as pd;from sklearn.metrics import accuracy_score, precision_score, recall_score;from tensorflow.keras.models import Model;import tensorflow as tf;from sklearn.model_selection import train_test_split;import numpy as np;import matplotlib.pyplot as plt', function_to_run='obj.decoder.summary()', method_object=eval('autoencoder'), function_args=[], function_kwargs={}, max_wait_secs=0, custom_class='class AnomalyDetector(Model):\n  def __init__(self):\n    super(AnomalyDetector, self).__init__()\n    self.encoder = tf.keras.Sequential([\n      layers.Dense(32, activation="relu"),\n      layers.Dense(16, activation="relu"),\n      layers.Dense(8, activation="relu")])\n    \n    self.decoder = tf.keras.Sequential([\n      layers.Dense(16, activation="relu"),\n      layers.Dense(32, activation="relu"),\n      layers.Dense(140, activation="sigmoid")])\n    \n  def call(self, x):\n    encoded = self.encoder(x)\n    decoded = self.decoder(encoded)\n    return decoded')
encoded_imgs = custom_method(
autoencoder.encoder(x_test_noisy).numpy(), imports='from tensorflow.keras.datasets import fashion_mnist;from tensorflow.keras import layers, losses;import pandas as pd;from sklearn.metrics import accuracy_score, precision_score, recall_score;from tensorflow.keras.models import Model;import tensorflow as tf;from sklearn.model_selection import train_test_split;import numpy as np;import matplotlib.pyplot as plt', function_to_run='autoencoder.encoder(obj).numpy()', method_object=eval('x_test_noisy'), function_args=[], function_kwargs={}, max_wait_secs=0, custom_class=None)
decoded_imgs = autoencoder.decoder(encoded_imgs).numpy()
n = 10
plt.figure(figsize=(20, 4))
for i in range(n):
    ax = plt.subplot(2, n, i + 1)
    plt.title('original + noise')
    plt.imshow(tf.squeeze(x_test_noisy[i]))
    plt.gray()
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)
    bx = plt.subplot(2, n, i + n + 1)
    plt.title('reconstructed')
    plt.imshow(tf.squeeze(decoded_imgs[i]))
    plt.gray()
    bx.get_xaxis().set_visible(False)
    bx.get_yaxis().set_visible(False)
plt.show()
dataframe = pd.read_csv('http://storage.googleapis.com/download.tensorflow.org/data/ecg.csv', header=None)
raw_data = dataframe.values
dataframe.head()
labels = raw_data[:, -1]
data = raw_data[:, 0:-1]
(train_data, test_data, train_labels, test_labels) = train_test_split(data, labels, test_size=0.2, random_state=21)
min_val = custom_method(
tf.reduce_min(train_data), imports='from tensorflow.keras.datasets import fashion_mnist;from tensorflow.keras import layers, losses;import pandas as pd;from sklearn.metrics import accuracy_score, precision_score, recall_score;from tensorflow.keras.models import Model;import tensorflow as tf;from sklearn.model_selection import train_test_split;import numpy as np;import matplotlib.pyplot as plt', function_to_run='tf.reduce_min(*args)', method_object=None, function_args=[eval('train_data')], function_kwargs={}, max_wait_secs=0)
max_val = custom_method(
tf.reduce_max(train_data), imports='from tensorflow.keras.datasets import fashion_mnist;from tensorflow.keras import layers, losses;import pandas as pd;from sklearn.metrics import accuracy_score, precision_score, recall_score;from tensorflow.keras.models import Model;import tensorflow as tf;from sklearn.model_selection import train_test_split;import numpy as np;import matplotlib.pyplot as plt', function_to_run='tf.reduce_max(*args)', method_object=None, function_args=[eval('train_data')], function_kwargs={}, max_wait_secs=0)
train_data = (train_data - min_val) / (max_val - min_val)
test_data = (test_data - min_val) / (max_val - min_val)
train_data = custom_method(
tf.cast(train_data, tf.float32), imports='from tensorflow.keras.datasets import fashion_mnist;from tensorflow.keras import layers, losses;import pandas as pd;from sklearn.metrics import accuracy_score, precision_score, recall_score;from tensorflow.keras.models import Model;import tensorflow as tf;from sklearn.model_selection import train_test_split;import numpy as np;import matplotlib.pyplot as plt', function_to_run='tf.cast(*args)', method_object=None, function_args=[eval('train_data'), eval('tf.float32')], function_kwargs={}, max_wait_secs=0)
test_data = custom_method(
tf.cast(test_data, tf.float32), imports='from tensorflow.keras.datasets import fashion_mnist;from tensorflow.keras import layers, losses;import pandas as pd;from sklearn.metrics import accuracy_score, precision_score, recall_score;from tensorflow.keras.models import Model;import tensorflow as tf;from sklearn.model_selection import train_test_split;import numpy as np;import matplotlib.pyplot as plt', function_to_run='tf.cast(*args)', method_object=None, function_args=[eval('test_data'), eval('tf.float32')], function_kwargs={}, max_wait_secs=0)
train_labels = train_labels.astype(bool)
test_labels = test_labels.astype(bool)
normal_train_data = train_data[train_labels]
normal_test_data = test_data[test_labels]
anomalous_train_data = train_data[~train_labels]
anomalous_test_data = test_data[~test_labels]
plt.grid()
plt.plot(np.arange(140), normal_train_data[0])
plt.title('A Normal ECG')
plt.show()
plt.grid()
plt.plot(np.arange(140), anomalous_train_data[0])
plt.title('An Anomalous ECG')
plt.show()

class AnomalyDetector(Model):

    def __init__(self):
        super(AnomalyDetector, self).__init__()
        self.encoder = custom_method(
        tf.keras.Sequential([layers.Dense(32, activation='relu'), layers.Dense(16, activation='relu'), layers.Dense(8, activation='relu')]), imports='from tensorflow.keras.datasets import fashion_mnist;from tensorflow.keras import layers, losses;import pandas as pd;from sklearn.metrics import accuracy_score, precision_score, recall_score;from tensorflow.keras.models import Model;import tensorflow as tf;from sklearn.model_selection import train_test_split;import numpy as np;import matplotlib.pyplot as plt', function_to_run='tf.keras.Sequential(*args)', method_object=None, function_args=[eval('[\n      layers.Dense(32, activation="relu"),\n      layers.Dense(16, activation="relu"),\n      layers.Dense(8, activation="relu")]')], function_kwargs={}, max_wait_secs=0)
        self.decoder = custom_method(
        tf.keras.Sequential([layers.Dense(16, activation='relu'), layers.Dense(32, activation='relu'), layers.Dense(140, activation='sigmoid')]), imports='from tensorflow.keras.datasets import fashion_mnist;from tensorflow.keras import layers, losses;import pandas as pd;from sklearn.metrics import accuracy_score, precision_score, recall_score;from tensorflow.keras.models import Model;import tensorflow as tf;from sklearn.model_selection import train_test_split;import numpy as np;import matplotlib.pyplot as plt', function_to_run='tf.keras.Sequential(*args)', method_object=None, function_args=[eval('[\n      layers.Dense(16, activation="relu"),\n      layers.Dense(32, activation="relu"),\n      layers.Dense(140, activation="sigmoid")]')], function_kwargs={}, max_wait_secs=0)

    def call(self, x):
        encoded = self.encoder(x)
        decoded = self.decoder(encoded)
        return decoded
autoencoder = AnomalyDetector()
custom_method(
autoencoder.compile(optimizer='adam', loss='mae'), imports='from tensorflow.keras.datasets import fashion_mnist;from tensorflow.keras import layers, losses;import pandas as pd;from sklearn.metrics import accuracy_score, precision_score, recall_score;from tensorflow.keras.models import Model;import tensorflow as tf;from sklearn.model_selection import train_test_split;import numpy as np;import matplotlib.pyplot as plt', function_to_run='obj.compile(**kwargs)', method_object=eval('autoencoder'), function_args=[], function_kwargs={'optimizer': eval("'adam'"), 'loss': eval("'mae'")}, max_wait_secs=0, custom_class='class AnomalyDetector(Model):\n  def __init__(self):\n    super(AnomalyDetector, self).__init__()\n    self.encoder = tf.keras.Sequential([\n      layers.Dense(32, activation="relu"),\n      layers.Dense(16, activation="relu"),\n      layers.Dense(8, activation="relu")])\n    \n    self.decoder = tf.keras.Sequential([\n      layers.Dense(16, activation="relu"),\n      layers.Dense(32, activation="relu"),\n      layers.Dense(140, activation="sigmoid")])\n    \n  def call(self, x):\n    encoded = self.encoder(x)\n    decoded = self.decoder(encoded)\n    return decoded')
history = custom_method(
autoencoder.fit(normal_train_data, normal_train_data, epochs=20, batch_size=512, validation_data=(test_data, test_data), shuffle=True), imports='from tensorflow.keras.datasets import fashion_mnist;from tensorflow.keras import layers, losses;import pandas as pd;from sklearn.metrics import accuracy_score, precision_score, recall_score;from tensorflow.keras.models import Model;import tensorflow as tf;from sklearn.model_selection import train_test_split;import numpy as np;import matplotlib.pyplot as plt', function_to_run='obj.fit(*args, **kwargs)', method_object=eval('autoencoder'), function_args=[eval('normal_train_data'), eval('normal_train_data')], function_kwargs={'epochs': eval('20'), 'batch_size': eval('512'), 'validation_data': eval('(test_data, test_data)'), 'shuffle': eval('True')}, max_wait_secs=0, custom_class='class AnomalyDetector(Model):\n  def __init__(self):\n    super(AnomalyDetector, self).__init__()\n    self.encoder = tf.keras.Sequential([\n      layers.Dense(32, activation="relu"),\n      layers.Dense(16, activation="relu"),\n      layers.Dense(8, activation="relu")])\n    \n    self.decoder = tf.keras.Sequential([\n      layers.Dense(16, activation="relu"),\n      layers.Dense(32, activation="relu"),\n      layers.Dense(140, activation="sigmoid")])\n    \n  def call(self, x):\n    encoded = self.encoder(x)\n    decoded = self.decoder(encoded)\n    return decoded')
plt.plot(history.history['loss'], label='Training Loss')
plt.plot(history.history['val_loss'], label='Validation Loss')
plt.legend()
encoded_data = custom_method(
autoencoder.encoder(normal_test_data).numpy(), imports='from tensorflow.keras.datasets import fashion_mnist;from tensorflow.keras import layers, losses;import pandas as pd;from sklearn.metrics import accuracy_score, precision_score, recall_score;from tensorflow.keras.models import Model;import tensorflow as tf;from sklearn.model_selection import train_test_split;import numpy as np;import matplotlib.pyplot as plt', function_to_run='autoencoder.encoder(obj).numpy()', method_object=eval('normal_test_data'), function_args=[], function_kwargs={}, max_wait_secs=0, custom_class=None)
decoded_data = autoencoder.decoder(encoded_data).numpy()
plt.plot(normal_test_data[0], 'b')
plt.plot(decoded_data[0], 'r')
plt.fill_between(np.arange(140), decoded_data[0], normal_test_data[0], color='lightcoral')
plt.legend(labels=['Input', 'Reconstruction', 'Error'])
plt.show()
encoded_data = custom_method(
autoencoder.encoder(anomalous_test_data).numpy(), imports='from tensorflow.keras.datasets import fashion_mnist;from tensorflow.keras import layers, losses;import pandas as pd;from sklearn.metrics import accuracy_score, precision_score, recall_score;from tensorflow.keras.models import Model;import tensorflow as tf;from sklearn.model_selection import train_test_split;import numpy as np;import matplotlib.pyplot as plt', function_to_run='autoencoder.encoder(obj).numpy()', method_object=eval('anomalous_test_data'), function_args=[], function_kwargs={}, max_wait_secs=0, custom_class=None)
decoded_data = autoencoder.decoder(encoded_data).numpy()
plt.plot(anomalous_test_data[0], 'b')
plt.plot(decoded_data[0], 'r')
plt.fill_between(np.arange(140), decoded_data[0], anomalous_test_data[0], color='lightcoral')
plt.legend(labels=['Input', 'Reconstruction', 'Error'])
plt.show()
reconstructions = custom_method(
autoencoder.predict(normal_train_data), imports='from tensorflow.keras.datasets import fashion_mnist;from tensorflow.keras import layers, losses;import pandas as pd;from sklearn.metrics import accuracy_score, precision_score, recall_score;from tensorflow.keras.models import Model;import tensorflow as tf;from sklearn.model_selection import train_test_split;import numpy as np;import matplotlib.pyplot as plt', function_to_run='obj.predict(*args)', method_object=eval('autoencoder'), function_args=[eval('normal_train_data')], function_kwargs={}, max_wait_secs=0, custom_class='class AnomalyDetector(Model):\n  def __init__(self):\n    super(AnomalyDetector, self).__init__()\n    self.encoder = tf.keras.Sequential([\n      layers.Dense(32, activation="relu"),\n      layers.Dense(16, activation="relu"),\n      layers.Dense(8, activation="relu")])\n    \n    self.decoder = tf.keras.Sequential([\n      layers.Dense(16, activation="relu"),\n      layers.Dense(32, activation="relu"),\n      layers.Dense(140, activation="sigmoid")])\n    \n  def call(self, x):\n    encoded = self.encoder(x)\n    decoded = self.decoder(encoded)\n    return decoded')
train_loss = custom_method(
tf.keras.losses.mae(reconstructions, normal_train_data), imports='from tensorflow.keras.datasets import fashion_mnist;from tensorflow.keras import layers, losses;import pandas as pd;from sklearn.metrics import accuracy_score, precision_score, recall_score;from tensorflow.keras.models import Model;import tensorflow as tf;from sklearn.model_selection import train_test_split;import numpy as np;import matplotlib.pyplot as plt', function_to_run='tf.keras.losses.mae(*args)', method_object=None, function_args=[eval('reconstructions'), eval('normal_train_data')], function_kwargs={}, max_wait_secs=0)
plt.hist(train_loss[None, :], bins=50)
plt.xlabel('Train loss')
plt.ylabel('No of examples')
plt.show()
threshold = np.mean(train_loss) + np.std(train_loss)
print('Threshold: ', threshold)
reconstructions = custom_method(
autoencoder.predict(anomalous_test_data), imports='from tensorflow.keras.datasets import fashion_mnist;from tensorflow.keras import layers, losses;import pandas as pd;from sklearn.metrics import accuracy_score, precision_score, recall_score;from tensorflow.keras.models import Model;import tensorflow as tf;from sklearn.model_selection import train_test_split;import numpy as np;import matplotlib.pyplot as plt', function_to_run='obj.predict(*args)', method_object=eval('autoencoder'), function_args=[eval('anomalous_test_data')], function_kwargs={}, max_wait_secs=0, custom_class='class AnomalyDetector(Model):\n  def __init__(self):\n    super(AnomalyDetector, self).__init__()\n    self.encoder = tf.keras.Sequential([\n      layers.Dense(32, activation="relu"),\n      layers.Dense(16, activation="relu"),\n      layers.Dense(8, activation="relu")])\n    \n    self.decoder = tf.keras.Sequential([\n      layers.Dense(16, activation="relu"),\n      layers.Dense(32, activation="relu"),\n      layers.Dense(140, activation="sigmoid")])\n    \n  def call(self, x):\n    encoded = self.encoder(x)\n    decoded = self.decoder(encoded)\n    return decoded')
test_loss = custom_method(
tf.keras.losses.mae(reconstructions, anomalous_test_data), imports='from tensorflow.keras.datasets import fashion_mnist;from tensorflow.keras import layers, losses;import pandas as pd;from sklearn.metrics import accuracy_score, precision_score, recall_score;from tensorflow.keras.models import Model;import tensorflow as tf;from sklearn.model_selection import train_test_split;import numpy as np;import matplotlib.pyplot as plt', function_to_run='tf.keras.losses.mae(*args)', method_object=None, function_args=[eval('reconstructions'), eval('anomalous_test_data')], function_kwargs={}, max_wait_secs=0)
plt.hist(test_loss[None, :], bins=50)
plt.xlabel('Test loss')
plt.ylabel('No of examples')
plt.show()

def predict(model, data, threshold):
    reconstructions = model(data)
    loss = custom_method(
    tf.keras.losses.mae(reconstructions, data), imports='from tensorflow.keras.datasets import fashion_mnist;from tensorflow.keras import layers, losses;import pandas as pd;from sklearn.metrics import accuracy_score, precision_score, recall_score;from tensorflow.keras.models import Model;import tensorflow as tf;from sklearn.model_selection import train_test_split;import numpy as np;import matplotlib.pyplot as plt', function_to_run='tf.keras.losses.mae(*args)', method_object=None, function_args=[eval('reconstructions'), eval('data')], function_kwargs={}, max_wait_secs=0)
    return custom_method(
    tf.math.less(loss, threshold), imports='from tensorflow.keras.datasets import fashion_mnist;from tensorflow.keras import layers, losses;import pandas as pd;from sklearn.metrics import accuracy_score, precision_score, recall_score;from tensorflow.keras.models import Model;import tensorflow as tf;from sklearn.model_selection import train_test_split;import numpy as np;import matplotlib.pyplot as plt', function_to_run='tf.math.less(*args)', method_object=None, function_args=[eval('loss'), eval('threshold')], function_kwargs={}, max_wait_secs=0)

def print_stats(predictions, labels):
    print('Accuracy = {}'.format(accuracy_score(labels, predictions)))
    print('Precision = {}'.format(precision_score(labels, predictions)))
    print('Recall = {}'.format(recall_score(labels, predictions)))
preds = predict(autoencoder, test_data, threshold)
print_stats(preds, test_labels)
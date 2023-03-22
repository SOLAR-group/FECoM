import matplotlib.pyplot as plt
import tensorflow as tf
import tensorflow_compression as tfc
import tensorflow_datasets as tfds
import os
from pathlib import Path
import dill as pickle
import sys
from tool.client.client_config import EXPERIMENT_DIR, MAX_WAIT_S, WAIT_AFTER_RUN_S
from tool.server.send_request import send_request
from tool.server.function_details import FunctionDetails
current_path = os.path.abspath(__file__)
experiment_number = sys.argv[1]
experiment_project = sys.argv[2]
EXPERIMENT_FILE_PATH = EXPERIMENT_DIR / 'method-level' / experiment_project / f'experiment-{experiment_number}.json'

def custom_method(func, imports: str, function_to_run: str, method_object=None, object_signature=None, function_args: list=None, function_kwargs: dict=None, max_wait_secs=MAX_WAIT_S, custom_class=None, wait_after_run_secs=WAIT_AFTER_RUN_S):
    result = send_request(imports=imports, function_to_run=function_to_run, function_args=function_args, function_kwargs=function_kwargs, max_wait_secs=max_wait_secs, wait_after_run_secs=wait_after_run_secs, method_object=method_object, object_signature=object_signature, custom_class=custom_class, experiment_file_path=EXPERIMENT_FILE_PATH)
    return func

class CustomDense(tf.keras.layers.Layer):

    def __init__(self, filters, name='dense'):
        super().__init__(name=name)
        self.filters = filters

    @classmethod
    def copy(cls, other, **kwargs):
        """Returns an instantiated and built layer, initialized from `other`."""
        self = cls(filters=other.filters, name=other.name, **kwargs)
        self.build(None, other=other)
        return self

    def build(self, input_shape, other=None):
        """Instantiates weights, optionally initializing them from `other`."""
        if other is None:
            kernel_shape = (input_shape[-1], self.filters)
            kernel = custom_method(
            tf.keras.initializers.GlorotUniform()(shape=kernel_shape), imports='import os;import tensorflow as tf;import shutil;import tensorflow_datasets as tfds;import tensorflow_compression as tfc;import matplotlib.pyplot as plt', function_to_run='tf.keras.initializers.GlorotUniform()(**kwargs)', method_object=None, object_signature=None, function_args=[], function_kwargs={'shape': eval('kernel_shape')}, max_wait_secs=0)
            bias = custom_method(
            tf.keras.initializers.Zeros()(shape=(self.filters,)), imports='import os;import tensorflow as tf;import shutil;import tensorflow_datasets as tfds;import tensorflow_compression as tfc;import matplotlib.pyplot as plt', function_to_run='tf.keras.initializers.Zeros()(**kwargs)', method_object=None, object_signature=None, function_args=[], function_kwargs={'shape': eval('(self.filters,)')}, max_wait_secs=0)
        else:
            (kernel, bias) = (other.kernel, other.bias)
        self.kernel = custom_method(
        tf.Variable(tf.cast(kernel, self.variable_dtype), name='kernel'), imports='import os;import tensorflow as tf;import shutil;import tensorflow_datasets as tfds;import tensorflow_compression as tfc;import matplotlib.pyplot as plt', function_to_run='tf.Variable(*args, **kwargs)', method_object=None, object_signature=None, function_args=[eval('tf.cast(kernel, self.variable_dtype)')], function_kwargs={'name': eval('"kernel"')}, max_wait_secs=0)
        self.bias = custom_method(
        tf.Variable(tf.cast(bias, self.variable_dtype), name='bias'), imports='import os;import tensorflow as tf;import shutil;import tensorflow_datasets as tfds;import tensorflow_compression as tfc;import matplotlib.pyplot as plt', function_to_run='tf.Variable(*args, **kwargs)', method_object=None, object_signature=None, function_args=[eval('tf.cast(bias, self.variable_dtype)')], function_kwargs={'name': eval('"bias"')}, max_wait_secs=0)
        self.built = True

    def call(self, inputs):
        outputs = custom_method(
        tf.linalg.matvec(self.kernel, inputs, transpose_a=True), imports='import os;import tensorflow as tf;import shutil;import tensorflow_datasets as tfds;import tensorflow_compression as tfc;import matplotlib.pyplot as plt', function_to_run='tf.linalg.matvec(*args, **kwargs)', method_object=None, object_signature=None, function_args=[eval('self.kernel'), eval('inputs')], function_kwargs={'transpose_a': eval('True')}, max_wait_secs=0)
        outputs = custom_method(
        tf.nn.bias_add(outputs, self.bias), imports='import os;import tensorflow as tf;import shutil;import tensorflow_datasets as tfds;import tensorflow_compression as tfc;import matplotlib.pyplot as plt', function_to_run='tf.nn.bias_add(*args)', method_object=None, object_signature=None, function_args=[eval('outputs'), eval('self.bias')], function_kwargs={}, max_wait_secs=0)
        return custom_method(
        tf.nn.leaky_relu(outputs), imports='import os;import tensorflow as tf;import shutil;import tensorflow_datasets as tfds;import tensorflow_compression as tfc;import matplotlib.pyplot as plt', function_to_run='tf.nn.leaky_relu(*args)', method_object=None, object_signature=None, function_args=[eval('outputs')], function_kwargs={}, max_wait_secs=0)

class CustomConv2D(tf.keras.layers.Layer):

    def __init__(self, filters, kernel_size, strides=1, padding='SAME', name='conv2d'):
        super().__init__(name=name)
        self.filters = filters
        self.kernel_size = kernel_size
        self.strides = strides
        self.padding = padding

    @classmethod
    def copy(cls, other, **kwargs):
        """Returns an instantiated and built layer, initialized from `other`."""
        self = cls(filters=other.filters, kernel_size=other.kernel_size, strides=other.strides, padding=other.padding, name=other.name, **kwargs)
        self.build(None, other=other)
        return self

    def build(self, input_shape, other=None):
        """Instantiates weights, optionally initializing them from `other`."""
        if other is None:
            kernel_shape = 2 * (self.kernel_size,) + (input_shape[-1], self.filters)
            kernel = custom_method(
            tf.keras.initializers.GlorotUniform()(shape=kernel_shape), imports='import os;import tensorflow as tf;import shutil;import tensorflow_datasets as tfds;import tensorflow_compression as tfc;import matplotlib.pyplot as plt', function_to_run='tf.keras.initializers.GlorotUniform()(**kwargs)', method_object=None, object_signature=None, function_args=[], function_kwargs={'shape': eval('kernel_shape')}, max_wait_secs=0)
            bias = custom_method(
            tf.keras.initializers.Zeros()(shape=(self.filters,)), imports='import os;import tensorflow as tf;import shutil;import tensorflow_datasets as tfds;import tensorflow_compression as tfc;import matplotlib.pyplot as plt', function_to_run='tf.keras.initializers.Zeros()(**kwargs)', method_object=None, object_signature=None, function_args=[], function_kwargs={'shape': eval('(self.filters,)')}, max_wait_secs=0)
        else:
            (kernel, bias) = (other.kernel, other.bias)
        self.kernel = custom_method(
        tf.Variable(tf.cast(kernel, self.variable_dtype), name='kernel'), imports='import os;import tensorflow as tf;import shutil;import tensorflow_datasets as tfds;import tensorflow_compression as tfc;import matplotlib.pyplot as plt', function_to_run='tf.Variable(*args, **kwargs)', method_object=None, object_signature=None, function_args=[eval('tf.cast(kernel, self.variable_dtype)')], function_kwargs={'name': eval('"kernel"')}, max_wait_secs=0)
        self.bias = custom_method(
        tf.Variable(tf.cast(bias, self.variable_dtype), name='bias'), imports='import os;import tensorflow as tf;import shutil;import tensorflow_datasets as tfds;import tensorflow_compression as tfc;import matplotlib.pyplot as plt', function_to_run='tf.Variable(*args, **kwargs)', method_object=None, object_signature=None, function_args=[eval('tf.cast(bias, self.variable_dtype)')], function_kwargs={'name': eval('"bias"')}, max_wait_secs=0)
        self.built = True

    def call(self, inputs):
        outputs = custom_method(
        tf.nn.convolution(inputs, self.kernel, strides=self.strides, padding=self.padding), imports='import os;import tensorflow as tf;import shutil;import tensorflow_datasets as tfds;import tensorflow_compression as tfc;import matplotlib.pyplot as plt', function_to_run='tf.nn.convolution(*args, **kwargs)', method_object=None, object_signature=None, function_args=[eval('inputs'), eval('self.kernel')], function_kwargs={'strides': eval('self.strides'), 'padding': eval('self.padding')}, max_wait_secs=0)
        outputs = custom_method(
        tf.nn.bias_add(outputs, self.bias), imports='import os;import tensorflow as tf;import shutil;import tensorflow_datasets as tfds;import tensorflow_compression as tfc;import matplotlib.pyplot as plt', function_to_run='tf.nn.bias_add(*args)', method_object=None, object_signature=None, function_args=[eval('outputs'), eval('self.bias')], function_kwargs={}, max_wait_secs=0)
        return custom_method(
        tf.nn.leaky_relu(outputs), imports='import os;import tensorflow as tf;import shutil;import tensorflow_datasets as tfds;import tensorflow_compression as tfc;import matplotlib.pyplot as plt', function_to_run='tf.nn.leaky_relu(*args)', method_object=None, object_signature=None, function_args=[eval('outputs')], function_kwargs={}, max_wait_secs=0)
classifier = custom_method(
tf.keras.Sequential([CustomConv2D(20, 5, strides=2, name='conv_1'), CustomConv2D(50, 5, strides=2, name='conv_2'), tf.keras.layers.Flatten(), CustomDense(500, name='fc_1'), CustomDense(10, name='fc_2')], name='classifier'), imports='import os;import tensorflow as tf;import shutil;import tensorflow_datasets as tfds;import tensorflow_compression as tfc;import matplotlib.pyplot as plt', function_to_run='tf.keras.Sequential(*args, **kwargs)', method_object=None, object_signature=None, function_args=[eval('[\n    CustomConv2D(20, 5, strides=2, name="conv_1"),\n    CustomConv2D(50, 5, strides=2, name="conv_2"),\n    tf.keras.layers.Flatten(),\n    CustomDense(500, name="fc_1"),\n    CustomDense(10, name="fc_2"),\n]')], function_kwargs={'name': eval('"classifier"')}, max_wait_secs=0)

def normalize_img(image, label):
    """Normalizes images: `uint8` -> `float32`."""
    return (custom_method(
    tf.cast(image, tf.float32), imports='import os;import tensorflow as tf;import shutil;import tensorflow_datasets as tfds;import tensorflow_compression as tfc;import matplotlib.pyplot as plt', function_to_run='tf.cast(*args)', method_object=None, object_signature=None, function_args=[eval('image'), eval('tf.float32')], function_kwargs={}, max_wait_secs=0) / 255.0, label)
(training_dataset, validation_dataset) = custom_method(
tfds.load('mnist', split=['train', 'test'], shuffle_files=True, as_supervised=True, with_info=False), imports='import os;import tensorflow as tf;import shutil;import tensorflow_datasets as tfds;import tensorflow_compression as tfc;import matplotlib.pyplot as plt', function_to_run='tfds.load(*args, **kwargs)', method_object=None, object_signature=None, function_args=[eval('"mnist"')], function_kwargs={'split': eval('["train", "test"]'), 'shuffle_files': eval('True'), 'as_supervised': eval('True'), 'with_info': eval('False')}, max_wait_secs=0)
training_dataset = training_dataset.map(normalize_img)
validation_dataset = validation_dataset.map(normalize_img)

def train_model(model, training_data, validation_data, **kwargs):
    model.compile(optimizer=tf.keras.optimizers.Adam(learning_rate=0.001), loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True), metrics=[tf.keras.metrics.SparseCategoricalAccuracy()])
    kwargs.setdefault('epochs', 5)
    kwargs.setdefault('verbose', 1)
    log = model.fit(training_data.batch(128).prefetch(8), validation_data=validation_data.batch(128).cache(), validation_freq=1, **kwargs)
    return log.history['val_sparse_categorical_accuracy'][-1]
classifier_accuracy = train_model(classifier, training_dataset, validation_dataset)
print(f'Accuracy: {classifier_accuracy:0.4f}')
_ = custom_method(
tf.linspace(-5.0, 5.0, 501), imports='import os;import tensorflow as tf;import shutil;import tensorflow_datasets as tfds;import tensorflow_compression as tfc;import matplotlib.pyplot as plt', function_to_run='tf.linspace(*args)', method_object=None, object_signature=None, function_args=[eval('-5.'), eval('5.'), eval('501')], function_kwargs={}, max_wait_secs=0)
plt.plot(_, tfc.PowerLawEntropyModel(0).penalty(_))

class PowerLawRegularizer(tf.keras.regularizers.Regularizer):

    def __init__(self, lmbda):
        super().__init__()
        self.lmbda = lmbda

    def __call__(self, variable):
        em = custom_method(
        tfc.PowerLawEntropyModel(coding_rank=variable.shape.rank), imports='import os;import tensorflow as tf;import shutil;import tensorflow_datasets as tfds;import tensorflow_compression as tfc;import matplotlib.pyplot as plt', function_to_run='tfc.PowerLawEntropyModel(**kwargs)', method_object=None, object_signature=None, function_args=[], function_kwargs={'coding_rank': eval('variable.shape.rank')}, max_wait_secs=0)
        return self.lmbda * custom_method(
        em.penalty(variable), imports='import os;import tensorflow as tf;import shutil;import tensorflow_datasets as tfds;import tensorflow_compression as tfc;import matplotlib.pyplot as plt', function_to_run='obj.penalty(*args)', method_object=eval('em'), object_signature='tfc.PowerLawEntropyModel', function_args=[eval('variable')], function_kwargs={}, max_wait_secs=0, custom_class=None)
regularizer = PowerLawRegularizer(lmbda=2.0 / classifier.count_params())

def quantize(latent, log_step):
    step = custom_method(
    tf.exp(log_step), imports='import os;import tensorflow as tf;import shutil;import tensorflow_datasets as tfds;import tensorflow_compression as tfc;import matplotlib.pyplot as plt', function_to_run='tf.exp(*args)', method_object=None, object_signature=None, function_args=[eval('log_step')], function_kwargs={}, max_wait_secs=0)
    return custom_method(
    tfc.round_st(latent / step), imports='import os;import tensorflow as tf;import shutil;import tensorflow_datasets as tfds;import tensorflow_compression as tfc;import matplotlib.pyplot as plt', function_to_run='tfc.round_st(*args)', method_object=None, object_signature=None, function_args=[eval('latent / step')], function_kwargs={}, max_wait_secs=0) * step

class CompressibleDense(CustomDense):

    def __init__(self, regularizer, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.regularizer = regularizer

    def build(self, input_shape, other=None):
        """Instantiates weights, optionally initializing them from `other`."""
        super().build(input_shape, other=other)
        if other is not None and hasattr(other, 'kernel_log_step'):
            kernel_log_step = other.kernel_log_step
            bias_log_step = other.bias_log_step
        else:
            kernel_log_step = bias_log_step = -4.0
        self.kernel_log_step = custom_method(
        tf.Variable(tf.cast(kernel_log_step, self.variable_dtype), name='kernel_log_step'), imports='import os;import tensorflow as tf;import shutil;import tensorflow_datasets as tfds;import tensorflow_compression as tfc;import matplotlib.pyplot as plt', function_to_run='tf.Variable(*args, **kwargs)', method_object=None, object_signature=None, function_args=[eval('tf.cast(kernel_log_step, self.variable_dtype)')], function_kwargs={'name': eval('"kernel_log_step"')}, max_wait_secs=0)
        self.bias_log_step = custom_method(
        tf.Variable(tf.cast(bias_log_step, self.variable_dtype), name='bias_log_step'), imports='import os;import tensorflow as tf;import shutil;import tensorflow_datasets as tfds;import tensorflow_compression as tfc;import matplotlib.pyplot as plt', function_to_run='tf.Variable(*args, **kwargs)', method_object=None, object_signature=None, function_args=[eval('tf.cast(bias_log_step, self.variable_dtype)')], function_kwargs={'name': eval('"bias_log_step"')}, max_wait_secs=0)
        self.add_loss(lambda : self.regularizer(self.kernel_latent / tf.exp(self.kernel_log_step)))
        self.add_loss(lambda : self.regularizer(self.bias_latent / tf.exp(self.bias_log_step)))

    @property
    def kernel(self):
        return quantize(self.kernel_latent, self.kernel_log_step)

    @kernel.setter
    def kernel(self, kernel):
        self.kernel_latent = custom_method(
        tf.Variable(kernel, name='kernel_latent'), imports='import os;import tensorflow as tf;import shutil;import tensorflow_datasets as tfds;import tensorflow_compression as tfc;import matplotlib.pyplot as plt', function_to_run='tf.Variable(*args, **kwargs)', method_object=None, object_signature=None, function_args=[eval('kernel')], function_kwargs={'name': eval('"kernel_latent"')}, max_wait_secs=0)

    @property
    def bias(self):
        return quantize(self.bias_latent, self.bias_log_step)

    @bias.setter
    def bias(self, bias):
        self.bias_latent = custom_method(
        tf.Variable(bias, name='bias_latent'), imports='import os;import tensorflow as tf;import shutil;import tensorflow_datasets as tfds;import tensorflow_compression as tfc;import matplotlib.pyplot as plt', function_to_run='tf.Variable(*args, **kwargs)', method_object=None, object_signature=None, function_args=[eval('bias')], function_kwargs={'name': eval('"bias_latent"')}, max_wait_secs=0)

def to_rdft(kernel, kernel_size):
    kernel = custom_method(
    tf.transpose(kernel, (2, 3, 0, 1)), imports='import os;import tensorflow as tf;import shutil;import tensorflow_datasets as tfds;import tensorflow_compression as tfc;import matplotlib.pyplot as plt', function_to_run='tf.transpose(*args)', method_object=None, object_signature=None, function_args=[eval('kernel'), eval('(2, 3, 0, 1)')], function_kwargs={}, max_wait_secs=0)
    kernel_rdft = custom_method(
    tf.signal.rfft2d(kernel), imports='import os;import tensorflow as tf;import shutil;import tensorflow_datasets as tfds;import tensorflow_compression as tfc;import matplotlib.pyplot as plt', function_to_run='tf.signal.rfft2d(*args)', method_object=None, object_signature=None, function_args=[eval('kernel')], function_kwargs={}, max_wait_secs=0)
    kernel_rdft = custom_method(
    tf.stack([tf.math.real(kernel_rdft), tf.math.imag(kernel_rdft)], axis=-1), imports='import os;import tensorflow as tf;import shutil;import tensorflow_datasets as tfds;import tensorflow_compression as tfc;import matplotlib.pyplot as plt', function_to_run='tf.stack(*args, **kwargs)', method_object=None, object_signature=None, function_args=[eval('[tf.math.real(kernel_rdft), tf.math.imag(kernel_rdft)]')], function_kwargs={'axis': eval('-1')}, max_wait_secs=0)
    return kernel_rdft / kernel_size

def from_rdft(kernel_rdft, kernel_size):
    kernel_rdft *= kernel_size
    kernel_rdft = custom_method(
    tf.dtypes.complex(*tf.unstack(kernel_rdft, axis=-1)), imports='import os;import tensorflow as tf;import shutil;import tensorflow_datasets as tfds;import tensorflow_compression as tfc;import matplotlib.pyplot as plt', function_to_run='tf.dtypes.complex(*args)', method_object=None, object_signature=None, function_args=[eval('*tf.unstack(kernel_rdft, axis=-1)')], function_kwargs={}, max_wait_secs=0)
    kernel = custom_method(
    tf.signal.irfft2d(kernel_rdft, fft_length=2 * (kernel_size,)), imports='import os;import tensorflow as tf;import shutil;import tensorflow_datasets as tfds;import tensorflow_compression as tfc;import matplotlib.pyplot as plt', function_to_run='tf.signal.irfft2d(*args, **kwargs)', method_object=None, object_signature=None, function_args=[eval('kernel_rdft')], function_kwargs={'fft_length': eval('2 * (kernel_size,)')}, max_wait_secs=0)
    return custom_method(
    tf.transpose(kernel, (2, 3, 0, 1)), imports='import os;import tensorflow as tf;import shutil;import tensorflow_datasets as tfds;import tensorflow_compression as tfc;import matplotlib.pyplot as plt', function_to_run='tf.transpose(*args)', method_object=None, object_signature=None, function_args=[eval('kernel'), eval('(2, 3, 0, 1)')], function_kwargs={}, max_wait_secs=0)

class CompressibleConv2D(CustomConv2D):

    def __init__(self, regularizer, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.regularizer = regularizer

    def build(self, input_shape, other=None):
        """Instantiates weights, optionally initializing them from `other`."""
        super().build(input_shape, other=other)
        if other is not None and hasattr(other, 'kernel_log_step'):
            kernel_log_step = other.kernel_log_step
            bias_log_step = other.bias_log_step
        else:
            kernel_log_step = custom_method(
            tf.fill(self.kernel_latent.shape[2:], -4.0), imports='import os;import tensorflow as tf;import shutil;import tensorflow_datasets as tfds;import tensorflow_compression as tfc;import matplotlib.pyplot as plt', function_to_run='tf.fill(*args)', method_object=None, object_signature=None, function_args=[eval('self.kernel_latent.shape[2:]'), eval('-4.')], function_kwargs={}, max_wait_secs=0)
            bias_log_step = -4.0
        self.kernel_log_step = custom_method(
        tf.Variable(tf.cast(kernel_log_step, self.variable_dtype), name='kernel_log_step'), imports='import os;import tensorflow as tf;import shutil;import tensorflow_datasets as tfds;import tensorflow_compression as tfc;import matplotlib.pyplot as plt', function_to_run='tf.Variable(*args, **kwargs)', method_object=None, object_signature=None, function_args=[eval('tf.cast(kernel_log_step, self.variable_dtype)')], function_kwargs={'name': eval('"kernel_log_step"')}, max_wait_secs=0)
        self.bias_log_step = custom_method(
        tf.Variable(tf.cast(bias_log_step, self.variable_dtype), name='bias_log_step'), imports='import os;import tensorflow as tf;import shutil;import tensorflow_datasets as tfds;import tensorflow_compression as tfc;import matplotlib.pyplot as plt', function_to_run='tf.Variable(*args, **kwargs)', method_object=None, object_signature=None, function_args=[eval('tf.cast(bias_log_step, self.variable_dtype)')], function_kwargs={'name': eval('"bias_log_step"')}, max_wait_secs=0)
        self.add_loss(lambda : self.regularizer(self.kernel_latent / tf.exp(self.kernel_log_step)))
        self.add_loss(lambda : self.regularizer(self.bias_latent / tf.exp(self.bias_log_step)))

    @property
    def kernel(self):
        kernel_rdft = quantize(self.kernel_latent, self.kernel_log_step)
        return from_rdft(kernel_rdft, self.kernel_size)

    @kernel.setter
    def kernel(self, kernel):
        kernel_rdft = to_rdft(kernel, self.kernel_size)
        self.kernel_latent = custom_method(
        tf.Variable(kernel_rdft, name='kernel_latent'), imports='import os;import tensorflow as tf;import shutil;import tensorflow_datasets as tfds;import tensorflow_compression as tfc;import matplotlib.pyplot as plt', function_to_run='tf.Variable(*args, **kwargs)', method_object=None, object_signature=None, function_args=[eval('kernel_rdft')], function_kwargs={'name': eval('"kernel_latent"')}, max_wait_secs=0)

    @property
    def bias(self):
        return quantize(self.bias_latent, self.bias_log_step)

    @bias.setter
    def bias(self, bias):
        self.bias_latent = custom_method(
        tf.Variable(bias, name='bias_latent'), imports='import os;import tensorflow as tf;import shutil;import tensorflow_datasets as tfds;import tensorflow_compression as tfc;import matplotlib.pyplot as plt', function_to_run='tf.Variable(*args, **kwargs)', method_object=None, object_signature=None, function_args=[eval('bias')], function_kwargs={'name': eval('"bias_latent"')}, max_wait_secs=0)

def make_mnist_classifier(regularizer):
    return custom_method(
    tf.keras.Sequential([CompressibleConv2D(regularizer, 20, 5, strides=2, name='conv_1'), CompressibleConv2D(regularizer, 50, 5, strides=2, name='conv_2'), tf.keras.layers.Flatten(), CompressibleDense(regularizer, 500, name='fc_1'), CompressibleDense(regularizer, 10, name='fc_2')], name='classifier'), imports='import os;import tensorflow as tf;import shutil;import tensorflow_datasets as tfds;import tensorflow_compression as tfc;import matplotlib.pyplot as plt', function_to_run='tf.keras.Sequential(*args, **kwargs)', method_object=None, object_signature=None, function_args=[eval('[\n      CompressibleConv2D(regularizer, 20, 5, strides=2, name="conv_1"),\n      CompressibleConv2D(regularizer, 50, 5, strides=2, name="conv_2"),\n      tf.keras.layers.Flatten(),\n      CompressibleDense(regularizer, 500, name="fc_1"),\n      CompressibleDense(regularizer, 10, name="fc_2"),\n  ]')], function_kwargs={'name': eval('"classifier"')}, max_wait_secs=0)
compressible_classifier = make_mnist_classifier(regularizer)
penalized_accuracy = train_model(compressible_classifier, training_dataset, validation_dataset)
print(f'Accuracy: {penalized_accuracy:0.4f}')

def compress_latent(latent, log_step, name):
    em = custom_method(
    tfc.PowerLawEntropyModel(latent.shape.rank), imports='import os;import tensorflow as tf;import shutil;import tensorflow_datasets as tfds;import tensorflow_compression as tfc;import matplotlib.pyplot as plt', function_to_run='tfc.PowerLawEntropyModel(*args)', method_object=None, object_signature=None, function_args=[eval('latent.shape.rank')], function_kwargs={}, max_wait_secs=0)
    compressed = custom_method(
    em.compress(latent / tf.exp(log_step)), imports='import os;import tensorflow as tf;import shutil;import tensorflow_datasets as tfds;import tensorflow_compression as tfc;import matplotlib.pyplot as plt', function_to_run='obj.compress(*args)', method_object=eval('em'), object_signature='tfc.PowerLawEntropyModel', function_args=[eval('latent / tf.exp(log_step)')], function_kwargs={}, max_wait_secs=0, custom_class=None)
    compressed = custom_method(
    tf.Variable(compressed, name=f'{name}_compressed'), imports='import os;import tensorflow as tf;import shutil;import tensorflow_datasets as tfds;import tensorflow_compression as tfc;import matplotlib.pyplot as plt', function_to_run='tf.Variable(*args, **kwargs)', method_object=None, object_signature=None, function_args=[eval('compressed')], function_kwargs={'name': eval('f"{name}_compressed"')}, max_wait_secs=0)
    log_step = custom_method(
    tf.cast(log_step, tf.float16), imports='import os;import tensorflow as tf;import shutil;import tensorflow_datasets as tfds;import tensorflow_compression as tfc;import matplotlib.pyplot as plt', function_to_run='tf.cast(*args)', method_object=None, object_signature=None, function_args=[eval('log_step'), eval('tf.float16')], function_kwargs={}, max_wait_secs=0)
    log_step = custom_method(
    tf.Variable(log_step, name=f'{name}_log_step'), imports='import os;import tensorflow as tf;import shutil;import tensorflow_datasets as tfds;import tensorflow_compression as tfc;import matplotlib.pyplot as plt', function_to_run='tf.Variable(*args, **kwargs)', method_object=None, object_signature=None, function_args=[eval('log_step')], function_kwargs={'name': eval('f"{name}_log_step"')}, max_wait_secs=0)
    return (compressed, log_step)

def decompress_latent(compressed, shape, log_step):
    latent = custom_method(
    tfc.PowerLawEntropyModel(len(shape)).decompress(compressed, shape), imports='import os;import tensorflow as tf;import shutil;import tensorflow_datasets as tfds;import tensorflow_compression as tfc;import matplotlib.pyplot as plt', function_to_run='tfc.PowerLawEntropyModel(len(shape)).decompress(*args)', method_object=None, object_signature=None, function_args=[eval('compressed'), eval('shape')], function_kwargs={}, max_wait_secs=0)
    step = custom_method(
    tf.exp(tf.cast(log_step, latent.dtype)), imports='import os;import tensorflow as tf;import shutil;import tensorflow_datasets as tfds;import tensorflow_compression as tfc;import matplotlib.pyplot as plt', function_to_run='tf.exp(*args)', method_object=None, object_signature=None, function_args=[eval('tf.cast(log_step, latent.dtype)')], function_kwargs={}, max_wait_secs=0)
    return latent * step

class CompressedDense(CustomDense):

    def build(self, input_shape, other=None):
        assert isinstance(other, CompressibleDense)
        self.input_channels = other.kernel.shape[0]
        (self.kernel_compressed, self.kernel_log_step) = compress_latent(other.kernel_latent, other.kernel_log_step, 'kernel')
        (self.bias_compressed, self.bias_log_step) = compress_latent(other.bias_latent, other.bias_log_step, 'bias')
        self.built = True

    @property
    def kernel(self):
        kernel_shape = (self.input_channels, self.filters)
        return decompress_latent(self.kernel_compressed, kernel_shape, self.kernel_log_step)

    @property
    def bias(self):
        bias_shape = (self.filters,)
        return decompress_latent(self.bias_compressed, bias_shape, self.bias_log_step)

class CompressedConv2D(CustomConv2D):

    def build(self, input_shape, other=None):
        assert isinstance(other, CompressibleConv2D)
        self.input_channels = other.kernel.shape[2]
        (self.kernel_compressed, self.kernel_log_step) = compress_latent(other.kernel_latent, other.kernel_log_step, 'kernel')
        (self.bias_compressed, self.bias_log_step) = compress_latent(other.bias_latent, other.bias_log_step, 'bias')
        self.built = True

    @property
    def kernel(self):
        rdft_shape = (self.input_channels, self.filters, self.kernel_size, self.kernel_size // 2 + 1, 2)
        kernel_rdft = decompress_latent(self.kernel_compressed, rdft_shape, self.kernel_log_step)
        return from_rdft(kernel_rdft, self.kernel_size)

    @property
    def bias(self):
        bias_shape = (self.filters,)
        return decompress_latent(self.bias_compressed, bias_shape, self.bias_log_step)

def compress_layer(layer):
    if isinstance(layer, CompressibleDense):
        return CompressedDense.copy(layer)
    if isinstance(layer, CompressibleConv2D):
        return CompressedConv2D.copy(layer)
    return type(layer).from_config(layer.get_config())
compressed_classifier = custom_method(
tf.keras.models.clone_model(compressible_classifier, clone_function=compress_layer), imports='import os;import tensorflow as tf;import shutil;import tensorflow_datasets as tfds;import tensorflow_compression as tfc;import matplotlib.pyplot as plt', function_to_run='tf.keras.models.clone_model(*args, **kwargs)', method_object=None, object_signature=None, function_args=[eval('compressible_classifier')], function_kwargs={'clone_function': eval('compress_layer')}, max_wait_secs=0)
custom_method(
compressed_classifier.compile(metrics=[tf.keras.metrics.SparseCategoricalAccuracy()]), imports='import os;import tensorflow as tf;import shutil;import tensorflow_datasets as tfds;import tensorflow_compression as tfc;import matplotlib.pyplot as plt', function_to_run='obj.compile(**kwargs)', method_object=eval('compressed_classifier'), object_signature='tf.keras.models.clone_model', function_args=[], function_kwargs={'metrics': eval('[tf.keras.metrics.SparseCategoricalAccuracy()]')}, max_wait_secs=0, custom_class=None)
(_, compressed_accuracy) = custom_method(
compressed_classifier.evaluate(validation_dataset.batch(128)), imports='import os;import tensorflow as tf;import shutil;import tensorflow_datasets as tfds;import tensorflow_compression as tfc;import matplotlib.pyplot as plt', function_to_run='obj.evaluate(*args)', method_object=eval('compressed_classifier'), object_signature='tf.keras.models.clone_model', function_args=[eval('validation_dataset.batch(128)')], function_kwargs={}, max_wait_secs=0, custom_class=None)
print(f'Accuracy of the compressible classifier: {penalized_accuracy:0.4f}')
print(f'Accuracy of the compressed classifier: {compressed_accuracy:0.4f}')

def get_weight_size_in_bytes(weight):
    if weight.dtype == tf.string:
        return custom_method(
        tf.reduce_sum(tf.strings.length(weight, unit='BYTE')), imports='import os;import tensorflow as tf;import shutil;import tensorflow_datasets as tfds;import tensorflow_compression as tfc;import matplotlib.pyplot as plt', function_to_run='tf.reduce_sum(*args)', method_object=None, object_signature=None, function_args=[eval('tf.strings.length(weight, unit="BYTE")')], function_kwargs={}, max_wait_secs=0)
    else:
        return custom_method(
        tf.size(weight), imports='import os;import tensorflow as tf;import shutil;import tensorflow_datasets as tfds;import tensorflow_compression as tfc;import matplotlib.pyplot as plt', function_to_run='tf.size(*args)', method_object=None, object_signature=None, function_args=[eval('weight')], function_kwargs={}, max_wait_secs=0) * weight.dtype.size
original_size = sum(map(get_weight_size_in_bytes, classifier.weights))
compressed_size = sum(map(get_weight_size_in_bytes, compressed_classifier.weights))
print(f'Size of original model weights: {original_size} bytes')
print(f'Size of compressed model weights: {compressed_size} bytes')
print(f'Compression ratio: {original_size / compressed_size:0.0f}x')
import os
import shutil

def get_disk_size(model, path):
    model.save(path)
    zip_path = shutil.make_archive(path, 'zip', path)
    return os.path.getsize(zip_path)
original_zip_size = get_disk_size(classifier, '/tmp/classifier')
compressed_zip_size = get_disk_size(compressed_classifier, '/tmp/compressed_classifier')
print(f'Original on-disk size (ZIP compressed): {original_zip_size} bytes')
print(f'Compressed on-disk size (ZIP compressed): {compressed_zip_size} bytes')
print(f'Compression ratio: {original_zip_size / compressed_zip_size:0.0f}x')
print(f'Accuracy of the vanilla classifier: {classifier_accuracy:0.4f}')
print(f'Accuracy of the penalized classifier: {penalized_accuracy:0.4f}')

def compress_and_evaluate_model(lmbda):
    print(f'lambda={lmbda:0.0f}: training...', flush=True)
    regularizer = PowerLawRegularizer(lmbda=lmbda / classifier.count_params())
    compressible_classifier = make_mnist_classifier(regularizer)
    train_model(compressible_classifier, training_dataset, validation_dataset, verbose=0)
    print('compressing...', flush=True)
    compressed_classifier = custom_method(
    tf.keras.models.clone_model(compressible_classifier, clone_function=compress_layer), imports='import os;import tensorflow as tf;import shutil;import tensorflow_datasets as tfds;import tensorflow_compression as tfc;import matplotlib.pyplot as plt', function_to_run='tf.keras.models.clone_model(*args, **kwargs)', method_object=None, object_signature=None, function_args=[eval('compressible_classifier')], function_kwargs={'clone_function': eval('compress_layer')}, max_wait_secs=0)
    compressed_size = sum(map(get_weight_size_in_bytes, compressed_classifier.weights))
    compressed_zip_size = float(get_disk_size(compressed_classifier, '/tmp/compressed_classifier'))
    print('evaluating...', flush=True)
    compressed_classifier = custom_method(
    tf.keras.models.load_model('/tmp/compressed_classifier'), imports='import os;import tensorflow as tf;import shutil;import tensorflow_datasets as tfds;import tensorflow_compression as tfc;import matplotlib.pyplot as plt', function_to_run='tf.keras.models.load_model(*args)', method_object=None, object_signature=None, function_args=[eval('"/tmp/compressed_classifier"')], function_kwargs={}, max_wait_secs=0)
    custom_method(
    compressed_classifier.compile(metrics=[tf.keras.metrics.SparseCategoricalAccuracy()]), imports='import os;import tensorflow as tf;import shutil;import tensorflow_datasets as tfds;import tensorflow_compression as tfc;import matplotlib.pyplot as plt', function_to_run='obj.compile(**kwargs)', method_object=eval('compressed_classifier'), object_signature='tf.keras.models.clone_model', function_args=[], function_kwargs={'metrics': eval('[tf.keras.metrics.SparseCategoricalAccuracy()]')}, max_wait_secs=0, custom_class=None)
    (_, compressed_accuracy) = custom_method(
    compressed_classifier.evaluate(validation_dataset.batch(128), verbose=0), imports='import os;import tensorflow as tf;import shutil;import tensorflow_datasets as tfds;import tensorflow_compression as tfc;import matplotlib.pyplot as plt', function_to_run='obj.evaluate(*args, **kwargs)', method_object=eval('compressed_classifier'), object_signature='tf.keras.models.clone_model', function_args=[eval('validation_dataset.batch(128)')], function_kwargs={'verbose': eval('0')}, max_wait_secs=0, custom_class=None)
    print()
    return (compressed_size, compressed_zip_size, compressed_accuracy)
lambdas = (2.0, 5.0, 10.0, 20.0, 50.0)
metrics = [compress_and_evaluate_model(l) for l in lambdas]
metrics = custom_method(
tf.convert_to_tensor(metrics, tf.float32), imports='import os;import tensorflow as tf;import shutil;import tensorflow_datasets as tfds;import tensorflow_compression as tfc;import matplotlib.pyplot as plt', function_to_run='tf.convert_to_tensor(*args)', method_object=None, object_signature=None, function_args=[eval('metrics'), eval('tf.float32')], function_kwargs={}, max_wait_secs=0)

def plot_broken_xaxis(ax, compressed_sizes, original_size, original_accuracy):
    xticks = list(range(int(tf.math.floor(min(compressed_sizes) / 5) * 5), int(tf.math.ceil(max(compressed_sizes) / 5) * 5) + 1, 5))
    xticks.append(xticks[-1] + 10)
    ax.set_xlim(xticks[0], xticks[-1] + 2)
    ax.set_xticks(xticks[1:])
    ax.set_xticklabels(xticks[1:-1] + [f'{original_size:0.2f}'])
    ax.plot(xticks[-1], original_accuracy, 'o', label='float32')
(sizes, zip_sizes, accuracies) = custom_method(
tf.transpose(metrics), imports='import os;import tensorflow as tf;import shutil;import tensorflow_datasets as tfds;import tensorflow_compression as tfc;import matplotlib.pyplot as plt', function_to_run='tf.transpose(*args)', method_object=None, object_signature=None, function_args=[eval('metrics')], function_kwargs={}, max_wait_secs=0)
sizes /= 1024
zip_sizes /= 1024
(fig, (axl, axr)) = plt.subplots(1, 2, sharey=True, figsize=(10, 4))
axl.plot(sizes, accuracies, 'o-', label='EPR compressed')
axr.plot(zip_sizes, accuracies, 'o-', label='EPR compressed')
plot_broken_xaxis(axl, sizes, original_size / 1024, classifier_accuracy)
plot_broken_xaxis(axr, zip_sizes, original_zip_size / 1024, classifier_accuracy)
axl.set_xlabel('size of model weights [kbytes]')
axr.set_xlabel('ZIP compressed on-disk model size [kbytes]')
axl.set_ylabel('accuracy')
axl.legend(loc='lower right')
axr.legend(loc='lower right')
axl.grid()
axr.grid()
for i in range(len(lambdas)):
    axl.annotate(f'$\\lambda = {lambdas[i]:0.0f}$', (sizes[i], accuracies[i]), xytext=(10, -5), xycoords='data', textcoords='offset points')
    axr.annotate(f'$\\lambda = {lambdas[i]:0.0f}$', (zip_sizes[i], accuracies[i]), xytext=(10, -5), xycoords='data', textcoords='offset points')
plt.tight_layout()

def decompress_layer(layer):
    if isinstance(layer, CompressedDense):
        return CustomDense.copy(layer)
    if isinstance(layer, CompressedConv2D):
        return CustomConv2D.copy(layer)
    return type(layer).from_config(layer.get_config())
decompressed_classifier = custom_method(
tf.keras.models.clone_model(compressed_classifier, clone_function=decompress_layer), imports='import os;import tensorflow as tf;import shutil;import tensorflow_datasets as tfds;import tensorflow_compression as tfc;import matplotlib.pyplot as plt', function_to_run='tf.keras.models.clone_model(*args, **kwargs)', method_object=None, object_signature=None, function_args=[eval('compressed_classifier')], function_kwargs={'clone_function': eval('decompress_layer')}, max_wait_secs=0)
decompressed_accuracy = train_model(decompressed_classifier, training_dataset, validation_dataset, epochs=1)
print(f'Accuracy of the compressed classifier: {compressed_accuracy:0.4f}')
print(f'Accuracy of the decompressed classifier after one more epoch of training: {decompressed_accuracy:0.4f}')

def decompress_layer_with_penalty(layer):
    if isinstance(layer, CompressedDense):
        return CompressibleDense.copy(layer, regularizer=regularizer)
    if isinstance(layer, CompressedConv2D):
        return CompressibleConv2D.copy(layer, regularizer=regularizer)
    return type(layer).from_config(layer.get_config())
decompressed_classifier = custom_method(
tf.keras.models.clone_model(compressed_classifier, clone_function=decompress_layer_with_penalty), imports='import os;import tensorflow as tf;import shutil;import tensorflow_datasets as tfds;import tensorflow_compression as tfc;import matplotlib.pyplot as plt', function_to_run='tf.keras.models.clone_model(*args, **kwargs)', method_object=None, object_signature=None, function_args=[eval('compressed_classifier')], function_kwargs={'clone_function': eval('decompress_layer_with_penalty')}, max_wait_secs=0)
decompressed_accuracy = train_model(decompressed_classifier, training_dataset, validation_dataset, epochs=1)
print(f'Accuracy of the compressed classifier: {compressed_accuracy:0.4f}')
print(f'Accuracy of the decompressed classifier after one more epoch of training: {decompressed_accuracy:0.4f}')

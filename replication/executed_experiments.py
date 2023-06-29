"""
Keep track of projects for which experiment have been executed such that
their data can be analysed and plotted.
"""

EXECUTED_EXPERIMENTS = [
    # "audio/simple_audio", # missing data for some methods in some experiments
    "audio/transfer_learning_audio",
    "estimator/keras_model_to_estimator",
    "estimator/linear",
    "estimator/premade",
    "generative/adversarial_fgsm",
    "generative/autoencoder",
    # "generative/cvae", # using skip_calls, needs update in analysis script
    "images/cnn",
    "keras/classification",
    "keras/overfit_and_underfit",
    "keras/regression",
    "keras/save_and_load",
    "load_data/numpy",
    "quickstart/advanced",
    "quickstart/beginner",
    "structured_data/feature_columns",
    "structured_data/imbalanced_data"
]
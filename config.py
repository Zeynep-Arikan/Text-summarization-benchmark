# Dataset configuration
DATASET_NAME = 'cnn_dailymail'
DATASET_VERSION = '3.0.0'
NUM_SAMPLES = 3

# Model configuration
MODELS = [
    'google/flan-t5-small',
    't5-small',
    'sshleifer/distilbart-cnn-12-6'
]

# Text processing configuration
MAX_INPUT_LENGTH = 512  # Maximum input length for models
MAX_SUMMARY_LENGTH = 100  # Reduced from 130 to 100
MIN_SUMMARY_LENGTH = 30

# Evaluation configuration
METRICS = ['rouge1', 'rouge2', 'rougeL']

# Output configuration
OUTPUT_DIR = 'results'

# Model generation configuration
GENERATION_CONFIG = {
    'do_sample': False,
    'num_beams': 4,  # Beam search for better summaries
    'early_stopping': True
} 
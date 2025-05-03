import os
from datetime import datetime

def truncate_text(text, max_length):
    """Truncate text to a maximum number of words."""
    words = text.split()
    if len(words) > max_length:
        return ' '.join(words[:max_length])
    return text

def ensure_dir(directory):
    """Create directory if it doesn't exist."""
    if not os.path.exists(directory):
        os.makedirs(directory)

def get_timestamp():
    """Get current timestamp in a formatted string."""
    return datetime.now().strftime("%Y%m%d_%H%M%S")

def format_rouge_scores(scores):
    """Format ROUGE scores for better readability."""
    return {k: round(v * 100, 2) for k, v in scores.items()} 
from transformers import pipeline
from utils import truncate_text
from config import MAX_INPUT_LENGTH, MAX_SUMMARY_LENGTH, MIN_SUMMARY_LENGTH

class Summarizer:
    def __init__(self, model_name):
        """Initialize summarizer with a specific model."""
        self.model_name = model_name
        self.pipeline = pipeline('summarization', model=model_name, device=-1)

    def generate_summary(self, text):
        """Generate summary for the given text."""
        try:
            # Truncate text to avoid sequence length errors
            truncated_text = truncate_text(text, MAX_INPUT_LENGTH)
            
            # Add warning if text was truncated
            if len(text.split()) > MAX_INPUT_LENGTH:
                print(f"Warning: Text was truncated from {len(text.split())} to {MAX_INPUT_LENGTH} words")
            
            summary = self.pipeline(
                truncated_text,
                max_length=MAX_SUMMARY_LENGTH,
                min_length=MIN_SUMMARY_LENGTH,
                do_sample=False,
                truncation=True  # Enable truncation in the model
            )
            return summary[0]['summary_text']
        except Exception as e:
            print(f"Error generating summary with {self.model_name}: {str(e)}")
            return "Error generating summary" 
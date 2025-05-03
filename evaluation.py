from evaluate import load
from utils import format_rouge_scores
from config import METRICS

class Evaluator:
    def __init__(self):
        """Initialize evaluator with ROUGE metric."""
        self.rouge = load('rouge')

    def evaluate_summary(self, reference, candidate):
        """Evaluate summary using ROUGE metrics."""
        try:
            result = self.rouge.compute(predictions=[candidate], references=[reference])
            # Convert numpy values to Python floats
            return {k: float(v) for k, v in result.items()}
        except Exception as e:
            print(f"Error evaluating summary: {str(e)}")
            return {metric: 0.0 for metric in METRICS}

    def calculate_average_scores(self, results):
        """Calculate average ROUGE scores across all articles."""
        avg_scores = {}
        for metric in METRICS:
            scores = [float(r['scores'][metric]) for r in results]
            avg_scores[metric] = sum(scores) / len(scores)
        return format_rouge_scores(avg_scores) 
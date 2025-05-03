import datasets
import json
import pandas as pd
from config import (
    DATASET_NAME, DATASET_VERSION, NUM_SAMPLES,
    MODELS, OUTPUT_DIR
)
from models import Summarizer
from evaluation import Evaluator
from utils import ensure_dir, get_timestamp

def main():
    # Create output directory
    ensure_dir(OUTPUT_DIR)

    # Load dataset
    dataset = datasets.load_dataset(
        DATASET_NAME,
        DATASET_VERSION,
        split=f'train[:{NUM_SAMPLES}]'
    )

    # Initialize evaluator
    evaluator = Evaluator()

    # Process articles
    results = []
    for i, article in enumerate(dataset):
        print(f"\nArticle {i+1}:")
        print(f"Original: {article['article'][:200]}...")
        print("\nSummaries:")

        article_results = {
            "article_id": i + 1,
            "original": article['article'],
            "reference": article['highlights'],
            "summaries": {}
        }

        # Generate summaries for each model
        for model_name in MODELS:
            print(f"\nModel: {model_name}")
            summarizer = Summarizer(model_name)
            summary = summarizer.generate_summary(article['article'])
            print(f"Summary: {summary}")

            # Evaluate summary
            scores = evaluator.evaluate_summary(article['highlights'], summary)
            print(f"ROUGE Scores: {scores}")

            article_results["summaries"][model_name] = {
                "summary": summary,
                "scores": scores
            }

        results.append(article_results)
        print("-" * 80)

    # Create performance comparison table
    performance_data = []
    for model in MODELS:
        model_scores = {
            "Model": model,
            **evaluator.calculate_average_scores([
                r["summaries"][model] for r in results
            ])
        }
        performance_data.append(model_scores)

    # Display performance comparison
    df = pd.DataFrame(performance_data)
    print("\nPerformance Comparison:")
    print(df.to_string(index=False))

    # Save results
    timestamp = get_timestamp()
    results_file = f"{OUTPUT_DIR}/summarization_results_{timestamp}.json"
    with open(results_file, 'w', encoding='utf-8') as f:
        json.dump(results, f, indent=2, ensure_ascii=False)

    print(f"\nResults saved to {results_file}")

if __name__ == "__main__":
    main()
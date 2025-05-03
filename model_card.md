---
language: en
license: mit
library_name: transformers
tags:
- summarization
- text-generation
- t5
- bart
datasets:
- cnn_dailymail
metrics:
- rouge
---

# Text Summarization Benchmark

This repository contains a benchmark comparison of different text summarization models:
- google/flan-t5-small
- t5-small
- sshleifer/distilbart-cnn-12-6

## Model Description

This project evaluates the performance of lightweight summarization models on the CNN/DailyMail dataset. The models are specifically chosen to work on low-resource environments (CPU-only with 8GB RAM).

### Model Details

- **Developed by:** [Your Name/Organization]
- **Model type:** Text Summarization
- **Language:** English
- **License:** MIT
- **Finetuned from model:** Multiple base models

## Performance

The models are evaluated using ROUGE metrics (ROUGE-1, ROUGE-2, ROUGE-L) on the CNN/DailyMail test set.

## Usage

```python
from transformers import pipeline

# Example usage for each model
summarizer = pipeline("summarization", model="google/flan-t5-small")
# or
summarizer = pipeline("summarization", model="t5-small")
# or
summarizer = pipeline("summarization", model="sshleifer/distilbart-cnn-12-6")

text = "Your long text here..."
summary = summarizer(text, max_length=150, min_length=30, do_sample=False)
```

## Training and Evaluation Data

The models are evaluated on the CNN/DailyMail dataset, which consists of news articles and their corresponding summaries.

## Limitations

- The models are optimized for CPU usage and may not achieve the same performance as larger models
- Maximum input length is limited to 512 tokens
- Batch size is limited to 4 for memory efficiency

## Citation

If you use this benchmark in your research, please cite:

```bibtex
@misc{text-summarization-benchmark,
  author = {[Your Name]},
  title = {Text Summarization Benchmark},
  year = {2024},
  publisher = {Hugging Face},
  journal = {Hugging Face Hub},
  howpublished = {\url{https://huggingface.co/[your-username]/text-summarization-benchmark}}
}
``` 
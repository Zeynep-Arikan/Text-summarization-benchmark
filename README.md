---
title: Text Summarization Benchmark
emoji: 📝
colorFrom: blue
colorTo: purple
sdk: gradio
sdk_version: 4.19.2
app_file: app.py
pinned: false
---

# Text Summarization Benchmark

This project benchmarks lightweight summarization models using the `cnn_dailymail` dataset. It is designed to work on a low-resource CPU-only machine with 8GB RAM.

## Models Used
- `google/flan-t5-small`
- `t5-small`
- `sshleifer/distilbart-cnn-12-6`

## Features
- Interactive text summarization interface
- Multiple model support
- ROUGE score evaluation
- CPU-optimized for low-resource environments

## Usage
1. Enter your text in the input box
2. Select a model from the dropdown menu
3. Click "Generate Summary" to get the result
4. View the generated summary and ROUGE scores

## Configuration
The project uses the following configuration:
- Maximum input length: 512 tokens
- Maximum summary length: 150 tokens
- Batch size: 4
- Evaluation metrics: ROUGE-1, ROUGE-2, ROUGE-L

## Technical Details
- Built with Gradio for the web interface
- Uses Hugging Face Transformers library
- Evaluated on CNN/DailyMail dataset
- Optimized for CPU usage

## License
MIT License

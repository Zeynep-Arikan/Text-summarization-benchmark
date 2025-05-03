import gradio as gr
from models import Summarizer
from evaluation import Evaluator
from config import MODELS, MAX_INPUT_LENGTH
from utils import truncate_text

# Initialize models and evaluator
summarizers = {model: Summarizer(model) for model in MODELS}
evaluator = Evaluator()

def process_text(text, model_name):
    """Process text and generate summary with selected model."""
    if not text.strip():
        return "Please enter some text.", {}
    
    # Generate summary
    summary = summarizers[model_name].generate_summary(text)
    
    # Evaluate summary
    scores = evaluator.evaluate_summary(text, summary)
    
    # Format scores for display
    formatted_scores = "\n".join([f"{metric}: {score:.2f}%" for metric, score in scores.items()])
    
    return summary, formatted_scores

# Create Gradio interface
with gr.Blocks(title="Text Summarization and Evaluation Tool") as demo:
    gr.Markdown("""
    # Text Summarization and Evaluation Tool
    
    This tool summarizes your input text using different models and evaluates them with ROUGE metrics.
    """)
    
    with gr.Row():
        with gr.Column():
            # Input components
            text_input = gr.Textbox(
                label="Text",
                placeholder="Enter the text you want to summarize here...",
                lines=10
            )
            model_dropdown = gr.Dropdown(
                choices=MODELS,
                value=MODELS[0],
                label="Select Model"
            )
            process_btn = gr.Button("Summarize and Evaluate")
        
        with gr.Column():
            # Output components
            summary_output = gr.Textbox(
                label="Generated Summary",
                lines=5
            )
            scores_output = gr.Textbox(
                label="ROUGE Scores",
                lines=4
            )
    
    # Set up event handling
    process_btn.click(
        fn=process_text,
        inputs=[text_input, model_dropdown],
        outputs=[summary_output, scores_output]
    )
    
    # Add examples
    gr.Examples(
        examples=[
            ["LONDON, England (Reuters) -- Harry Potter star Daniel Radcliffe gains access to a reported £20 million ($41.1 million) fortune as he turns 18 on Monday, but he insists the money won't cast a spell on him. Daniel Radcliffe as Harry Potter in 'Harry Potter and the Order of the Phoenix' To the disappointment of gossip columnists around the world, the young actor says he has no plans to fritter his cash away on fast cars, drink and celebrity parties.", "google/flan-t5-small"],
            ["The ninth floor of the Miami-Dade pretrial detention facility is dubbed the 'forgotten floor.' Here, inmates with the most severe mental illnesses are incarcerated until they're ready to appear in court. Most often, they face drug charges or charges of assaulting an officer --charges that Judge Steven Leifman says are usually 'avoidable felonies.'", "t5-small"]
        ],
        inputs=[text_input, model_dropdown]
    )

if __name__ == "__main__":
    demo.launch() 
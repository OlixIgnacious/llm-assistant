import os
import sys

# Add project src directory to Python path
CURRENT_DIR = os.path.dirname(__file__)
PROJECT_ROOT = os.path.abspath(os.path.join(CURRENT_DIR, ".."))
SRC_DIR = os.path.join(PROJECT_ROOT, "src")
if SRC_DIR not in sys.path:
    sys.path.insert(0, SRC_DIR)

import gradio as gr
from chain import run_analysis_chain


def analyze(question, model, output_mode):
    return run_analysis_chain(context="", question=question, output_mode=output_mode)



with gr.Blocks() as demo:
    gr.Markdown("# AnalystGPT")
    with gr.Row():
        with gr.Column(scale=1):
            gr.Markdown("## Settings")
            model_dd = gr.Dropdown(
                choices = ["gpt-4o-mini", "gpt-4o"],
                value = "gpt-4o-mini",
                label = "Model",
                interactive=True,
            )

            output_mode_dd = gr.Dropdown(
                choices = ["text", "json"],
                value="text",
                label="Output Mode",
                interactive=True,
            )
        with gr.Column(scale=2):
            query_tb = gr.Textbox(
                label="Question",
                placeholder="Enter your question here",
                lines=4,
                interactive=True,
            )

            run_btn = gr.Button("Run")

            answer_tb = gr.Textbox(
                label="Answer",
                placeholder="The answer will appear here",
                lines=10,
                interactive=False,
            )
    
    run_btn.click(
        fn =analyze,
        inputs = [query_tb, model_dd, output_mode_dd],
        outputs = [answer_tb],
    )
if __name__ == "__main__":
    demo.launch(share=True)
from prompts import render_analysis_prompt, SYSTEM_PROMPT, BEHAVIOR_PROMPT
from models import call_completion

def run_analysis_chain(context: str, question: str, output_mode: str = "text") -> str:
    prompt = render_analysis_prompt(context, question)
    full_prompt = f"{SYSTEM_PROMPT}\n{BEHAVIOR_PROMPT}\n\n{prompt}\n\nOutput mode: {output_mode}"
    response = call_completion(full_prompt, temperature=0.0)
    return response
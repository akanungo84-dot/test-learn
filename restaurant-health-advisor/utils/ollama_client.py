import ollama

DEFAULT_MODEL='qwen3:14b'

def ask_llm(prompt, model=DEFAULT_MODEL):
    response = ollama.chat(model=model, messages=[{'role':'user','content':prompt}])
    return response['message']['content']

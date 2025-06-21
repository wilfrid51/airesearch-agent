import requests

def summarize_with_llm(text):
    prompt = f"Summarize the following text in 5-7 sentences:\n\n{text}"
    response = requests.post(
        "http://localhost:11434/api/generate",
        json={"model": "llama3", "prompt": prompt, "stream": False}
    )
    summary = response.json().get('response', '')
    return summary if summary.strip() else "No summary available."

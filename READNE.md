# AI Research & Summarizer Agent

## What it does
- Enter a research question.
- The agent uses Google Search (via SerpAPI) to find and summarize relevant information.
- It saves the summary in Notepad (Windows) or TextEdit (Mac).

## Quick Start

1. **Install [Ollama](https://ollama.com/download)** and run `ollama pull llama3`.
2. **Install Python dependencies:**
`pip install -r requirements.txt`
3. **Get your [SerpAPI API key](https://serpapi.com/) (free tier available).**
- Set it as an environment variable:
  ```
  export SERPAPI_KEY=your_actual_key_here
  ```
- Or put it in `agent/tools_browser.py` for testing (less secure).
4. **Run Ollama server in a terminal:**
`ollama serve`
5. **Run the app:**
`streamlit run frontend/app.py`
6. **Enjoy it!**
- Enter a question (e.g., "What is Llama 3 and why is it important?")
- Click "Run Research"
- Wait for desktop automation. The summary will appear in Notepad/TextEdit and in your browser.

## Notes

- The agent writes to whichever window is in focus. Don't use your keyboard/mouse while it types!
- For advanced usage, you can improve link filtering, content extraction, and error handling.
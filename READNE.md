# AI Research & Summarizer Agent

## What it does
- Takes your research question
- Searches the web and scrapes content
- Summarizes with an open-source LLM (Llama 3 via Ollama)
- Writes the summary into Notepad (or TextEdit on Mac)

## Setup
1. Install [Ollama](https://ollama.com/download) and run `ollama pull llama3`
2. Install Python dependencies: `pip install -r requirements.txt`
3. Download ChromeDriver for Selenium
4. Run the app: `streamlit run frontend/app.py`

## Demo
- ![Demo GIF or link to video]

## Notes
- Desktop automation writes into Notepad/TextEdit. Make sure it's open in focus!
- No payment, no credentials required.

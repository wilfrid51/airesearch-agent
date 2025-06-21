from .tools_browser import google_search, scrape_page, serpapi_search
from .tools_llm import summarize_with_llm
from .tools_desktop import write_to_notepad

def run_research_and_summarize(query):
    links = serpapi_search(query, num_results=3)
    content = []
    for url in links:
        page_text = scrape_page(url)
        content.append(page_text)
    all_text = "\n\n".join(content)
    summary = summarize_with_llm(all_text)
    write_to_notepad(summary)
    return summary, links

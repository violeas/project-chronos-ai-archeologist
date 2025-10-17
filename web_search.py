def search_context(keywords, num_results=3):
    """
    Simulates web search. Replace this with Google Custom Search or SerpAPI later.
    """
    urls = []
    for i in range(num_results):
        urls.append(f"https://example.com/search?q={keywords.replace(' ', '+')}&result={i+1}")
    return urls

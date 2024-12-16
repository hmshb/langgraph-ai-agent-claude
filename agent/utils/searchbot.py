from langchain_community.tools.tavily_search import TavilySearchResults

searchbot = TavilySearchResults(max_results=2, include_answer=True)
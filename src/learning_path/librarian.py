from agno.agent import Agent
from agno.models.groq import Groq
from agno.tools.serpapi import SerpApiTools
from agno.utils.pprint import pprint_run_response

def get_learning_resources(topic: str, groq_api_key: str, serpapi_key: str) -> str:
    """
    Find learning resources for the given topic using the Research Librarian agent.
    
    Args:
        topic (str): The topic to find resources for
        groq_api_key (str): The GROQ API key
        serpapi_key (str): The SerpAPI key
        
    Returns:
        str: The found learning resources
    """
    research_librarian_agent = Agent(
        name="Research Librarian",
        role="Learning Resource Specialist",
        model=Groq(id="deepseek-r1-distill-llama-70b", api_key=groq_api_key),
        tools=[
            SerpApiTools(api_key=serpapi_key)
        ],
        instructions=[
            "Find high-quality learning resources for provided topic across the web",
            "Use SerpApi to find relevant resources and provide their direct URL to access it",
            "use SerpApi to find Github Links, Medium Blogs, Youtube Videos and playlists, etc.",
            "Keep the output concise and limit it to approximately 4000 tokens to avoid rate limits",
            "Focus on the most relevant and high-quality resources",
            "Limit the number of resources to the most essential ones"
        ],
        markdown=True, 
    )
    
    response = research_librarian_agent.run(
        f"the topic is: {topic}",
        stream=False
    )
    
    return response.content 
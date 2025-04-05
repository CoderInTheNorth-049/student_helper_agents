from agno.agent import Agent
from agno.models.groq import Groq
from agno.tools.serpapi import SerpApiTools
from agno.utils.pprint import pprint_run_response

def get_prerequisites(topic: str, groq_api_key: str, serpapi_key: str) -> str:
    """
    Find prerequisites for the given topic using the Prerequisite agent.
    
    Args:
        topic (str): The topic to find prerequisites for
        groq_api_key (str): The GROQ API key
        serpapi_key (str): The SerpAPI key
        
    Returns:
        str: The found prerequisites
    """
    prerequisite_agent = Agent(
        name="Prerequisite Agent",
        role="Researcher",
        model=Groq(id="deepseek-r1-distill-llama-70b", api_key=groq_api_key),
        tools=[
            SerpApiTools(api_key=serpapi_key)
        ],
        markdown=True,
        instructions=[
            "Find the prerequisites of a given topic in field of research which are present in the research papers",
            "List down the topics that are required to understand before researching on given topic",
            "Provide links to the sources where user can learn about the prerequisites. It can be article, youtube videos.",
            "Provide direct URLs to accessible resources",
            "Keep the output concise and limit it to approximately 4000 tokens to avoid rate limits",
            "Focus on the most essential prerequisites",
            "Limit the number of prerequisites to the most important ones"
        ],
    )
    
    response = prerequisite_agent.run(
        f"the topic is: {topic}",
        stream=False
    )
    
    return response.content 
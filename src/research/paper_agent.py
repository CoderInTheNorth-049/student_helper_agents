from agno.agent import Agent
from agno.models.groq import Groq
from agno.tools.serpapi import SerpApiTools
from agno.utils.pprint import pprint_run_response

def get_research_papers(topic: str, groq_api_key: str, serpapi_key: str) -> str:
    """
    Find research papers for the given topic using the Research Paper agent.
    
    Args:
        topic (str): The topic to find papers for
        groq_api_key (str): The GROQ API key
        serpapi_key (str): The SerpAPI key
        
    Returns:
        str: The found research papers
    """
    research_paper_agent = Agent(
        name="Research Paper Agent",
        role="Researcher",
        model=Groq(id="deepseek-r1-distill-llama-70b", api_key=groq_api_key),
        tools=[
            SerpApiTools(api_key=serpapi_key)
        ],
        markdown=True,
        instructions=[
            "Provide relevant Research Papers on a given topics. max 8 papers",
            "Provide direct URLs to accessible Research Papers and Articles where user don't need to pay for access",
            """Sci-Hub - sci-hub.se
ResearchGate - researchgate.net
Academia.edu - academia.edu
arXiv - arxiv.org
Springer Open - springeropen.com
bioRxiv & medRxiv - biorxiv.org | medrxiv.org
PhilPapers+ - philpapers.org
PsyArXiv - psyarxiv.com
SciELO (Scientific Electronic Library Online) - scielo.org
WorldWideScience - worldwidescience.org
Research4Life - research4life.org
Cambridge Open Engage - cambridge.org/engage
Wiley Open Access - wileyopenaccess.com
""",
            "Keep the output concise and limit it to approximately 4000 tokens to avoid rate limits",
            "Focus on the most recent and highly cited papers",
            "Limit the number of papers to the most essential ones"
        ],
    )
    
    response = research_paper_agent.run(
        f"the topic is: {topic}",
        stream=False
    )
    
    return response.content 
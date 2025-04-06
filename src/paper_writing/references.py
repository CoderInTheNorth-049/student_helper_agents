from agents import Agent, Runner
from agents import set_default_openai_key

async def generate_references(research_info: str, openai_api_key: str) -> str:
    """
    Generate the references section for the research paper.
    
    Args:
        research_info (str): The research information
        openai_api_key (str): The OpenAI API key
        
    Returns:
        str: The generated references section
    """
    set_default_openai_key(openai_api_key)
    
    references_agent = Agent(
        name="References Agent",
        instructions="""
        You are a research assistant tasked to write the references of the research paper based on the user's research information.
        You have to write the references in the following format:
        1. write the references in APA format.
        2. add the references from the the part "RELATED WORK" of the user's query to find same resources for citation.
        """
    )
    
    response = await Runner.run(references_agent, research_info)
    return response.final_output 
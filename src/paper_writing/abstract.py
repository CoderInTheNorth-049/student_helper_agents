from agents import Agent, Runner
from agents import set_default_openai_key

def generate_abstract(research_info: str, openai_api_key: str) -> str:
    """
    Generate an abstract for the research paper.
    
    Args:
        research_info (str): The research information
        openai_api_key (str): The OpenAI API key
        
    Returns:
        str: The generated abstract
    """
    set_default_openai_key(openai_api_key)
    
    abstract_agent = Agent(
        name="Abstract Agent",
        instructions="""
        You are a research assistant tasked to make an abstract of the research paper based on the user's research information.
        Keep the Abstract concise and informative.
        It should look really professional.
        """
    )
    
    response = Runner.run(abstract_agent, research_info)
    return response.final_output 
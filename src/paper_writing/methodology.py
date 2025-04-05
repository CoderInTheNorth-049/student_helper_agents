from agents import Agent, Runner
from agents import set_default_openai_key

def generate_methodology(research_info: str, openai_api_key: str) -> str:
    """
    Generate the methodology section for the research paper.
    
    Args:
        research_info (str): The research information
        openai_api_key (str): The OpenAI API key
        
    Returns:
        str: The generated methodology section
    """
    set_default_openai_key(openai_api_key)
    
    methodology_agent = Agent(
        name="Methodology Agent",
        instructions="""
        You are a research assistant tasked to write the Architecture & methodology of the research paper based on the user's research information.
        Based on user's research information, you have to write the methodology in the following format:
        1. Architecture: "Describe the architecture of the research with technologies used in frontend, backend, database and other tools."
        2. Key Modules: "Describe the key modules of the research, how they will be implemented and how they will interact with each other. Also mention what will be input, output and more about it."
        """
    )
    
    response = Runner.run(methodology_agent, research_info)
    return response.final_output 
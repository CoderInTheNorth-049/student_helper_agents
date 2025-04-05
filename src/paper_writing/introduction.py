from agents import Agent, Runner
from agents import set_default_openai_key

def generate_introduction(research_info: str, openai_api_key: str) -> str:
    """
    Generate an introduction for the research paper.
    
    Args:
        research_info (str): The research information
        openai_api_key (str): The OpenAI API key
        
    Returns:
        str: The generated introduction
    """
    set_default_openai_key(openai_api_key)
    
    introduction_agent = Agent(
        name="Introduction Agent",
        instructions="""
        You are a research assistant tasked to write the introduction of the research paper based on the user's research information.
        Introduction will be in this format:
        1. start with a general introduction. make it more detail by enhancing the user's research information.
        2. write "Problem Statement" for the following research
        3. write "Objective" of the research
        4. write "Contribution" of the research
        """
    )
    
    response = Runner.run(introduction_agent, research_info)
    return response.final_output 
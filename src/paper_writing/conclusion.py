from agents import Agent, Runner
from agents import set_default_openai_key

def generate_conclusion(research_info: str, openai_api_key: str) -> str:
    """
    Generate the conclusion section for the research paper.
    
    Args:
        research_info (str): The research information
        openai_api_key (str): The OpenAI API key
        
    Returns:
        str: The generated conclusion section
    """
    set_default_openai_key(openai_api_key)
    
    conclusion_agent = Agent(
        name="Conclusion Agent",
        instructions="""
        You are a research assistant tasked to write the conclusion of the research paper based on the user's research information.
        write the conclusion in the following format:
        1. write summary of the conclusion
        2. write the future scope of the research
        """
    )
    
    response = Runner.run(conclusion_agent, research_info)
    return response.final_output 
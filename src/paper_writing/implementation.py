from agents import Agent, Runner
from agents import set_default_openai_key

async def generate_implementation(research_info: str, openai_api_key: str) -> str:
    """
    Generate the implementation and evaluation section for the research paper.
    
    Args:
        research_info (str): The research information
        openai_api_key (str): The OpenAI API key
        
    Returns:
        str: The generated implementation and evaluation section
    """
    set_default_openai_key(openai_api_key)
    
    implementation_evaluation_agent = Agent(
        name="Implementation & Evaluation Agent",
        instructions="""
        You are a research assistant tasked to write the Implementation & Evaluation of the research paper based on the user's research information.
        You have to write the Implementation & Evaluation in the following format:
        1. Teachnolgies used: "Mention the technologies used in the research and why they are used."
        2. Comparative Analysis: "Compare the research with other researches in the domain and mention the pros and cons of the research."
        3. Evaluation: "Evaluate the research based on the results and findings. Mention the results and how they are obtained."
        4. case studies: "Mention the case studies if user mentioned any and how they are implemented."
        """
    )
    
    response = await Runner.run(implementation_evaluation_agent, research_info)
    return response.final_output 
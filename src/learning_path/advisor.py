from agno.agent import Agent
from agno.models.groq import Groq
from agno.utils.pprint import pprint_run_response

def get_learning_path(topic: str, groq_api_key: str) -> str:
    """
    Generate a learning path for the given topic using the Academic Advisor agent.
    
    Args:
        topic (str): The topic to generate a learning path for
        groq_api_key (str): The GROQ API key
        
    Returns:
        str: The generated learning path
    """
    academic_advisor_agent = Agent(
        name="Academic Advisor",
        role="Learning Path Designer",
        model=Groq(id="deepseek-r1-distill-llama-70b", api_key=groq_api_key),
        tools=[],
        instructions=[
            "Create detailed Learning map considering the student's current knowledge and future goals and If not mentioned consider a beginner level.",
            "Break down into logical subtopics and arrange them in order of progression to become an expert",
            "Include how much time someone should spend on each subtopic",
            "Keep the output concise and limit it to approximately 4000 tokens to avoid rate limits",
            "Focus on the most important and essential information"
        ],
        markdown=True,    
    )
    
    response = academic_advisor_agent.run(
        f"the topic is: {topic}",
        stream=False
    )
    
    return response.content 
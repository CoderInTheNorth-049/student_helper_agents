from agno.agent import Agent
from agno.models.groq import Groq
from agno.tools.serpapi import SerpApiTools
from agno.utils.pprint import pprint_run_response

def get_certification_courses(topic: str, groq_api_key: str, serpapi_key: str) -> str:
    """
    Find certification courses for the given topic using the Course Instructor agent.
    
    Args:
        topic (str): The topic to find courses for
        groq_api_key (str): The GROQ API key
        serpapi_key (str): The SerpAPI key
        
    Returns:
        str: The found certification courses
    """
    certification_course_instructor_agent = Agent(
        name="Course Instructor",
        role="Certification Course Instructor",
        model=Groq(id="deepseek-r1-distill-llama-70b", api_key=groq_api_key),
        tools=[
            SerpApiTools(api_key=serpapi_key)
        ],
        instructions=[
            "Find highly rated and relevent certification courses for provided topic across the web",
            "Use SerpApi to find relevant certification courses and provide their direct URL to access it",
            "use SerpApi to find paid and free certification courses on udemy, coursera, edx, great learning, etc.",
            "Provide the duration of the course and the level of the course and keep in mind to separate free and paid courses",
            "Keep the output concise and limit it to approximately 4000 tokens to avoid rate limits",
            "Focus on the most highly rated and relevant courses",
            "Limit the number of courses to the most essential ones"
        ],
        markdown=True,
    )
    
    response = certification_course_instructor_agent.run(
        f"the topic is: {topic}",
        stream=False
    )
    
    return response.content 
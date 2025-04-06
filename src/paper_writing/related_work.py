from agents import Agent, Runner
from agents import set_default_openai_key
from agents.tool import function_tool
from firecrawl import FirecrawlApp

@function_tool
async def deep_research(query: str, max_depth: int, time_limit: int, max_urls: int, firecrawl_api_key: str) -> dict:
    """
    Perform comprehensive web research using FireCrawl's deep research endpoint.
    
    Args:
        query (str): The research query
        max_depth (int): Maximum depth for research
        time_limit (int): Time limit for research
        max_urls (int): Maximum number of URLs to process
        firecrawl_api_key (str): The Firecrawl API key
        
    Returns:
        dict: Research results
    """
    try:
        firecrawl_app = FirecrawlApp(api_key=firecrawl_api_key)
        
        params = {
            "maxDepth": max_depth,
            "timeLimit": time_limit,
            "maxUrls": max_urls,
        }
        
        results = firecrawl_app.deep_research(
            query=query,
            params=params
        )
        
        return {
            "success": True,
            "final_analysis": results['data']['finalAnalysis'],
            "sources_count": len(results['data']['sources']),
            "sources": results['data']['sources']
        }
        
    except Exception as e:
        return {"error": str(e), "success": False}

async def generate_related_work(research_info: str, openai_api_key: str, firecrawl_api_key: str) -> str:
    """
    Generate the related work section for the research paper.
    
    Args:
        research_info (str): The research information
        openai_api_key (str): The OpenAI API key
        firecrawl_api_key (str): The Firecrawl API key
        
    Returns:
        str: The generated related work section
    """
    set_default_openai_key(openai_api_key)
    
    related_work_agent = Agent(
        name="Related Work Agent",
        instructions="""
        You are a research assistant tasked to write the related work of the research paper based on the user's research information.
        You have to write the related work in the following format:
        1. Traditional Methods: "Talk about Traditional Methods used in that topic of research their pros and cons"
        2. Recent Methods: "Talk about recent methods getting adapted by the world in that domain e.g. How Paid and Open Source tools are helping in that domain"
        Note: while writing the related work, make sure to keep it informative and concise and divide them in meaningful parts with headings like for eg:
           a. Traditional LMS Limitations
           b. AI in Education
           c. Open Source vs Proprietary AI Tools
        
        While writing the related work you'll need to refer various resources as articles, research papers, and blogs.
        1. Use the deep_research tool to get the resources.
          - Always use these parameters:
          * max_depth: 3 (for moderate depth)
          * time_limit: 240 (4 minutes)
          * max_urls: 15 (sufficient resources to add in reference of research paper)
        2. while writing the related work, make sure to add references to the resources you have used along with the URLs to resources for proper citation.
        3. Review the resources and write the related work in a professional manner.
        """,
        tools=[deep_research]
    )
    
    response = await Runner.run(related_work_agent, research_info)
    return response.final_output 
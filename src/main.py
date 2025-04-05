import streamlit as st
from config.settings import initialize_session_state
from learning_path.advisor import get_learning_path
from learning_path.librarian import get_learning_resources
from learning_path.instructor import get_certification_courses
from research.paper_agent import get_research_papers
from research.prerequisite_agent import get_prerequisites
from paper_writing.abstract import generate_abstract
from paper_writing.introduction import generate_introduction
from paper_writing.related_work import generate_related_work
from paper_writing.methodology import generate_methodology
from paper_writing.implementation import generate_implementation
from paper_writing.conclusion import generate_conclusion
from paper_writing.references import generate_references
from utils.text_processor import clean_llm_output, markdown_to_docx

st.set_page_config(
    page_title="Student Helper Agent",
    page_icon=":brain:",
    layout="wide"
)

def render_sidebar():
    with st.sidebar:
        st.title("Student Helper Agent")
        
        # Mode selection
        mode = st.selectbox(
            "Select Mode",
            ["Learning Path", "Research Papers", "Craft Research Paper"]
        )
        
        # API Keys based on mode
        if mode in ["Learning Path", "Research Papers"]:
            st.subheader("API Configuration")
            groq_key = st.text_input("GROQ API Key", type="password")
            serpapi_key = st.text_input("SerpAPI Key", type="password")
            return mode, groq_key, serpapi_key, None, None
            
        else:  # Craft Research Paper
            st.subheader("API Configuration")
            openai_key = st.text_input("OpenAI API Key", type="password")
            firecrawl_key = st.text_input("Firecrawl API Key", type="password")
            return mode, None, None, openai_key, firecrawl_key

def add_download_buttons(content: str, filename: str):
    """Add download buttons for different document formats."""
    col1, col2 = st.columns(2)
    
    # with col1:
    #     st.download_button(
    #         "Download as PDF",
    #         markdown_to_pdf(content),
    #         file_name=f"{filename}.pdf",
    #         mime="application/pdf"
    #     )
    
    with col2:
        st.download_button(
            "Download as DOCX",
            markdown_to_docx(content),
            file_name=f"{filename}.docx",
            mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
        )

def main():
    # Initialize session state
    initialize_session_state()
    
    # Render sidebar and get configuration
    mode, groq_key, serpapi_key, openai_key, firecrawl_key = render_sidebar()
    
    # Main content area
    st.title("Student Helper Agent")
    
    # Input area
    user_input = st.text_input(
        "Enter your topic or research query:",
        placeholder="e.g., Machine Learning, Quantum Computing, etc."
    )
    
    if st.button("Generate"):
        if not user_input:
            st.error("Please enter a topic or query.")
            return
            
        try:
            if mode == "Learning Path":
                with st.spinner("Generating Learning Path..."):
                    learning_path = clean_llm_output(get_learning_path(user_input, groq_key))
                    st.markdown("### Learning Path")
                    st.markdown(learning_path)
                    
                with st.spinner("Finding Learning Resources..."):
                    resources = clean_llm_output(get_learning_resources(user_input, groq_key, serpapi_key))
                    st.markdown("### Learning Resources")
                    st.markdown(resources)
                    
                with st.spinner("Finding Certification Courses..."):
                    courses = clean_llm_output(get_certification_courses(user_input, groq_key, serpapi_key))
                    st.markdown("### Certification Courses")
                    st.markdown(courses)
                    
                # Combine all content for download
                complete_content = f"""
                # Learning Path: {user_input}
                
                ## Learning Path
                {learning_path}
                
                ## Learning Resources
                {resources}
                
                ## Certification Courses
                {courses}
                """
                
                add_download_buttons(complete_content, f"learning_path")
                    
            elif mode == "Research Papers":
                with st.spinner("Finding Research Papers..."):
                    papers = clean_llm_output(get_research_papers(user_input, groq_key, serpapi_key))
                    st.markdown("### Research Papers")
                    st.markdown(papers)
                    
                with st.spinner("Finding Prerequisites..."):
                    prereqs = clean_llm_output(get_prerequisites(user_input, groq_key, serpapi_key))
                    st.markdown("### Prerequisites")
                    st.markdown(prereqs)
                    
                # Combine all content for download
                complete_content = f"""
                # Research Papers: {user_input}
                
                ## Research Papers
                {papers}
                
                ## Prerequisites
                {prereqs}
                """
                
                add_download_buttons(complete_content, f"research_papers")
                    
            else:  # Craft Research Paper
                with st.spinner("Generating Research Paper..."):
                    # Generate each section
                    abstract = clean_llm_output(generate_abstract(user_input, openai_key))
                    st.markdown("### Abstract")
                    st.markdown(abstract)
                    
                    introduction = clean_llm_output(generate_introduction(user_input, openai_key))
                    st.markdown("### Introduction")
                    st.markdown(introduction)
                    
                    related_work = clean_llm_output(generate_related_work(user_input, openai_key, firecrawl_key))
                    st.markdown("### Related Work")
                    st.markdown(related_work)
                    
                    methodology = clean_llm_output(generate_methodology(user_input, openai_key))
                    st.markdown("### Methodology")
                    st.markdown(methodology)
                    
                    implementation = clean_llm_output(generate_implementation(user_input, openai_key))
                    st.markdown("### Implementation & Evaluation")
                    st.markdown(implementation)
                    
                    conclusion = clean_llm_output(generate_conclusion(user_input, openai_key))
                    st.markdown("### Conclusion")
                    st.markdown(conclusion)
                    
                    references = clean_llm_output(generate_references(user_input, openai_key))
                    st.markdown("### References")
                    st.markdown(references)
                    
                    # Combine all content for download
                    complete_paper = f"""
                    # Research Paper: {user_input}
                    
                    ## Abstract
                    {abstract}
                    
                    ## Introduction
                    {introduction}
                    
                    ## Related Work
                    {related_work}
                    
                    ## Methodology
                    {methodology}
                    
                    ## Implementation & Evaluation
                    {implementation}
                    
                    ## Conclusion
                    {conclusion}
                    
                    ## References
                    {references}
                    """
                    
                    add_download_buttons(complete_paper, f"research_paper")
                    
        except Exception as e:
            st.error(f"An error occurred: {str(e)}")
            st.info("Please check your API keys and try again.")

if __name__ == "__main__":
    main() 
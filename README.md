# Student Helper Agent

A comprehensive Streamlit application that helps students with learning paths, research papers, and academic writing. The application combines multiple AI agents to provide a seamless experience for students.

## Features

1. **Learning Path Generation**
   - Creates detailed learning maps for any topic
   - Provides time estimates for each subtopic
   - Suggests learning resources and certification courses

2. **Research Paper Assistant**
   - Finds relevant research papers on any topic
   - Identifies prerequisites and learning resources
   - Provides direct links to accessible papers

3. **Research Paper Writing**
   - Generates complete research papers
   - Includes all standard sections (Abstract, Introduction, Related Work, etc.)
   - Provides proper citations and references

## Setup

1. Clone the repository:
```bash
git clone https://github.com/yourusername/student-helper-agent.git
cd student-helper-agent
```

2. Create a virtual environment and activate it:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run the application:
```bash
streamlit run src/main.py
```

## API Keys Required

The application requires the following API keys:

1. For Learning Path and Research Papers:
   - GROQ API Key
   - SerpAPI Key

2. For Research Paper Writing:
   - OpenAI API Key
   - Firecrawl API Key

## Usage

1. Launch the application using the command above
2. Select your desired mode from the sidebar
3. Enter the required API keys
4. Input your topic or research query
5. Click "Generate" to get results

## Project Structure

```
student-helper-agent/
├── src/
│   ├── main.py              # Main Streamlit application
│   ├── config/              # Configuration settings
│   ├── learning_path/       # Learning path generation modules
│   ├── research/           # Research paper finding modules
│   └── paper_writing/      # Research paper writing modules
├── requirements.txt        # Project dependencies
└── README.md              # Project documentation
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details. 
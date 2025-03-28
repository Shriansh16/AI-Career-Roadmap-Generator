# Career Roadmap Generator 🚀

**A multi-AI agent powered application that analyzes resumes and generates personalized career roadmaps to help users achieve their professional goals.**

This tool bridges the gap between current qualifications and dream careers using cutting-edge AI technologies.

## Key Features

### 🔍 Resume Analysis
- Extracts and structures information from PDF resumes
- Identifies current skills with proficiency levels
- Maps work experience and education background

### 🎯 Career Goal Analysis
- Understands requirements for target roles
- Identifies core competencies and secondary skills
- Maps industry expectations and certification paths

### 📚 Smart Resource Finder
- Discovers the best and most recent learning resources
- Prioritizes up-to-date materials (last 2 years)
- Includes free/paid courses with direct links
- Recommends industry-recognized certifications

### 🗺️ Personalized Roadmap Generation
- Creates clear, actionable career progression plans
- Develops a 3-phase plan:
  - 0-3 month immediate actions
  - 3-6 month intermediate goals
  - 6-12 month advanced targets
- Outputs professional markdown formatting

## Technical Architecture

```mermaid
graph TD
    A[Streamlit UI] --> B[PDF Parser]
    B --> C[Resume Analyzer Agent]
    A --> D[Career Goal Input]
    D --> E[Career Path Analyst Agent]
    C --> F[Skill Gap Analysis]
    E --> F
    F --> G[Resource Finder Agent]
    G --> H[Roadmap Generator Agent]
    H --> I[Markdown Output]

## How It Works

The application uses a sophisticated multi-agent AI system:

### Resume Analysis Expert
- Extracts structured information from resumes  
- Identifies current skills and experience  
- Outputs standardized JSON format for processing  

### Career Path Analyst
- Determines requirements for the target role  
- Identifies skill gaps between current and desired state  
- Maps industry-standard certification paths  

### Learning Resource Specialist
- Finds up-to-date learning resources (prioritizing last 2 years)  
- Verifies links and resource availability  
- Prioritizes high-quality materials from reputable sources  
- Includes both free and paid options with direct links  

### Career Roadmap Designer
- Synthesizes information from all other agents  
- Creates clear, phased action plan with:  
  - 0-3 month immediate actions  
  - 3-6 month intermediate goals  
  - 6-12 month advanced targets  
- Formats professional output in markdown  

## Technologies Used

### Core Technologies
- **Python**: Primary programming language  
- **Streamlit**: Web application framework  
- **PyPDF2**: PDF text extraction  
- **OpenAI GPT-4**: AI language model  
- **LangChain**: LLM integration framework  

### AI/ML Stack
- **CrewAI**: For multi-agent orchestration  
- **SerperDev**: For web search capabilities  
- **Custom Prompt Engineering**: For precise task execution  


## How to Run

Follow these steps to set up and run the application:

1. **Create a virtual environment** (Python 3.12 recommended)
2. Activate the environment
3. Install dependencies:
  ```bash
  pip install -r requirements.txt

4. Run the application:
  ```bash
  streamlit run app.py

5. Access the application:

The app will automatically open in your default browser                                                             

If not, navigate to http://localhost:8501
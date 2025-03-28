import PyPDF2
from crewai import Agent, Task, Crew, Process
import streamlit as st
from langchain_openai import ChatOpenAI
#from dotenv import load_dotenv
import os
from datetime import datetime
from crewai_tools import SerperDevTool

# Load environment variables
#load_dotenv()
llm = ChatOpenAI(
    model="gpt-4o-mini",  
    openai_api_key=st.secrets["OPENAI_API_KEY"]
)
SERPER_API_KEY = st.secrets["SERPER_API_KEY"]
os.environ['SERPER_API_KEY'] = SERPER_API_KEY
# PDF text extraction function
def input_pdf_text(uploaded_file):
    reader = PyPDF2.PdfReader(uploaded_file)
    text = ""
    for page in range(len(reader.pages)):
        page = reader.pages[page]
        text += str(page.extract_text())
    return text

# Set up the UI
st.title("Career Roadmap Generator")

with st.form("roadmap_form"):
    goal = st.text_area("Enter your career goal", 
                       placeholder="e.g., 'Become a Data Scientist' or 'Transition to AI Engineer'")
    uploaded_file = st.file_uploader("Upload Your Resume (PDF)", 
                                   type="pdf", 
                                   help="Please upload your resume in PDF format")
    submit = st.form_submit_button("Generate Roadmap")

if submit and uploaded_file is not None and goal.strip():
    with st.spinner("Analyzing your resume and creating roadmap..."):
        # Extract text from PDF
        resume_text = input_pdf_text(uploaded_file)
        
        # Define Agents
        profile_analyzer = Agent(
            role="Resume Analysis Expert",
            goal="Extract and structure information from resumes",
            backstory="You are an expert at analyzing resumes and professional profiles.",
            verbose=True,
            llm=llm,
            allow_delegation=False
        )
        
        career_target_analyzer = Agent(
            role="Career Path Analyst",
            goal="Identify requirements for target roles",
            backstory="You deeply understand career paths and role requirements across industries.",
            verbose=True,
            llm=llm,
            allow_delegation=False
        )
        
        resource_finder = Agent(
            role="Learning Resource Specialist",
            goal="Find the best and most recent learning resources for skill development from the web.",
            backstory="""You specialize in finding the most up-to-date, high-quality learning resources from reputable sources.
            You verify links and prioritize resources that are currently available and actively maintained.""",
            verbose=True,
            llm=llm,
            tools=[SerperDevTool()],
            allow_delegation=False
        )
        
        roadmap_writer = Agent(
            role="Career Roadmap Designer",
            goal="Create clear, actionable career progression plans",
            backstory="You are a professional career coach known for creating clear, actionable roadmaps.",
            verbose=True,
            llm=llm,
            allow_delegation=False
        )
        
        # Define Tasks
        analyze_resume_task = Task(
            description=f"Analyze this resume:\n{resume_text}",
            agent=profile_analyzer,
            expected_output="A JSON structure containing: current skills with proficiency levels, work experience (roles, duration), education background, and existing certifications."
        )
        
        analyze_requirements_task = Task(
         description=f"""Analyze requirements for: {goal}
         Consider the candidate's current profile that is given in the context.
         """,
         agent=career_target_analyzer,
         expected_output="A JSON structure containing: core competencies (must-have skills), secondary skills (nice-to-have), typical certification paths, and industry expectations.",
         context=[analyze_resume_task] 
         )
        current_year = datetime.now().year
        find_resources_task = Task(
          description=f"""Find the best and most recent online courses, certifications, and learning resources to bridge the skill gaps for becoming a {goal}.  
          Current year is {current_year} - prioritize resources from the last 2 years.  
          Use the **requirements analysis** and **candidate's current profile** provided in the context to ensure relevance.
           Focus on:  
           - Free/paid courses (include direct links)  
           - Industry-recognized certifications  
           - Books, blogs, and practice projects  
           Prioritize resources that are highly rated and relevant to {goal}.
           Verify all links are working and resources are currently available""",
          agent=resource_finder,
          expected_output="A JSON structure of resources including: free/paid online courses (with links), recommended certifications (with links), books/blogs, and practice projects.",
          context=[analyze_requirements_task, analyze_resume_task]
          )
        
        create_roadmap_task = Task(
         description=f"""
         Transform skill gaps and resources into a step-by-step career progression plan for transitioning to {goal}.
         Use only the given context and information to create a roadmap.
         The roadmap should clearly describe:
         - How the individual's **current skills** contribute to the transition.
         - The **skills they need to learn** and their relevance to the goal.
         - Recommended Resources.
          A structured **3-phase plan** for skill acquisition and career transition.
          Include:
             - 0-3 month immediate actions
             - 3-6 month intermediate goals
             - 6-12 month advanced targets
         Format as a markdown document directly (no code block markers).
         Only return your final work without additional comments.""",
         agent=roadmap_writer,
         expected_output="A well-formatted markdown document with the career roadmap, ready for display.",
         context=[find_resources_task, analyze_requirements_task, analyze_resume_task]
            )
        
        # Create Crew
        crew = Crew(
            agents=[profile_analyzer, career_target_analyzer, resource_finder, roadmap_writer],
            tasks=[analyze_resume_task, analyze_requirements_task, find_resources_task, create_roadmap_task],
            verbose=True,
            process=Process.sequential  # Tasks will be executed in order
        )
        
        # Execute tasks
        result = crew.kickoff()
        # Display results
        st.markdown(result)
# Career Roadmap Generator 🚀

**An AI-powered application that analyzes resumes and generates personalized career roadmaps to help users achieve their professional goals.**

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
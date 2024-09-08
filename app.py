import streamlit as st
import openai
import os
import PyPDF2 as pdf
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configure OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")

def get_openai_response(prompt):
    response = openai.Completion.create(
        model="gpt-3.5-turbo",
        prompt=prompt,
        max_tokens=1500,  # Adjust this based on your needs
        temperature=0.7   # Adjust this based on your needs
    )
    return response.choices[0].text.strip()

def input_pdf_text(uploaded_file):
    reader = pdf.PdfReader(uploaded_file)
    text = ""
    for page in reader.pages:
        text += page.extract_text() or ""
    return text

# Prompt Template
def create_prompt(resume_text, job_description):
    return f"""
    Act like a skilled ATS (Applicant Tracking System) with a deep understanding of tech fields such as software engineering, data science, data analysis, and big data engineering. Your task is to evaluate the resume based on the given job description. You must consider that the job market is very competitive, and you should provide the best assistance for improving the resume. Assign a percentage match based on the job description and list the missing keywords with high accuracy.

    resume: {resume_text}
    description: {job_description}

    I want the response in one single string having the structure
    {{ "JD Match": "%", "MissingKeywords": [], "Profile Summary": "" }}
    """

# Streamlit app
st.title("Smart ATS")
st.text("Improve Your Resume ATS")
jd = st.text_area("Paste the Job Description")
uploaded_file = st.file_uploader("Upload Your Resume", type="pdf", help="Please upload the PDF")

submit = st.button("Submit")

if submit:
    if uploaded_file is not None:
        resume_text = input_pdf_text(uploaded_file)
        prompt = create_prompt(resume_text, jd)
        response = get_openai_response(prompt)
        st.subheader(response)

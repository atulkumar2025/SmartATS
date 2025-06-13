import streamlit as st
from utils.file_handler import extract_text_from_pdf, extract_text_from_docx
from utils.text_cleaner import clean_text
from utils.matcher import compute_match_score
from utils.analyzer import get_openai_feedback
import openai

from dotenv import load_dotenv
import os
load_dotenv()  # Load variables from .env

openai.api_key = os.getenv("OPENAI_API_KEY")

st.title("SmartATS (An AI-Powered Tool)")

resume_file = st.file_uploader("Upload Resume (PDF/DOCX)", type=["pdf", "docx"])
jd_text = st.text_area("Paste Job Description")

if resume_file and jd_text:
    if resume_file.name.endswith(".pdf"):
        resume_text = extract_text_from_pdf(resume_file)
    else:
        resume_text = extract_text_from_docx(resume_file)

    clean_resume = clean_text(resume_text)
    clean_jd = clean_text(jd_text)

    score = compute_match_score(clean_resume, clean_jd)
    st.subheader(f"Matching Score: {score} %")

    with st.spinner("Analyzing with AI..."):
        feedback = get_openai_feedback(resume_text, jd_text)
        st.subheader("AI Feedback")
        st.markdown(feedback)

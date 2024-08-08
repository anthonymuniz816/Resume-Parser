import os
import re
import spacy
import docx2txt
from pdfminer.high_level import extract_text

# Load the SpaCy model
nlp = spacy.load("en_core_web_sm")

# Function to extract text from a PDF
def extract_text_from_pdf(pdf_path):
    return extract_text(pdf_path)

# Function to extract text from a DOCX file
def extract_text_from_docx(docx_path):
    return docx2txt.process(docx_path)

# Function to extract text based on file type
def extract_text_from_file(file_path):
    if file_path.lower().endswith('.pdf'):
        return extract_text_from_pdf(file_path)
    elif file_path.lower().endswith('.docx'):
        return extract_text_from_docx(file_path)
    else:
        raise ValueError("Unsupported file type")

# Function to extract information from text
def extract_information(text):
    doc = nlp(text)
    info = {
        "name": "",
        "email": "",
        "phone": "",
        "university": "",
        "degree": "",
        "skills": []
    }

    # Extract university
    university_match = re.search(r'(?i)university of [^\n]+', text)
    if university_match:
        info["university"] = university_match.group(0)
    
    # Extract email
    email_match = re.search(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', text)
    if email_match:
        info["email"] = email_match.group(0)
    
    # Extract phone number
    phone_match = re.search(r'\b\d{3}[-.]\d{3}[-.]\d{4}\b|\b\d{10}\b|\(\d{3}\)\d{3}-\d{4}', text)
    if phone_match:
        info["phone"] = phone_match.group(0)
    
    # Extract degree
    #degree_match = re.search(r'(?i)B.S [^\n]+ | B.A [^\n]+ | Bachelor of Science [^\n]+ | Bachelor of Arts [^\n]+', text)
    degree_match = re.search(r'(?i)B.S .* | B.A [^\n]+ | Bachelor of Science [^\n]+ | Bachelor of Arts [^\n]+', text)
    if degree_match:
        info["degree"]= degree_match.group(0)

    # Extract skills (Assuming a predefined list of skills)
    predefined_skills = ["Python", "Java", "C", "C++", "Javascript", "html", "CSS", "Machine Learning", "Data Science", "AWS", "Azure", "Cloud","SQL"]
    for token in doc:
        if token.text in predefined_skills:
            info["skills"].append(token.text)
    
    # Extract name (Assuming the first proper noun is the name)
    for ent in doc.ents:
        if ent.label_ == "PERSON":
            info["name"] = ent.text
            break
    
    return info

# Main function to parse resume
def parse_resume(file_path):
    text = extract_text_from_file(file_path)
    info = extract_information(text)
    return info

# Example usage
if __name__ == "__main__":
    file_path = "Anthony-Muniz-Internship-Resume.pdf"
    parsed_info = parse_resume(file_path)
    print(parsed_info)

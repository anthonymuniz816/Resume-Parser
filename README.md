# Resume Parser with Flask

This project is a web application that allows users to upload their resumes in PDF or DOCX format, parses the resumes to extract key information using Natural Language Processing (NLP) with SpaCy, and displays the extracted information.

![parsed_resume_example](https://github.com/user-attachments/assets/404ba008-6963-4e03-a010-c06c8f7fdb0c)

## Table of Contents

- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)

## Features

- Upload resumes in PDF or DOCX format.
- Parse resumes to extract key information like name, email, phone, university, degree, and skills.
- Display the extracted information on a web page.

## Prerequisites

- Python 3.8+
- pip (Python package installer)

## Installation

1. **Clone the repository:**

    ```sh
    git clone https://github.com/your-username/resume-parser.git
    cd resume-parser
    ```

2. **Create and activate a virtual environment:**

    ```sh
    python3 -m venv resume_parser_env
    source resume_parser_env/bin/activate
    ```

3. **Install the required packages:**

    ```sh
    pip install -r requirements.txt
    python3 -m spacy download en_core_web_sm
    ```

4. **Run the application locally:**

    ```sh
    export FLASK_APP=app.py
    flask run
    ```

5. **Open your browser and go to:**

    ```
    http://127.0.0.1:5000/
    ```

## Usage

1. **Upload a resume:**

    Go to the upload page, choose a resume file (PDF or DOCX), and click the "Upload" button.

2. **View parsed information:**

    After uploading, the application will parse the resume and display the extracted information on a new page.




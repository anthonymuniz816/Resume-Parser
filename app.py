from flask import Flask, request, render_template
import os
from resume_parser import parse_resume  # Ensure this import matches your resume parser file

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/')
def upload_resume():
    return render_template('upload.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        if file:
            file_path = os.path.join(UPLOAD_FOLDER, file.filename)
            file.save(file_path)
            parsed_info = parse_resume(file_path)
            return render_template('result.html', info=parsed_info)

if __name__ == "__main__":
    app.run(debug=True)

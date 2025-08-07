import os
from flask import Flask, render_template, request, jsonify, send_file
from werkzeug.utils import secure_filename
from main import extract_text_from_file, extract_keywords_from_jd, analyze_resumes

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

jd_filename = ""
keywords_selected = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload_jd', methods=['POST'])
def upload_jd():
    global jd_filename
    jd_file = request.files['jd_file']
    jd_filename = secure_filename(jd_file.filename)
    jd_path = os.path.join(app.config['UPLOAD_FOLDER'], jd_filename)
    jd_file.save(jd_path)

    jd_text = extract_text_from_file(jd_path)
    keywords = extract_keywords_from_jd(jd_text)
    return jsonify({'filename': jd_filename, 'keywords': sorted(keywords)})

@app.route('/submit_keywords', methods=['POST'])
def submit_keywords():
    global keywords_selected
    keywords_selected = request.json.get('keywords', [])
    return jsonify({'message': 'Keywords received', 'keywords': keywords_selected})

@app.route('/analyze', methods=['POST'])
def analyze():
    if not keywords_selected:
        return jsonify({'error': 'No keywords selected'}), 400

    resumes = request.files.getlist('resume_files')
    top_n = int(request.form.get('top_n', 5))
    jd_path = os.path.join(app.config['UPLOAD_FOLDER'], jd_filename)

    resume_paths = []
    for resume in resumes:
        filename = secure_filename(resume.filename)
        path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        resume.save(path)
        resume_paths.append(path)

    output_excel, top_results = analyze_resumes(jd_path, resume_paths, keywords_selected, top_n)

    results = []
    for res in top_results:
        results.append({
            'Rank': res['Rank'],
            'Resume': res['Resume'],
            'Skill Match %': res['Skill Match %'],
            'JD Match %': res['JD Match %']
        })

    return jsonify({'results': results, 'excel_file': output_excel})

@app.route('/download', methods=['GET'])
def download():
    file_path = request.args.get('file')
    if os.path.exists(file_path):
        return send_file(file_path, as_attachment=True)
    return "File not found", 404

if __name__ == '__main__':
    if not os.path.exists(UPLOAD_FOLDER):
        os.makedirs(UPLOAD_FOLDER)
    app.run(debug=True)

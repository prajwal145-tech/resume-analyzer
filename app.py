import os
import shutil
from flask import Flask, render_template, request, send_from_directory, session
from werkzeug.utils import secure_filename
from main import extract_text_from_file, extract_keywords_from_jd, analyze_resumes

app = Flask(__name__)
app.secret_key = 'your_secret_key'
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)


def cleanup_uploads():
    # Clean uploaded files before new upload
    for filename in os.listdir(UPLOAD_FOLDER):
        file_path = os.path.join(UPLOAD_FOLDER, filename)
        if os.path.isfile(file_path):
            os.remove(file_path)


@app.route('/', methods=['GET', 'POST'])
def index():
    jd_filename = session.get('jd_filename')
    extracted_keywords = session.get('extracted_keywords', [])
    selected_keywords = session.get('selected_keywords', [])
    uploaded_resumes = session.get('uploaded_resumes', [])
    results_table = None
    excel_download = None

    if request.method == 'POST':
        action = request.form.get('action')

        # Step 1: Upload JD and extract keywords
        if action == 'upload_jd':
            cleanup_uploads()
            jd_file = request.files.get('jd_file')
            if jd_file:
                jd_filename = secure_filename(jd_file.filename)
                jd_path = os.path.join(UPLOAD_FOLDER, jd_filename)
                jd_file.save(jd_path)

                jd_text = extract_text_from_file(jd_path)
                keywords = extract_keywords_from_jd(jd_text)
                session['jd_text'] = jd_text
                session['jd_filename'] = jd_filename
                session['extracted_keywords'] = keywords
                session['selected_keywords'] = []  # Clear old keywords
                session['uploaded_resumes'] = []
        
        # Step 2: Submit selected and manual keywords
        elif action == 'submit_keywords':
            selected = request.form.getlist('selected_keywords')
            manual = request.form.get('manual_keywords', '')
            manual_keywords = [k.strip() for k in manual.split(',') if k.strip()]
            all_keywords = sorted(set(selected + manual_keywords))
            session['selected_keywords'] = all_keywords

        # Step 3: Upload resumes and analyze
        elif action == 'analyze':
            top_n = int(request.form.get('top_n', 0))
            resume_files = request.files.getlist('resumes')

            resume_paths = []
            for file in resume_files:
                filename = secure_filename(file.filename)
                file_path = os.path.join(UPLOAD_FOLDER, filename)
                file.save(file_path)
                resume_paths.append(file_path)

            session['uploaded_resumes'] = [os.path.basename(p) for p in resume_paths]

            jd_text = session.get('jd_text', '')
            selected_keywords = session.get('selected_keywords', [])

            if jd_text and selected_keywords and resume_paths:
                df, excel_path = analyze_resumes(jd_text, resume_paths, selected_keywords, top_n)
                results_table = df.to_html(classes='result-table', index=False)
                excel_download = f"/download/{os.path.basename(excel_path)}"
                session['last_excel'] = os.path.basename(excel_path)

    return render_template(
        'index.html',
        jd_filename=jd_filename,
        extracted_keywords=extracted_keywords,
        selected_keywords=selected_keywords,
        uploaded_resumes=uploaded_resumes,
        results_table=results_table,
        excel_download=excel_download
    )


@app.route('/download/<filename>')
def download_file(filename):
    return send_from_directory(UPLOAD_FOLDER, filename, as_attachment=True)


if __name__ == '__main__':
    app.run(debug=True)

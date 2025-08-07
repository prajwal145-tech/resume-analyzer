**AI Resume Analyzer**
Intelligent Resume Matching with AI-Powered Skill Analysis
A sophisticated web application that uses machine learning and natural language processing to analyze and rank resumes against job descriptions. Built with Flask, scikit-learn, and Sentence Transformers for accurate candidate matching.
✨ Features

🤖 AI-Powered Matching: Uses Sentence Transformers and TF-IDF for semantic similarity analysis
🔍 Smart Keyword Extraction: Automatically extracts relevant keywords from job descriptions using spaCy NLP
🎨 Modern UI: Clean, responsive interface with interactive keyword selection and loading animations
📁 Multiple File Formats: Supports PDF, DOCX, and TXT files for both job descriptions and resumes
📊 Excel Reports: Generates detailed analysis reports with conditional formatting and rankings
⚡ Real-time Analysis: Fast processing with visual feedback and progress indicators
📈 Dual Scoring System: Calculates both skill-specific and overall JD match percentages
🏆 Smart Ranking: Automatically ranks candidates based on combined relevance scores

🎯 Use Cases

👔 HR Professionals: Quickly screen large volumes of resumes with data-driven insights
🎯 Recruiters: Identify best-fit candidates efficiently and reduce time-to-hire
👨‍💼 Hiring Managers: Get objective, AI-powered candidate rankings for informed decisions
👨‍🎓 Job Seekers: Understand how well their resume matches specific job requirements
🏢 Recruitment Agencies: Scale resume screening process with consistent, unbiased results

🚀 Quick Start
⚠️ System Requirements

Python Version: 3.8, 3.9, 3.10, or 3.11 (Python 3.12+ is not currently supported)
Operating System: Windows, macOS, or Linux
RAM: Minimum 4GB (8GB recommended for better performance)
Disk Space: At least 2GB free space for dependencies

📋 Prerequisites

Check Python Version
Open PowerShell (Windows) or Terminal (Mac/Linux) and run:
bash python --version
If you don't have Python or have version 3.12+, download Python 3.11 from python.org
Verify pip installation
bash pip --version


🔧 Installation Steps

Clone the repository
bash  git clone https://github.com/prajwal145-tech/resume-analyzer.git
cd resume-analyzer

Create a virtual environment (Recommended)
Windows (PowerShell):
bash  python -m venv venv
venv\Scripts\activate
Mac/Linux:
bash  python -m venv venv
source venv/bin/activate

Install required packages
bash  pip install flask pandas docx2txt PyMuPDF openpyxl scikit-learn sentence-transformers spacy werkzeug

Download spaCy English model
bash  python -m spacy download en_core_web_sm

Create uploads directory
bash  mkdir uploads

Run the application
bash  python app.py

Access the application
Open your web browser and go to:

http://localhost:5000 or
http://127.0.0.1:5000



🎉 Success Indicators
You should see output similar to:
* Running on http://127.0.0.1:5000
* Debug mode: on
📖 How to Use
Step 1: Upload Job Description 📄

Click "Choose File" and select your job description (PDF, DOCX, or TXT)
Click "Extract Keywords" - the AI will automatically identify relevant skills and requirements
Wait for the loading animation to complete

Step 2: Select Keywords 🎯

Review the AI-extracted keywords displayed in the interactive grid
Click on keywords to select/deselect them (selected keywords turn blue)
Add custom keywords using the text input field if needed
Click "Confirm Keywords" when satisfied with your selection

Step 3: Upload Resumes 📋

Click "Choose Files" and select multiple resume files
Set the number of top candidates you want to highlight (default: 5)
Click "Analyze Now 🔍" and wait for the analysis to complete

Step 4: Review Results 📊

View the ranked results table with match percentages
Download the detailed Excel report for further analysis
Results include:

Rank: Overall ranking based on combined scores
Resume: Filename of the candidate's resume
Skill Match %: Percentage of selected keywords found in the resume
JD Match %: Semantic similarity between resume and job description



🛠️ Technical Details
🏗️ Architecture

Backend: Flask (Python web framework)
ML/NLP Engine:

Sentence Transformers (all-MiniLM-L6-v2 model) for semantic analysis
spaCy (Natural Language Processing) for keyword extraction
scikit-learn (TF-IDF, Cosine Similarity) for text analysis


File Processing:

PyMuPDF for PDF text extraction
docx2txt for Word document processing


Data Processing: pandas for data manipulation, openpyxl for Excel generation
Frontend: Bootstrap 5 with vanilla JavaScript for responsive UI

🧮 Algorithm Workflow

Text Extraction: Converts PDFs, Word docs, and text files to clean text
Keyword Extraction: Uses spaCy NLP to identify relevant nouns, proper nouns, and adjectives
Vectorization: Converts documents to numerical vectors using Sentence Transformers
Similarity Analysis: Computes cosine similarity between job description and resume vectors
Skill Matching: Performs direct keyword matching for specific skills
Scoring & Ranking: Combines similarity scores to create final candidate rankings

⚠️ Important Notes
🐍 Python Version Compatibility

Supported: Python 3.8, 3.9, 3.10, 3.11
Not Supported: Python 3.12+ (due to dependency compatibility issues)
Recommended: Python 3.11 for optimal performance

🔒 Security Considerations

Files are temporarily stored in the uploads/ directory
Clean up uploaded files periodically in production environments
Consider implementing file size limits for production use

📊 Performance Tips

For large batches (50+ resumes), expect 2-5 minutes processing time
The first run may be slower due to model loading
Use SSD storage for better I/O performance

🐛 Troubleshooting
Common Issues and Solutions
1. ModuleNotFoundError
bash # Solution: Install missing packages
pip install [missing-package-name]
2. spaCy model not found
bash # Solution: Download the English model
python -m spacy download en_core_web_sm
3. Python version issues
bash # Check your Python version
python --version
# If you have Python 3.12+, install Python 3.11
4. Port already in use
bash # Error: Address already in use
# Solution: Use a different port
Edit app.py and change:
pythonapp.run(debug=True, port=5001)  # Use port 5001 instead of 5000
5. Permission errors on Windows
bash # Solution: Run PowerShell as Administrator or use Command Prompt
6. Virtual environment issues
bash # Deactivate and recreate virtual environment
deactivate
rm -rf venv  # or rmdir /s venv on Windows
python -m venv venv
# Then reactivate and reinstall packages
🆘 Getting Help
If you encounter issues:

Check the Issues section
Create a new issue with:

Your Python version
Operating system
Full error message
Steps to reproduce



🤝 Contributing
We welcome contributions! Here's how to get started:

Fork the repository
Create a feature branch
bash git checkout -b feature/your-feature-name

Make your changes
Test thoroughly
Commit your changes
bash git commit -am 'Add: your feature description'

Push to your branch
bash git push origin feature/your-feature-name

Create a Pull Request

🎯 Contribution Ideas

Add support for more file formats
Improve keyword extraction algorithms
Enhance UI/UX with more interactive features
Add batch processing capabilities
Implement user authentication
Add API endpoints for integration

📄 License
This project is licensed under the MIT License - see the LICENSE file for details.
👨‍💻 Author
Prajwal - GitHub Profile
🙏 Acknowledgments

Sentence Transformers for semantic similarity analysis
spaCy for natural language processing
Bootstrap for responsive UI components
Flask for the web framework
Community contributors for feedback and improvements

⭐ Star this repository if you find it helpful!
GitHub will auto-generate URLs you can use in your README

⭐ Star this repository if you find it helpful!


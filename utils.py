import os
from fpdf import FPDF
from PyPDF2 import PdfReader
from datetime import datetime
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

# Configure the generative AI model with API key
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
model = genai.GenerativeModel('models/gemini-1.5-flash')

# Function to get AI response based on input and prompt
def SendRequest(input_text, pdf_content, prompt):
    response = model.generate_content([input_text, pdf_content, prompt])
    return response.text

# Function to extract text from a PDF file
def ExtractPDF(file):
    pdf = PdfReader(file)
    text = ""
    for page in pdf.pages:
        text += page.extract_text() + "\n"
    return text

# Function to create a optimize resume PDF
def CreatePDF(text, input_filename):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_auto_page_break(auto=True, margin=10)
    pdf.set_margins(left=10, top=10, right=10)
    pdf.set_font("Arial", size=10)
    
    for line in text.split('\n'):
        pdf.multi_cell(0, 10, line.encode('latin-1', 'replace').decode('latin-1'), align='L')

    # Generate the timestamped filename with formate ddmmyyyyhhmmss
    timestamp = datetime.now().strftime("%d%m%Y-%H%M%S")
    file_name = f"{input_filename}_Optimized_{timestamp}.pdf"
    pdf.output(file_name, 'F')
    return file_name if os.path.exists(file_name) else None
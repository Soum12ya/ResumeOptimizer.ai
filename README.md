# ResumePerfector.ai

   ## About The Project

   **ResumeOptimizer.ai** is an GENAI-powered platform designed to optimize resumes for applicant tracking systems (ATS). By leveraging the **Google Gemini LLM Model**, the system enhances the likelihood of your resume passing through ATS filters and matching specific job descriptions.

   ### 𝗙𝗲𝗮𝘁𝘂𝗿𝗲𝘀:
   - 💡 𝗝𝗼𝗯 𝗗𝗲𝘀𝗰𝗿𝗶𝗽𝘁𝗶𝗼𝗻 𝗜𝗻𝘀𝗶𝗴𝗵𝘁𝘀: Tailor your resume to match the job description perfectly!
   - 🤖 𝗔𝗧𝗦 𝗖𝗼𝗺𝗽𝗮𝘁𝗶𝗯𝗶𝗹𝗶𝘁𝘆 𝗖𝗵𝗲𝗰𝗸: Ensure your resume passes ATS filters with ease!
   - 📊 𝗦𝗸𝗶𝗹𝗹𝘀 𝗚𝗮𝗽 𝗔𝗻𝗮𝗹𝘆𝘀𝗶𝘀: Identify missing skills compared to the job requirements.
   - ✅ 𝗥𝗲𝘀𝘂𝗺𝗲 𝗙𝗲𝗲𝗱𝗯𝗮𝗰𝗸: Get actionable tips for improvement.
   - 🎯 𝗥𝗲𝘀𝘂𝗺𝗲 𝗠𝗮𝘁𝗰𝗵 %: See how closely your resume fits the JD.
   - 📄 𝗔𝘂𝘁𝗼𝗺𝗮𝘁𝗲𝗱 𝗖𝗼𝘃𝗲𝗿 𝗟𝗲𝘁𝘁𝗲𝗿𝘀: Generate a personalized cover letter instantly.
   - ⚡ 𝗚𝗲𝗻𝗲𝗿𝗮𝘁𝗲 𝗢𝗽𝘁𝗶𝗺𝗶𝘇𝗲𝗱 𝗥𝗲𝘀𝘂𝗺𝗲: Craft an optimized resume that stands out!

   ## Screenshot
   <img width="960" alt="ResumeOptimizer ai" src="https://github.com/user-attachments/assets/fd280c35-0d15-4b81-9e5f-cb57987e6b5d" />

   ## Key Technologies:

   - **Google Gemini LLM Model**: Advanced AI for analyzing resumes and job descriptions.
   - **pdf2image**: Converts PDF resumes into image formats for preprocessing.
   - **fpdf**: Generates PDF documents programmatically for enhanced resume creation.
   - **PyPDF2**: Extracts, merges, and manipulates PDF content efficiently.
   
   ## Use Cases:

   - **Resume Optimization**: Tailors resumes to pass Applicant Tracking System (ATS) filters.
   - **Job Description Analysis**: Analyzes job postings to provide actionable feedback for resume refinement.
   - **PDF Manipulation**: Simplifies resume uploads and adjustments by enabling seamless PDF processing.

   ### Prerequisites

   Before getting started, make sure you have the following:

   **GOOGLE GEMINI API Key**: You’ll need an API key for interaction with the Google Gemini LLM.

   ### Getting Started

   To get started with this project locally, you’ll need Python 3.10+ installed on your machine along with the necessary Python packages. You can either clone the repository and install dependencies manually or use Docker for an isolated environment.

   ## Installation Steps

   1. **Clone the repository**:
      - Open your terminal or command prompt.
      - Navigate to the directory where you want to install the project.
      - Run the following command to clone the GitHub repository:
      ```bash
      git clone https://github.com/Soum12ya/ResumeOptimizer.ai.git
      ```

   2. **Create a Virtual Environment (Optional)**:
      - It's recommended to use a virtual environment to manage dependencies. Run the following command:
      ```bash
      conda create -p <Environment_Name> python==<python version> -y
      ```

   3. **Activate the Virtual Environment (Optional)**:
      - Activate the virtual environment based on your operating system:
      ```bash
      conda activate <Environment_Name>/
      ```

   4. **Install Dependencies**:
      - Navigate to the project directory:
      ```bash
      cd [project_directory]
      ```
      - Run the following command to install project dependencies:
      ```bash
      pip install -r requirements.txt
      ```

   5. **Create `.env` file and add your API keys**:
      - Create a `.env` file in the root directory and add your Google Gemini API key for LLM interaction.

   6. **Run the Project**:
      - To start the application, run the following command:
      ```bash
      streamlit run app.py
      ```

   7. **Access the Project**:
      - Visit `http://localhost:8501` in your browser to use the app.

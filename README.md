# Medical Report Analyzer



Medical Report Analyzer is a simple AI-ready backend that processes medical reports by extracting text from PDFs, Word documents, plain text, or converting images to base64 for later analysis. It stores all processed data in a single JSON file (`data.json`) for easy retrieval and integration with an AI model or frontend app.



---



## ✨ Features



### Core Processing Tools



- 📄 \*\*Upload Files:\*\* Supports `.pdf`, `.docx`, `.txt`, and common image formats.

- 🧠 \*\*Text Extraction:\*\* Automatically extract readable text from PDF and Word documents.

- 🖼️ \*\*Image Handling:\*\* Convert uploaded images to Base64-encoded PNG data.

- 💾 \*\*Single JSON Store:\*\* All processed content saved to one `data.json` file.



### AI-Ready Design



- 🔌 \*\*Simple API:\*\* Easy to connect to any AI model for generating insights.

- 📂 \*\*Unified Storage:\*\* All uploads and processed outputs in a single local file for portability.



---



## 🛠 Tech Stack



| Layer     | Tech                                                        |
| --------- | ----------------------------------------------------------- |
| Backend   | Python, Flask, Flask-CORS, OpenAI API (optional), PyMuPDF, Pillow |
| Storage   | Local JSON (`data.json`)                                    |



---



## 🚀 Local Setup Guide (All-in-One)



Follow these steps to clone, set up, and run the backend locally.



### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/medical-report-analyzer.git

cd medical-report-analyzer
```

### 2. Create Virtual Environment \& Install Dependencies

```bash
# Windows
python -m venv venv

venv\Scripts\activate

# macOS/Linux
python3 -m venv venv

source venv/bin/activate

# Install requirements
pip install -r requirements.txt
```
### 3. Set Environment Variables

```bash
# Create a .env file in the root folder
OPENAI\_API\_KEY=sk-your-api-key
```
### 4. Run the Backend

```bash
python backend/app.py
```

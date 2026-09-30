# 🧠 Minutes.AI — Automated Meeting Transcription & Action-Oriented Summarization

### 📌 Objective
**Minutes.AI** is an intelligent Flask-based application that **transcribes meeting audio** and automatically generates **structured, action-oriented summaries** using **Whisper** for transcription and **Google Gemini** for summarization.  

It helps teams save time by turning spoken discussions into clear summaries, decisions, and actionable next steps.

---

### ⚙️ Scope of Work
- **Input:** Meeting audio files (`.wav`, `.mp3`, etc.)
- **Output:**  
  - Accurate **text transcript**  
  - Detailed **meeting summary**  
  - Clearly defined **action items**
- **Frontend:**  
  A simple Flask web interface to upload audio and view results.

---

### 🧩 System Architecture
1. **Frontend:**  
   - HTML/CSS interface (`/templates`, `/static`) for file upload and result display.  
   - Allows users to upload an audio file and view transcript and summary instantly.

2. **Backend:**  
   - Built with **Flask**.  
   - Handles file uploads and temporary storage.  
   - Uses **Whisper (medium model)** for ASR transcription.  
   - Integrates **Google Gemini API** for summarization and extraction of key decisions and actions.  
   - Cleans up temporary files after processing to maintain efficiency.

3. **LLM Integration:**  
   - Custom prompt for structured summarization in JSON format:
     > Summarize the transcript, list key decisions, and action items (who, what).

4. **Evaluation Metrics:**  
   - **WER (Word Error Rate)** — transcription accuracy  
   
---

### 📊 Evaluation Metrics
| Type of Meeting | Description | WER ↓ | 
|------------------|--------------|-------|------------|
| Podcast-like (single speaker, clear audio) | Minimal noise and consistent tone | **3.6%** |
| Two-person conversational (with background hindrance) | Dialogue with overlapping speech and mild interference | **3%** |

---

### 🧪 Technical Stack
- **Backend:** Python (Flask)  
- **Frontend:** HTML, CSS (under `/templates` and `/static`)  
- **ASR Model:** OpenAI **Whisper (medium)**  
- **LLM Model:** **Google Gemini-Pro** for summarization  
- **Audio Processing:** Pydub (for splitting long audio)  
- **Environment Management:** `venv`  
- **Evaluation Libraries:** `jiwer` (WER), `rouge-score` (ROUGE-L)

---

### 📁 Folder Structure

minutes.ai/

├── app.py

├── requirements.txt

├── .env

├── venv/

├── static/

│ └── style.css

└── templates/

└── index.html

---

### 🚀 Setup & Execution

#### **1. Clone the Repository**
```bash
git clone https://github.com/drishti3001/minutes.ai.git

cd minutes.ai

python -m venv venv

# Activate it:
venv\Scripts\activate       # for Windows
source venv/bin/activate    # for Mac/Linux

pip install -r requirements.txt

# set up your API in .env folder
GOOGLE_API_KEY=your_gemini_api_key

#in terminal run the app.py
python app.py

Once started, visit the app at:
👉 http://127.0.0.1:5000

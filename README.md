# 🧠 Smart Document Analyzer using NLP and Vision

## 📌 Project Overview
Smart Document Analyzer is a Flask-based AI application that extracts, analyzes, and summarizes information from documents such as PDFs and scanned images. It combines the power of NLP and computer vision to provide insights and enable question-answering from uploaded documents.

---

## 🚀 Features
- 📄 Upload and process scanned documents or PDFs
- 🔍 Optical Character Recognition (OCR) using Tesseract or EasyOCR
- 🧾 Named Entity Recognition (NER) to extract people, places, dates, and more
- ✂️ Text Summarization to condense long documents
- 🤖 Question Answering using Transformer-based models
- 🗂️ Document classification (e.g., invoice, resume, etc.)

---

## 🛠️ Tech Stack
- Python 3
- Flask (Web framework)
- spaCy, HuggingFace Transformers (for NLP)
- OpenCV, EasyOCR or pytesseract (for Vision)
- HTML/CSS for frontend
- Docker (optional for deployment)

---

## 📦 Installation

```bash
git clone https://github.com/yourusername/Smart_Document_Analyzer.git
cd Smart_Document_Analyzer
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

Make sure to install **Tesseract-OCR** if using pytesseract:
- Windows: https://github.com/tesseract-ocr/tesseract/wiki
- Ubuntu: `sudo apt install tesseract-ocr`

---

## ▶️ Run the App

```bash
python main.py
```

Visit `http://localhost:5000` in your browser.

---

## 📁 Project Structure

```
Smart_Document_Analyzer/
├── app/
│   ├── templates/
│   ├── static/
│   └── routes.py
├── models/
├── utils/
├── data/
├── main.py
├── requirements.txt
└── README.md
```

---

## 🙌 Contribution
Feel free to fork the repo, create pull requests, or submit issues!

---

## 📝 License
This project is open-source under the MIT License.

# 📝 Grammar Error Detection System

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)
![Streamlit](https://img.shields.io/badge/Framework-Streamlit-red?logo=streamlit)
![NLP](https://img.shields.io/badge/Field-NLP-green)
![Status](https://img.shields.io/badge/Status-Completed-brightgreen)

---

## 📌 Description

This project is a **grammar error detection system** that analyzes English text and provides feedback to improve grammatical accuracy.

The system detects **grammar errors**, classifies error types, generates corrected text, and calculates an overall **score** based on writing performance.

---

## 🎯 Research Question

> Can a rule-based NLP system automatically detect grammatical errors and improve English writing accuracy?

---

## ⚙️ Methodology

The system applies the following techniques:

* Grammar checking using **LanguageTool**
* Error classification *(Agreement, Tense, Article, Other)*
* Rule-based scoring system
* Automated correction generation
* Data storage and performance tracking

---

## 🚀 Features

### ✨ Core Features

* ✏️ Input paragraph and analyze grammar
* ❌ Detect grammar errors
* 💡 Provide corrected version
* 📊 Assign score *(0–10)*
* 📂 Store results *(history.csv)*

### 🔥 Additional Features

* 📊 Error type classification
* 📈 Score progress chart
* 📋 Data table display
* 📊 Error distribution visualization

---

## 📊 How It Works

1. User inputs text
2. System checks grammar using LanguageTool
3. Errors are detected and classified
4. Text is corrected automatically
5. Score is generated
6. Results are saved and visualized

---

## 📈 Example Output

* **Score:** 8.0 / 10
* **Grammar errors detected**
* **Corrected version provided**
* **Error types:**
  * Agreement
  * Tense
  * Article

---

## 🧠 Technologies Used

| Technology   | Purpose                   |
| ------------ | ------------------------- |
| Python       | Core programming language |
| Streamlit    | Web interface             |
| LanguageTool | Grammar checking          |
| Pandas       | Data processing           |
| Matplotlib   | Data visualization        |

---

## 📂 Project Structure

```
grammar-error-detection/
│
├── app.py # Main application
├── history.csv # Stored results
├── requirements.txt # Dependencies
└── README.md # Documentation
```

---

## ▶️ How to Run

### 1. Install dependencies

```bash
pip install -r requirements.txt
```

### 2. Run the app

```bash
streamlit run app.py
```

### 3. Open browser

```bash
http://localhost:8501
```
---

## 📊 Evaluation

The system was tested with multiple user inputs:

*Texts with more grammar errors → lower scores*
*Texts with fewer errors → higher scores*

✅ This confirms the effectiveness of the scoring mechanism.
---

## 💡 Future Improvements

* Improve grammar detection accuracy
* Add detailed explanations for errors
* Integrate machine learning models
* Enhance user interface

---

## 👨‍💻 Author

**Bao Chau – Grammar Error Detection System**

---
## ⭐ Project Highlights

* Combines **NLP + rule-based system + web app**
* Practical tool for **grammar learning**
* Interactive and user-friendly interface
* Works as a **mini grammar checking system**
  
---

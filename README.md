# 📖 AI Storytelling App (Groq API + LSTM + GRU)

An AI-powered storytelling application that generates creative and engaging stories based on user input. The system integrates Groq API for fast inference along with deep learning models (LSTM & GRU) to enhance narrative coherence and contextual understanding.

---

## 🚀 Features

- ✨ Generate stories from custom prompts
- 🎭 Multiple genres (Fantasy, Horror, Sci-Fi, etc.)
- 📏 Adjustable story length (Short / Medium / Long)
- ⚡ High-speed generation using Groq API
- 🧠 Deep Learning integration (LSTM & GRU)
- 🌐 Interactive UI (Streamlit)

---

## 🧠 Tech Stack

- **Programming Language:** Python  
- **Framework:** Streamlit  
- **API:** Groq API  
- **Deep Learning Models:** LSTM, GRU  
- **Libraries:** TensorFlow / Keras, NumPy, Pandas  
- **NLP Techniques:** Text generation, sequence modeling  

---

## 📂 Project Structure
AI-Storytelling-App/
│
├── app.py # Streamlit frontend
├── own_agents.py # Story generation logic (Groq API)
├── models/ # LSTM & GRU models (optional)
├── data/ # Training data (not included)
├── requirements.txt # Dependencies
├── README.md # Documentation
└── .gitignore # Ignored files

## ⚙️ How It Works

1. User inputs a story idea, genre, and length  
2. Prompt is processed and sent to Groq API  
3. LSTM/GRU models assist in sequence generation logic  
4. AI generates a structured and coherent story  

---

## ▶️ How to Run the Project

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/AI-Storytelling-App.git
cd AI-Storytelling-App

Sample Input
Story Idea: A girl receives messages from her future self
Genre: Fantasy
Length: Medium

Sample Output
AI-generated story with structured narrative, characters, and plot progression

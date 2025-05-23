# 🤖 Wizzen - AI Voice Assistant

**Wizzen** is an intelligent voice assistant inspired by Jarvis from Iron Man. It uses the **Gemini API** for natural language processing and **PyQt** for a sleek desktop GUI.

## 🧠 Features

- 🎤 Voice command recognition
- 🗣️ AI-powered responses (Gemini API)
- 💻 User-friendly GUI (built with PyQt)
- 🔁 Task automation (web search, opening apps, etc.)
- 🧩 Modular design for easy extension



## 🛠️ Tech Stack

| Component        | Technology        |
|------------------|-------------------|
| Language Model   | Gemini API        |
| GUI Framework    | PyQt (Qt for Python) |
| Language         | Python 3.x        |
| Speech           | `speech_recognition`, `pyttsx3` |



## 🚀 Getting Started

### 1. Clone the Repository
    git clone https://github.com/Santhosh-6/Ai_Voice_Assistant.git
    cd Ai_Voice_Assistant
    
### 2. Set Up a Virtual Environment 
    python -m venv venv
    venv\Scripts\activate

### 3. Install Dependencies
    pip install -r requirements.txt

### 4. Add Your Gemini API Key
    Replace the gemini api key in mani.py
    genai.configure(api_key=("YOUR_API_KEY"))  

### 5. Run Wizzen
    python main.py

## 📁 Project Structure
    Ai_Voice_Assistant/
    ├── functions/(online_ops.py,os_ops.py)                 
    ├── Resource/(.png,.gifs)         
    ├── template.py                  
    ├── main.py                  
    ├── LICENSE      
    └── README.md        


## ✨ Credits

**Wizzen** — AI Voice Assistant  
Developed with passion by:

-  **Santhosh** 
-  **Dhivakar** 

Special thanks to:
- The open-source community
- Google Gemini API team
- Qt framework contributors

# 🤝 Contributing to Wizzen - AI Voice Assistant

We welcome contributions from developers, designers, and AI enthusiasts!  
Whether it’s fixing bugs, adding features, or improving documentation, your help is appreciated.

## 📄 License

This project is licensed under the [MIT License](LICENSE).  
You're free to use, modify, and distribute it with proper attribution.


# SENTIMENT-ANALYSIS-OF-PATIENT-FEEDBACK-USING-NLP

# Sentiment Analysis of Patient Feedback

This project is a **Natural Language Processing (NLP)** application that analyzes hospital or clinic patient feedback to determine its sentiment as **Positive, Negative, or Neutral**.  
It is built using **Python**, **Flask**, **NLTK's VADER Sentiment Analyzer**, and visualization libraries to make insights easy to understand.


📌 Features

- Accepts patient feedback text as input from a web interface.
- Classifies sentiment into **Positive**, **Negative**, or **Neutral**.
- Displays sentiment score (compound, positive, negative, neutral values).
- Generates visual insights:
  - Sentiment distribution chart
  - Word cloud of frequently used words
- Simple and responsive Flask web interface.
- Works locally without requiring a GPU or cloud deployment.


🛠️ Tech Stack

- **Programming Language:** Python 3
- **Framework:** Flask
- **NLP:** NLTK (VADER Sentiment Analyzer)
- **Visualization:** Matplotlib, WordCloud
- **Frontend:** HTML, CSS (Flask templates)



📂 Project Structure

project-folder/
├── app.py                # Main Flask application
├── requirements.txt      # Python dependencies
├── templates/
│   └── index.html        # Web interface
├── static/
│   └── style.css         # Stylesheet
├── report/
│   └── tharun.pdf        # Detailed project report
└── README.md             # Project documentation



🚀 Installation & Usage

1. **Clone the repository**

   git clone https://github.com/<tharunjakkam939>/<SENTIMENT-ANALYSIS-OF-PATIENT-FEEDBACK-USING-NLP>.git
   cd <SENTIMENT-ANALYSIS-OF-PATIENT-FEEDBACK-USING-NLP>

2. **Create a virtual environment (optional but recommended)**

   
   python -m venv venv
   source venv/bin/activate       # On macOS/Linux
   venv\Scripts\activate          # On Windows
   

3. **Install dependencies**

   
   pip install -r requirements.txt
   

4. **Run the application**

   
   python app.py
   

   Open the browser at **[http://127.0.0.1:5000/](http://127.0.0.1:5000/)**
   ![image alt](https://github.com/tharunjakkam939/SENTIMENT-ANALYSIS-OF-PATIENT-FEEDBACK-USING-NLP-/blob/ab89bc49dc4799cdccc2228d0a714546971cba31/outputs/nlp1.png)
    ![image alt]( ![image alt](https://github.com/tharunjakkam939/SENTIMENT-ANALYSIS-OF-PATIENT-FEEDBACK-USING-NLP-/blob/ab89bc49dc4799cdccc2228d0a714546971cba31/outputs/nlp1.png))

    ![image alt](https://github.com/tharunjakkam939/SENTIMENT-ANALYSIS-OF-PATIENT-FEEDBACK-USING-NLP-/blob/da5822121fa6150c96e681e1444a74a932ef1bde/outputs/nlp3.png)



📊 Example Output

* **Text Input:** *"The doctors were kind and attentive, but the waiting time was too long."*
* **Sentiment:** Neutral
* **Compound Score:** 0.10
* **Positive Score:** 0.35
* **Negative Score:** 0.20
* **Visuals:** Pie chart & word cloud generated automatically.



📜 Future Improvements

* Deploy on a cloud platform (Heroku, Render, etc.)
* Add multi-language sentiment analysis.
* Integrate database to store and analyze feedback over time.
* Improve UI with Bootstrap or Tailwind CSS.


📄 License

This project is for **educational purposes** and is not intended for production use in a real hospital setting without further validation.


👤 Author

**Tharun Jakkam**

* GitHub: [tharunjakkam939](https://github.com/<your-username>)
* LinkedIn: [https://www.linkedin.com/in/tharun-jakkam-123733336/](https://linkedin.com/in/<your-linkedin>)




# 🧠 GenAI E-commerce Question Answering Agent

This project is built as part of the **GenAI Intern Task (VIT)**. It enables users to ask natural language questions about e-commerce datasets, converts them into SQL queries using logic/LLM, and responds via an API.

---

## 🚀 Features

✅ Converts natural language to SQL  
✅ Queries SQLite database dynamically  
✅ FastAPI-powered API endpoint  
✅ Bonus: Generates visual charts from database  
✅ Fully offline-compatible with optional Gemini API support

---

## 📁 Folder Structure

genai_ecom_agent/
├── app/
│ ├── main.py # FastAPI app entrypoint
│ ├── db_connector.py # Handles DB query execution
│ ├── llm_handler.py # Contains logic to convert questions → SQL
│ └── visualizer.py # Bonus: generates bar chart visualizations
├── db/
│ └── ecommerce.db # SQLite database with 3 loaded tables
├── data/
│ ├── ad_sales.csv
│ ├── total_sales.csv
│ └── eligibility.csv
├── demo/
│ └── demo_video.mp4 # Required demo video
├── prepare_db.py # Script to convert CSV → SQLite tables
├── requirements.txt # Python dependencies
└── README.md # This file


---

## 📦 Installation

1. **Clone the repo**  
   ```bash
   git clone https://github.com/your-username/genai_ecom_agent.git
   cd genai_ecom_agent

    Install dependencies

pip install -r requirements.txt

Convert CSVs to SQLite

python prepare_db.py

Run the FastAPI server

    python -m uvicorn app.main:app --reload

🔗 API Usage

Go to: http://127.0.0.1:8000/docs

Use the /ask POST endpoint to send JSON questions like:

{
  "question": "What is my total sales?"
}

💡 Supported Questions
💬 Question	🧠 Translated SQL	✅ Status
What is my total sales?	SELECT SUM(total_sales) FROM TotalSales;	✅
Calculate the RoAS	SELECT SUM(ad_sales)/SUM(ad_spend) FROM AdSales;	✅
Which product had the highest CPC?	ORDER BY (ad_spend/clicks) DESC LIMIT 1	✅
Show a chart of sales per item	Generates a bar chart (.png)	✅ Bonus
📊 Demo Video

🎥 Video demo: Google Drive Link

    Includes API call + terminal output for all 3 required questions.

📌 Submission

GitHub Repo with working code

Demo video answering 3 questions

    Bonus: Visualization chart generation

🧑‍💻 Built With

    FastAPI

    SQLite

    Pandas

    Matplotlib

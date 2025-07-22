from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.responses import FileResponse
from app.llm_handler import generate_sql_from_question
from app.db_connector import execute_sql_query
from app.visualizer import generate_sales_bar_chart

app = FastAPI()

class Query(BaseModel):
    question: str

@app.post("/ask")
def ask_question(payload: Query):
    question = payload.question.lower()

    # ✅ Check for visual-related keyword BEFORE trying to convert to SQL
    if "chart" in question or "graph" in question or "visual" in question:
        chart_path = generate_sales_bar_chart()
        if chart_path:
            return FileResponse(chart_path, media_type="image/png")
        else:
            return {"error": "No data found for chart."}

    # Else proceed normally
    sql_query = generate_sql_from_question(question)
    result = execute_sql_query(sql_query)

    return {
        "question": payload.question,
        "sql": sql_query,
        "answer": result
    }

from google import genai
import mysql.connector
from dotenv import load_dotenv
import os

load_dotenv()

# Configure Gemini
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

# Connect to MySQL
db = mysql.connector.connect(
    host=os.getenv("DB_HOST"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    database=os.getenv("DB_NAME")
)

# Database schema context
SCHEMA = """
Database: e_master_card (Bank Credit Card Launch Project)

Tables:
1. customers(cust_id, name, gender, age, location, occupation, annual_income, marital_status)
2. transactions(trans_id, cust_id, tran_date, tran_amount, product_category, payment_type)
3. credit_profiles(cust_id, credit_score, credit_utilisation, outstanding_debit, credit_inquires_last_6_months, credit_limit)
4. avg_transactions_after_campaign(campaign_date, control_group_avg_tran, test_group_avg_tran)
"""

def ask_bank(question: str):
    # Step 1 — Ask Gemini to generate SQL
    prompt = f"""
You are a MySQL expert working on a bank credit card dataset.
Here is the database schema:
{SCHEMA}

Convert this question to a valid MySQL SELECT query only.
Return ONLY the SQL query — no explanation, no markdown, no backticks.
Never use DROP, DELETE, UPDATE or INSERT.

Question: {question}
"""
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )
    sql = response.text.strip()

    print(f"\nGenerated SQL:\n{sql}\n")

    # Step 2 — Run SQL on MySQL
    try:
        cursor = db.cursor()
        cursor.execute(sql)
        columns = [desc[0] for desc in cursor.description]
        rows = cursor.fetchall()
        return columns, rows, sql
    except Exception as e:
        return None, None, f"SQL Error: {str(e)}"

# 🏦 BankQuery AI — Natural Language SQL Agent

> An AI-powered agent that converts plain English questions into SQL queries on a real banking database — enabling non-technical analysts to query fraud patterns, customer segments, and transaction data without writing SQL.

![Tech Stack](https://img.shields.io/badge/Python-3.10+-blue) ![Gemini](https://img.shields.io/badge/Google%20Gemini-2.5%20Flash-orange) ![Streamlit](https://img.shields.io/badge/Streamlit-Latest-red) ![MySQL](https://img.shields.io/badge/MySQL-Database-blue)

---

## 🎯 Problem Solved

In banking environments, fraud analysts and business teams depend on tech teams to write SQL queries for every data request. This creates bottlenecks and delays.

**BankQuery AI removes this dependency** — analysts can now ask questions in plain English and get instant SQL-backed answers.

---

## 💡 Example Use Cases

```
User: "Show me top 5 customers by total spending"
→ Agent generates SQL with JOIN across customers and transactions tables
→ Returns formatted results with the SQL it used

User: "Which location has the highest spending?"
→ Agent groups, aggregates, and sorts automatically
→ Displays result in interactive table
```

---

## 🧠 How It Works

```
User Question (English)
        ↓
Gemini AI reads database schema
        ↓
Generates contextually accurate SQL
        ↓
Python executes query on MySQL
        ↓
Returns result + SQL used in chat UI
```

---

## 🛠 Tech Stack

| Layer | Technology |
|-------|-----------|
| AI Model | Google Gemini 2.5 Flash API |
| Database | MySQL |
| Backend | Python + mysql-connector |
| UI | Streamlit |
| Config | python-dotenv |

---

## 📁 Project Structure

```
bankquery-ai/
├── agent.py          # Core AI + database logic
├── app.py            # Streamlit chat UI
├── test.py           # Test suite for query validation
├── .env.example      # Template for credentials
├── requirements.txt  # Python dependencies
└── README.md         # You are here
```

---

## 🚀 Setup Instructions

**1. Clone the repository**
```bash
git clone https://github.com/juliet3-lab/bankquery-ai.git
cd bankquery-ai
```

**2. Install dependencies**
```bash
pip install google-genai mysql-connector-python streamlit pandas python-dotenv
```

**3. Set up your environment variables**
```bash
cp .env.example .env
```
Then open `.env` and add your actual Gemini API key and MySQL credentials.

**4. Set up your MySQL database**

Make sure you have a database with these tables:
- `customers` (cust_id, name, gender, age, location, occupation, annual_income, marital_status)
- `transactions` (trans_id, cust_id, tran_date, tran_amount, product_category, payment_type)
- `credit_profiles` (cust_id, credit_score, credit_utilisation, outstanding_debit, credit_inquires_last_6_months, credit_limit)
- `avg_transactions_after_campaign` (campaign_date, control_group_avg_tran, test_group_avg_tran)

**5. Run the app**
```bash
streamlit run app.py
```

Your browser will automatically open at `http://localhost:8501`.

---

## 🔒 Security Features

- ✅ API keys stored in `.env` file (never hardcoded)
- ✅ Read-only SQL — agent cannot run DROP, DELETE, UPDATE, INSERT
- ✅ Schema-aware prompt engineering for safe query generation
- ✅ Graceful error handling for invalid queries

---

## 🧪 Sample Questions to Try

- "How many customers do we have?"
- "What is the average transaction amount?"
- "Show top 5 customers by total spending"
- "Find customers with credit score above 750"
- "Which location has the highest number of customers?"
- "What is the average credit limit by occupation?"

---

## 📊 Banking Domain Context

Built on a real bank credit card launch dataset containing:
- 1000 customer records
- 4 linked tables — customers, transactions, credit profiles, campaign data
- Real-world fields covering demographics, credit behaviour, and transaction patterns

---

## 🔮 What's Next

- [ ] Add visualisation for query results — auto-generate charts for numerical answers
- [ ] Implement conversation memory — let users ask follow-up questions like "now filter that by location"
- [ ] Deploy to Streamlit Cloud for public demo access
---

## 👤 Author

**Florence Arul Juliet** — Banking Domain Professional transitioning into Data Science & AI

- 💼 3.7 years in BFSI · Fraud Detection · Transaction Analysis
---

## 📜 License

This project is open source and available under the MIT License.

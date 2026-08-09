**Manufacturing Data AI Agent**

A quick LangChain project I built to test out natural language SQL querying. Instead of writing manual SQL queries to check plant sensor data, this agent lets you "chat" with the database.

Right now it uses a dummy SQLite DB of manufacturing machines, but the concept scales to real SQL warehouses.

**How it works**

1. Takes a user question (e.g., "Which machines are overheating?")
2. Uses an LLM to look at the DB schema and write the correct SQL query.
3. Executes the SQL query.
4. Passes the results back to the LLM to generate a human-readable answer.

**Tech Stack**
1. Python 3.10
2. LangChain (create_sql_agent)
3. OpenAI API (gpt-3.5-turbo)
4. SQLite 

**Setup & Run**

**1. Clone the repo:**
git clone (https://github.com/anubhavvaishnav/AI-Data-Agent)

**2. Install dependencies:**
```bash
pip install langchain langchain-openai langchain-community langchain-experimental sqlalchemy python-dotenv
```
**3. Add your API Key:**
-----------------------

**4. Initialize the database:**
```bash
python setup_db.py
```
**5. Run the agent:**
```bash
python run_agent.py
```
**Example Chat**
```bash
Question: Which machines currently have a status other than 'Normal'?

Agent Answer: The machines with a status other than 'Normal' are CNC_Mill_01 (Overheating) and Metal_3D_Printer_01 (Maintenance Required).
```
**TODOs / Future Work**

1. Upgrade to gpt-4o-mini to improve JSON parsing reliability.
2. Connect to a live PostgreSQL database instead of SQLite.
3. Add a Streamlit UI so non-technical managers can use it easily.


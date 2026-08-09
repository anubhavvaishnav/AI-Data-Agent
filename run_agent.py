import os
import warnings
from dotenv import load_dotenv
from langchain_community.utilities import SQLDatabase
from langchain_openai import ChatOpenAI
from langchain_community.agent_toolkits import create_sql_agent
from langchain.agents.agent_types import AgentType

# Ignore langchain deprecation warnings for now (need to update to LangGraph later)
warnings.filterwarnings("ignore")

def main():
    load_dotenv()
    
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        print("ERROR: Missing OPENAI_API_KEY in .env file!")
        return

    print("Connecting to local DB...")
    db = SQLDatabase.from_uri("sqlite:///plant_sensors.db")
    
    # Using gpt-3.5-turbo to keep API costs low during testing
    # TODO: Switch to gpt-4o-mini for better tool calling
    llm = ChatOpenAI(temperature=0, model="gpt-3.5-turbo", openai_api_key=api_key)
    
    print("Setting up SQL Agent...")
    agent = create_sql_agent(
        llm=llm,
        db=db,
        agent_type=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
        verbose=True,
        handle_parsing_errors=True # gpt-3.5 sometimes messes up the JSON, this fixes it
    )
    
    print("\n" + "="*50)
    print("PLANT DATA AGENT READY")
    print("Ask questions about the machines, or type 'exit' to quit.")
    print("="*50 + "\n")
    
    # Interactive chat loop
    while True:
        user_input = input("Question: ")
        if user_input.lower() in ['exit', 'quit']:
            break
            
        try:
            response = agent.invoke({"input": user_input})
            print("\nAgent Answer:", response['output'])
            print("-" * 50)
        except Exception as e:
            print(f"Agent crashed on this query: {e}")
            print("-" * 50)

if __name__ == "__main__":
    # Auto-init DB if it doesn't exist
    if not os.path.exists("plant_sensors.db"):
        import setup_db
        setup_db.init_db()
        
    main()

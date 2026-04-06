from langchain_groq import ChatGroq
from langchain_experimental.agents import create_csv_agent
from config import groqAPIkey, modelName

def main():
    csv = input("Enter CSV file path: ")

    llm = ChatGroq(api_key = groqAPIkey, model = modelName)

    agent = create_csv_agent(
        llm = llm,
        path = csv, 
        verbose = True,
        allow_dangerous_code = True
    )

    while True:
        question = input("You: ")
        if question.lower() == 'exit':
            break

        answer = agent.invoke(question)
        print(f"Bot: {answer['output']}\n")

if __name__ == "__main__":
    main()
# CSV Data Analyst

A CSV Data Analyst app built with LangChain and Groq. Upload any CSV file
and ask questions about your data in plain English. Powered by a LangChain
CSV Agent that internally writes and executes Pandas code to analyze your
data and return accurate answers using llama-3.3-70b-versatile.

## Features

- Load any CSV file from local path
- Ask questions in plain English
- Agent writes and runs Pandas code internally
- Powered by llama-3.3-70b-versatile via Groq
- Verbose mode to see agent thinking process

# Get Started

## Setting up the Environment

first create .env file in the root of this project

```
GROQ_API_KEY=YOUR_API_KEY
```

## Create and Activate your Virtual Environment

```
python -m venv .venv
.venv\Scripts\activate
```

## Install dependencies

```
pip install -r requirements.txt
```

## Run the main.py file

```
python main.py
```

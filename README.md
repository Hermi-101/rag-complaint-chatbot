🛡️ CrediTrust Complaint Assistant (RAG)
An AI-powered Retrieval-Augmented Generation (RAG) system built to help financial analysts navigate and analyze customer credit card complaints efficiently.

🌟 Overview
Analysts at CrediTrust often have to sift through thousands of customer complaints to identify systemic issues. This project automates that process by allowing analysts to ask natural language questions. The system retrieves the most relevant complaints from a local database and uses a Large Language Model (LLM) to summarize the findings.

🚀 Key Features
Intelligent Retrieval: Uses ChromaDB and Hugging Face Embeddings to find relevant context from a dataset of credit card complaints.

Context-Aware Generation: Powered by Mistral-7B-Instruct-v0.3 via the Hugging Face Inference API.

Transparent Sources: Displays the specific snippets of raw data used by the AI to ensure accuracy and trust.

Streaming Web UI: A modern, interactive chat interface built with Gradio 6.0.

Secure: Implements environment variable management to protect sensitive API credentials.

🛠️ Tech Stack
Language: Python 3.12

Orchestration: LangChain

Vector Database: ChromaDB

LLM Provider: Hugging Face (Serverless Inference)

Frontend: Gradio

📦 Installation & Setup
1. Clone the Repository
Bash

git clone https://github.com/Hermi-101/rag-complaint-chatbot.git
cd rag-complaint-chatbot
2. Set Up Virtual Environment
Bash

python -m venv .venv
source .venv/Scripts/activate  # Windows
# source .venv/bin/activate    # Mac/Linux
pip install -r requirements.txt
3. Environment Variables
Create a .env file in the root directory and add your Hugging Face API token:

Plaintext

HUGGINGFACEHUB_API_TOKEN=your_hf_token_here
🖥️ Usage
Initialize the Vector Store (Optional/One-time)
If the database isn't built yet, run the ingestion script:

Bash

python src/ingest_data.py
Launch the Chatbot
Run the Gradio application:

Bash

python src/app.py
Open your browser and navigate to http://127.0.0.1:7860.

📂 Project Structure
Plaintext

rag-complaint-chatbot/
├── data/               # Raw CSV complaint data
├── src/
│   ├── rag_logic.py    # Core RAG pipeline and LangChain logic
│   └── app.py          # Gradio Web Interface
├── vector_store/       # Local ChromaDB persistent storage
├── .env                # API Keys (Ignored by Git)
├── .gitignore          # File exclusions
└── README.md           # Project documentation
🤝 Acknowledgments
Built as part of the Week 7: RAG Chatbot Project for the CrediTrust case study.

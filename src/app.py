import gradio as gr
import time
from rag_logic import ask_creditrust

def chatbot_response(message, history):
    """
    Handles the chat logic, streaming, and source display.
    """
    # 1. Call your RAG function
    answer, docs = ask_creditrust(message)
    
    # 2. Format the sources
    source_content = "\n\n---\n### 📚 Sources used from CrediTrust Database:\n"
    for i, doc in enumerate(docs):
        content = doc.page_content.replace("\n", " ")
        source_content += f"**Source {i+1}:** ...{content[:300]}...\n\n"

    # 3. Implement Streaming
    full_response = ""
    for char in answer:
        full_response += char
        yield full_response + source_content
        time.sleep(0.01)

# --- UI Layout (Gradio 6.0 Optimized) ---
with gr.Blocks() as demo:
    gr.Markdown("# 🛡️ CrediTrust Complaint Assistant")
    gr.Markdown("Analyzing financial complaints to provide data-driven insights.")
    
    # The ChatInterface no longer takes 'theme' or 'title'
    chat_interface = gr.ChatInterface(
        fn=chatbot_response,
        chatbot=gr.Chatbot(height=500, label="CrediTrust AI"),
        textbox=gr.Textbox(placeholder="Ask about credit card issues...", container=False, scale=7),
        examples=["What are the main issues with credit cards?", "Tell me about billing disputes."],
    )
    
    gr.Markdown("---")
    gr.Markdown("Built for the **CrediTrust RAG Project** | Task 4")

if __name__ == "__main__":
    # THEME GOES HERE NOW in Gradio 6.0
    demo.launch(theme=gr.themes.Soft())
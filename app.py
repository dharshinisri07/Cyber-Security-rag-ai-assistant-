
import sys
from pathlib import Path

import truststore
truststore.inject_into_ssl()

import gradio as gr


# --------------------------------------------------
# 1. Project configuration
# --------------------------------------------------

PROJECT_ROOT = Path(__file__).resolve().parent
SRC_PATH = PROJECT_ROOT / "src"

sys.path.insert(0, str(SRC_PATH))

from rag_chain import generate_rag_answer


# --------------------------------------------------
# 2. Chatbot response function
# --------------------------------------------------

def chatbot_response(message, history):

    if not message or not message.strip():
        return "Please enter a cybersecurity question."

    try:
        result = generate_rag_answer(message.strip())

        answer = result.get(
            "answer",
            "No answer was generated."
        )

        sources = result.get("sources", [])

        if sources:
            source_text = "\n".join(
                f"- {source}" for source in sources
            )

            answer += "\n\n**Sources:**\n" + source_text

        return answer

    except Exception as error:

        print("\nChatbot Error:", error)

        return (
            "Sorry, an error occurred while processing "
            "your question. Please try again."
        )


# --------------------------------------------------
# 3. Create chatbot interface
# --------------------------------------------------

with gr.Blocks(
    title="Cybersecurity RAG AI Assistant",
    theme=gr.themes.Soft(
        primary_hue="cyan",
        secondary_hue="blue",
        neutral_hue="slate"
    )
) as demo:

    gr.Markdown(
        """
        # Cybersecurity RAG AI Assistant

        ### Your AI-powered cybersecurity learning companion

        Ask questions about cybersecurity, network security,
        web application security, digital forensics and more.

        **Powered by:** Python | FAISS | LangChain | Google Gemini
        """
    )

    gr.ChatInterface(
        fn=chatbot_response,
        examples=[
            "What is cybersecurity?",
            "Explain the CIA triad.",
            "How can SQL Injection be prevented?",
            "What is a SIEM system?",
            "What is digital forensics?"
        ]
    )


# --------------------------------------------------
# 4. Launch application
# --------------------------------------------------

if __name__ == "__main__":

    print("\n" + "=" * 55)
    print("CYBERSECURITY RAG AI ASSISTANT")
    print("=" * 55)

    print("\nStarting application...")

    demo.launch(
        server_name="127.0.0.1",
        server_port=7860,
        inbrowser=True,
        show_error=True
    )

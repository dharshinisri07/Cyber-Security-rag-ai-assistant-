
import truststore
truststore.inject_into_ssl()

import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI


# Load API key from the main project .env file
load_dotenv()

api_key = os.getenv("GOOGLE_API_KEY")

if not api_key:
    raise ValueError("Gemini API key not found. Check your .env file.")


# Initialize Gemini
llm = ChatGoogleGenerativeAI(
    model="gemini-3.8-flash",
    temperature=0.2,
    google_api_key=api_key
)


def generate_response(prompt):

    response = llm.invoke(prompt)

    # Extract readable text from Gemini response
    content = response.content

    if isinstance(content, str):
        return content

    if isinstance(content, list):
        text_parts = [
            block["text"]
            for block in content
            if isinstance(block, dict)
            and block.get("type") == "text"
        ]

        return "\n".join(text_parts)

    return str(content)

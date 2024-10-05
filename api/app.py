from fastapi import FastAPI
from langchain.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms import Ollama
from langserve import add_routes
import uvicorn
import os
from dotenv import load_dotenv

load_dotenv()

# Set environment variables
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")

# Initialize FastAPI app
app = FastAPI(
    title="Langchain Server",
    version="1.0",
    description="A simple API server using llama2 for poems and a generic chatbot"
)

# Initialize the LLM with Ollama (Llama2 model)
llm = Ollama(model="llama2")

# Define prompt for poem generation
poem_prompt = ChatPromptTemplate.from_template("Write me a poem about {topic} around 50 words.")

# Define prompt for a generic chatbot
generic_prompt = ChatPromptTemplate.from_template("Respond to the following query in {language}: {query}")

# Add routes for the poem endpoint
add_routes(
    app,
    poem_prompt | llm,
    path="/poem"  # Keep the original poem endpoint
)

# Add routes for the generic chatbot endpoint
add_routes(
    app,
    generic_prompt | llm,
    path="/generic"  # New endpoint for generic chatbot
)

if __name__ == "__main__":
    uvicorn.run(app, host='localhost', port=8000)

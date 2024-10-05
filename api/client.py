import streamlit as st
import requests

# Function for poem generation
def get_poem_response(topic):
    response = requests.post("http://localhost:8000/poem/invoke",
                             json={'input': {'topic': topic}})
    return response.json()['output']

# Function for generic chatbot response
def get_chatbot_response(query, language):
    response = requests.post("http://localhost:8000/generic/invoke",
                             json={'input': {'query': query, 'language': language}})
    return response.json()['output']

# Streamlit UI
st.title('Langchain Demo With LLAMA2 API')

# Poem Generation Section
st.header("Poem Generator")
input_text1 = st.text_input("Write a poem on")
if input_text1:
    st.write(get_poem_response(input_text1))

# Generic Chatbot Section
st.header("Generic Multilingual Chatbot")
input_query = st.text_input("Enter your query")
input_language = st.text_input("Response language (default is English)")

if input_query:
    if not input_language:
        input_language = "English"  # Default to English if no language is provided
    st.write(get_chatbot_response(input_query, input_language))

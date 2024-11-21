from dotenv import load_dotenv
import google.generativeai as genai
import os
import streamlit as st

load_dotenv()
os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

model = genai.GenerativeModel("gemini-pro")
chat = model.start_chat(history=[])
def get_response(question):
    response = model.generate_content(question)
    return response.text

st.set_page_config("Q & A")
st.header("Initial application")
input = st.text_input("Enter Question", key = "input")
submit = st.button("Ask the question")

if submit:
    response = get_response(input)
    print(response)
    st.subheader("Answer is here")
    st.write(response)


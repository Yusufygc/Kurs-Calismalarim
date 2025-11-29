import streamlit as st
from google import genai
from dotenv import load_dotenv
import os

load_dotenv()
API_KEY = os.getenv("GEMINI_API_KEY")

if not API_KEY:
    st.error("Missing GEMINI_API_KEY in .env file. Please add it and restart the app.")
    st.stop()

client = genai.Client(api_key=API_KEY)
MODEL_NAME = "models/gemini-2.5-flash"

st.set_page_config(page_title="PersonalBot", layout="centered")
st.title(" PersonalBot")
st.markdown("An intelligent assistant powered by **Gemini** and **Streamlit**.")

if "history" not in st.session_state:
    st.session_state.history = []


def get_gemini_response(prompt):
    response = client.models.generate_content(
        model=MODEL_NAME,
        contents=prompt
    )
    return response.text


for role, msg in st.session_state.history:
    if role == "user":
        st.markdown(f"** You:** {msg}")
    else:
        st.markdown(f"** PersonalBot:** {msg}")

user_input = st.text_input("Type your message here...")

if st.button("Send"):
    if user_input.strip():
        st.session_state.history.append(("user", user_input))
        with st.spinner("PersonalBot is thinking..."):
            try:
                reply = get_gemini_response(user_input)
            except Exception as e:
                reply = f" Error: {e}"

        st.session_state.history.append(("bot", reply))
        st.rerun()
    else:
        st.warning("Please enter a message before sending.")
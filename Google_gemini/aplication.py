

import os
import sys
import subprocess

import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import SystemMessage, HumanMessage
from dotenv import load_dotenv

# Automatically launch Streamlit when running this file with Python
from streamlit.runtime.scriptrunner import get_script_run_ctx

if get_script_run_ctx(suppress_warning=True) is None:
    subprocess.run([
        sys.executable, "-m", "streamlit", "run", os.path.abspath(__file__)
    ], check=True)
    sys.exit()

load_dotenv()

st.set_page_config(
    page_title="Travel Assistance",
    page_icon="✈️",
    layout="centered"
)

model = ChatGoogleGenerativeAI(model="gemini-3.5-flash-lite")

sys_message = """
Instruction:
You are a travel assistance bot.
Answer questions related to travelling and tourism only.
For other questions not related to tourism, reply:
"Unable to answer your question. I can answer questions related to tourism."
Give clear, helpful answers using headings, paragraphs and bullet points
where appropriate. Do not format normal answers as code.
"""

# Web UI
st.title("✈️ Travel Assistance")
st.write("Your AI travel companion. Where would you like to go?")

with st.form("travel_form"):
    human_result = st.text_area(
        "Ask your travel question",
        placeholder="Example: Suggest the best places to visit in Goa for 3 days.",
        height=120
    )

    submit = st.form_submit_button(
        "✈️ Send Question",
        use_container_width=True
    )

if submit:
    if not human_result.strip():
        st.warning("Please enter a travel question.")
    else:
        try:
            with st.spinner("🌍 Preparing your travel recommendations..."):
                result = model.invoke([
                    SystemMessage(content=sys_message),
                    HumanMessage(content=human_result.strip())
                ])

            st.subheader("🌎 Travel Assistance")

            # Extract readable text from Gemini's response
            if isinstance(result.content, str):
                answer = result.content

            elif isinstance(result.content, list):
                answer = "\n\n".join(
                    block["text"]
                    for block in result.content
                    if isinstance(block, dict)
                    and block.get("type") == "text"
                    and isinstance(block.get("text"), str)
                )

            else:
                answer = str(result.content)

            # Handle escaped newline characters
            answer = answer.replace("\\n", "\n")

            # Display formatted Markdown, not raw Python data
            st.markdown(answer)

        except Exception as e:
            st.error("Unable to process your question.")
            st.caption(str(e))

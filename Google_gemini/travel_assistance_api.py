# we are making travel assistance here using google gemini library

# all the dependencies has been installed in requirment.txt file and imported here 
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import SystemMessage, HumanMessage
from dotenv import load_dotenv
import streamlit as st

load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-3.5-flash-lite")

sys_message = """
    you are a travel assistance bot \
    give answers related to travleling and tourism only \
    related to travleling and tourism only \
    do not give answers relatedd to different industry or topice \
    strictly reply unable to answer you question \
    i can answer related to tourism
""" 

Human_result= input("enter you question related to tourism : ")


result = model.invoke([('system', sys_message), ('human', Human_result)])
print(result.content)
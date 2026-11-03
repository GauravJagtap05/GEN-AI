from langchain_google_genai import ChatGoogleGenerativeAI

from langchain_core.messages import HumanMessage, SystemMessage

from dotenv import load_dotenv
load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-3.5-flash-lite")

SystemMessage =
"""act like you are a data engineer \
   give answers according to a senior data engineer \
   give answers in 2-3 lines only' """

human_message = HumanMessage(content='what data engineering tools are used in the industry?')

result = model.invoke([
    ('system', sys_message),
    ('human', human_message)])

print(result.content)
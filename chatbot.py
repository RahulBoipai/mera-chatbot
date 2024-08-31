## Conversational AI Chatbot - QnA Chatbot
import streamlit as st 

from langchain.schema import HumanMessage, SystemMessage, AIMessage
from langchain_ollama.chat_models import ChatOllama
from langchain.chat_models import ChatOpenAI


st.set_page_config(page_title="QnA Chatbot", page_icon=":robot_face:")
st.header("HeY :wave: Ask me anything!")

from dotenv import load_dotenv
load_dotenv()


#chat = ChatOllama(model="llama3.1", temperature=0.5)
chat = ChatOpenAI(temperature=0.5)

if 'flowmessages' not in st.session_state:
    st.session_state['flowmessages'] = [
        SystemMessage(content="I am a QnA Chatbot. I love humor and reply in a funny way. Ask me anything!"),
    ]
def get_response(question):
    st.session_state['flowmessages'].append(HumanMessage(content=question))
    answer=chat(st.session_state['flowmessages'])
    st.session_state['flowmessages'].append(HumanMessage(content=answer.content))
    return answer.content
    
input = st.text_input("Input: ",key="input")
response=get_response(input)

submit=st.button("Ask the question")

#if button is clicked
if submit:
    st.subheader(":robot_face: :loudspeaker:")
    st.write(response)

## Conversational AI Chatbot - QnA Chatbot
import streamlit as st 

from langchain.schema import HumanMessage, SystemMessage, AIMessage
from langchain_ollama.chat_models import ChatOllama
# from langchain.chat_models import ChatOpenAI

## 
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser


st.set_page_config(page_title="QnA Chatbot", page_icon=":robot_face:")
st.header("HeY :wave: I am a ChatBOT! 	:left_speech_bubble: :robot_face:")

from dotenv import load_dotenv
load_dotenv()

# prompt = ChatPromptTemplate.from_messages(
#     [
#         ("system", "I am a QnA Chatbot. I love humor and reply in a funny way. Ask me anything!"),
#         ("user", "Question:{question}"),
#     ]
# )
# input_text = st.text_input("Enter you words: ", key="input")

# llm = ChatOllama(model="llama3", temperature=0.5)
# output_parser = StrOutputParser()


# chain = prompt|llm|output_parser
# if 'flowmessages' not in st.session_state:
#     st.session_state['flowmessages'] = [
#         SystemMessage(content="I am a QnA Chatbot. I love humor and reply in a funny way. Ask me anything!"),
#     ]

# if input_text:
#     st.session_state['flowmessages'].append(HumanMessage(content=input_text))
#     response = chain.invoke({"question": st.session_state['flowmessages']})
#     st.session_state['flowmessages'].append(HumanMessage(content=response))
#     st.subheader(":robot_face: :loudspeaker:")
#     #st.write(st.session_state['flowmessages']) # for debugging
#     st.write(response)

chat = ChatOllama(model="llama3", temperature=0.5)
# # chat = ChatOpenAI(temperature=0.5)


if 'flowmessages' not in st.session_state:
    st.session_state['flowmessages'] = [
        SystemMessage(content="I am a QnA Chatbot. I love humor and reply in a funny way. Ask me anything!"),
    ]
def get_response(question):
    st.session_state['flowmessages'].append(HumanMessage(content=question))
    answer=chat(st.session_state['flowmessages'])
    st.session_state['flowmessages'].append(HumanMessage(content=answer.content))
    return answer.content
    
input = st.text_input("ask me anything: ",key="input")
response=get_response(input)

submit=st.button("Enter")

#if button is clicked
if response or submit:
    st.subheader(":robot_face: :loudspeaker:")
    st.write(response)

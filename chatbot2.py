import streamlit as st 
from streamlit_chat import message
from dotenv import load_dotenv #use env variables

from langchain.schema import HumanMessage, SystemMessage, AIMessage
from langchain_ollama.chat_models import ChatOllama



def main():
    load_dotenv()
    st.set_page_config(page_title="QnA Chatbot", page_icon=":robot_face:")
    st.header("HeY :wave: I am a ChatBOT! 	:left_speech_bubble: :robot_face:")
    
    chat = ChatOllama(model="llama3", temperature=0.5)
    #message history make persistent
    if "messages1" not in st.session_state:
        st.session_state["messages1"] = [
            SystemMessage(content="I am a QnA Chatbot. I love humor and reply in a funny way. Ask me anything!"),
        ]
    if "messages3" not in st.session_state:
        st.session_state["messages3"] = [
            SystemMessage(content="I am a software Engineer, I write clean code and give clear explanations. Ask me anything!"),
        ]
    def clear_text():
        st.session_state.input = st.session_state.prompt
        st.session_state.prompt = ""
        
    st.text_input("Ask me anything:", key="prompt", help="Enter you text here", on_change=clear_text)    
    tab1, tab2, tab3 = st.tabs(["Chit-chat", "Doc-chat", "Code"])
    if tab1:
        with tab1:
            input1 = st.session_state.get("input", "")
            col1, col2, col3 = st.columns([1,1,3], gap="small")
            with col1:
                st.button("Clear chats", key="clc_tab1", on_click=lambda: st.session_state.clear(), use_container_width=True) 
            with col2:   
                previous = st.button("Previous chats",key="p_tab1", use_container_width=True)
            if input1 and not previous:
                message(input1, is_user=True)
                st.session_state.messages1.append(HumanMessage(content=input1))
                with st.spinner("Thinking..."):
                    response = chat(st.session_state.messages1)
                st.session_state.messages1.append(AIMessage(content=response.content))
                message(response.content, is_user=False)
    
            input1 = ""
            #get all messages
            if previous:
                messages1 = st.session_state.get("messages1", []) 
                for i, msg in enumerate(messages1[1:]):
                    if i%2 == 0:
                        message(msg.content, is_user=True, key=str(i)+'_user_tab1')
                    else:
                        message(msg.content, is_user=False, key=str(i)+'_bot_tab1') 
            
    if tab3:
        with tab3:
            input3 = st.session_state.get("input", "")
            col1, col2, col3 = st.columns([1,1,3], gap="small")
            with col1:
                st.button("Clear chats", key="clc_tab3", on_click=lambda: st.session_state.clear(), use_container_width=True) 
            with col2:   
                previous3 = st.button("Previous chats", key="p_tab3", use_container_width=True)
            
            if input3 and not previous3:
                message(input3, is_user=True, key="user3")
                st.session_state.messages3.append(HumanMessage(content=input3))
                with st.spinner("Thinking..."):
                    response = chat(st.session_state.messages3)
                st.session_state.messages3.append(AIMessage(content=response.content))
                message(response.content, is_user=False, key="ai3")
            st.session_state.input = ""
            input3=""
            #get all messages
            if previous3:
                messages3 = st.session_state.get("messages3", []) 
                for i, msg in enumerate(messages3[1:]):
                    if i%2 == 0:
                        message(msg.content, is_user=True, key=str(i)+'_user_tab1')
                    else:
                        message(msg.content, is_user=False, key=str(i)+'_bot_tab1') 
                    
                    
                    
if __name__ == '__main__':
    main()
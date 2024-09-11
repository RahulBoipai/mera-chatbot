import streamlit as st 
from streamlit_chat import message
from dotenv import load_dotenv #use env variables

from langchain.schema import HumanMessage, SystemMessage, AIMessage
from langchain_ollama.chat_models import ChatOllama

from PyPDF2 import PdfReader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_core.prompts import ChatPromptTemplate
#from langchain.chains.combine_documents import CombineDocuments
from langchain_community.embeddings import OllamaEmbeddings
#from langchain_core.documents import create_stuff_documents_chain
#from langchain_core.document_loaders import load_text_documents
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationalRetrievalChain

def clear_text_chat():
        st.session_state.input1 = st.session_state.prompt1
        st.session_state.prompt1 = ""
def clear_text_doc():
        st.session_state.input2 =  st.session_state.prompt2
        st.session_state.prompt2 = ""
def clear_text_code():
        st.session_state.input3 =  st.session_state.prompt3
        st.session_state.prompt3 = ""


def extract_text_from_pdf(file):
    text = ""
    for pdf in file:
        pdf_reader = PdfReader(pdf)
        for page in pdf_reader.pages:
            text += page.extract_text()
    return text

def extract_text_chunks(text):
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size = 1000,
        chunk_overlap = 100,
    )
    chunks = text_splitter.split_text(text)
    return chunks

def extract_vector_store(text_chunks,embeddings):
    vectors = FAISS.from_texts(text_chunks,embeddings)
    return vectors

def get_conversation(chat,vector_store):
    memory = ConversationBufferMemory(memory_key='chat_history', return_messages=True)
    conversation_chain = ConversationalRetrievalChain.from_llm(
        llm=chat,
        retriever=vector_store.as_retriever(),
        memory=memory,
    )
    return conversation_chain   
    
        
def main():
    load_dotenv()
    st.set_page_config(page_title="QnA Chatbot", page_icon=":robot_face:")
    st.header("Hi:wave: ! Let's Chat, Learn & Laugh :robot_face:")
    
    chat = ChatOllama(model="llama3", temperature=0.5)
    #message history make persistent
    if "messages1" not in st.session_state:
        st.session_state["messages1"] = [
            SystemMessage(content="I am a QnA Chatbot. I love humor and reply in a funny way. Ask me anything!"),
        ]
    if "messages3" not in st.session_state:
        st.session_state["messages3"] = [
            SystemMessage(content="I am a software Engineer, I write simple, clean python code and give clear explanations. Ask me anything!"),
        ]
    
    if "conversation" not in st.session_state:
        st.session_state["conversation"] = None
        
    #st.text_input("Ask me anything:", key="prompt", help="Enter you text here", on_change=clear_text)    
    tab1, tab2, tab3 = st.tabs(["Chit-chat", "Doc-chat", "Code-chat"])

    with tab1:
        st.text_input("Ask me anything:", key="prompt1", help="Enter you text here", on_change=clear_text_chat)
        input1 = st.session_state.get("input1", "")
        st.session_state.input1 = ""
            
        col1, col2, col3 = st.columns([1,1,3], gap="small", vertical_alignment="center")
        with col3:
            st.write(":robot_face: :loudspeaker:")
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
        
        #get all messages
        if previous:
            messages1 = st.session_state.get("messages1", []) 
            for i, msg in enumerate(messages1[1:]):
                if i%2 == 0:
                    message(msg.content, is_user=True, key=str(i)+'_user_tab1')
                else:
                    message(msg.content, is_user=False, key=str(i)+'_bot_tab1') 
            
    with tab2:
        st.text_input("Talk with files:", key="prompt2", help="Enter you text here", on_change=clear_text_doc)
        input2 = st.session_state.get("input2", "")
        
        st.session_state.input2 = ""
        
        data = st.file_uploader("Upload a file", 
                                type=["txt", "csv", "pdf", "docx"], 
                                accept_multiple_files=True)
        col1, col2, col3 = st.columns([1,1,3add], gap="small", vertical_alignment="center")
        with col2:
            st.write(":robot_face: :books:")
        with col1:
            if st.button("Process", key="process"):
                with st.spinner("Processing..."):

                        #get pdf text
                        st.session_state.raw_text = extract_text_from_pdf(data)
                    
                        #get text chunks
                        st.session_state.text_chunks = extract_text_chunks(
                            st.session_state.raw_text
                            )
                        #create vector store
                        st.session_state.embeddings = OllamaEmbeddings(model="llama3")
                        st.session_state.vector_store = extract_vector_store(
                            st.session_state.text_chunks,
                            st.session_state.embeddings
                            )
                        #get conversation
                        st.session_state.conversation = get_conversation(
                            chat, 
                            st.session_state.vector_store
                            )
        if input2:
            with st.spinner("Thinking..."):
                response = st.session_state.conversation({'question': input2})
                st.write(":thinking_face::question::", input2)
                st.write(response["answer"])
        
        
    with tab3:
        st.text_input("Give me a problem:", key="prompt3", help="Enter you text here", on_change=clear_text_code)
        input3 = st.session_state.get("input3", "")
        st.session_state.input3 = ""
        
        col1, col2, col3 = st.columns([1,1,3], gap="small", vertical_alignment="center")
        with col3:
            st.write(":robot_face: :computer:")
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
        #get all messages
        if previous3:
            messages3 = st.session_state.get("messages3", []) 
            for i, msg in enumerate(messages3[1:]):
                if i%2 == 0:
                    message(msg.content, is_user=True, key=str(i)+'_user_tab3')
                else:
                    message(msg.content, is_user=False, key=str(i)+'_bot_tab3') 
                    
                    
                    
if __name__ == '__main__':
    main()
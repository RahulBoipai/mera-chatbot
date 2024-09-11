All the necessary dependency are in Dockerfile
build docker image
1. bash build_image.sh 

build container
2. bash start_container.sh 

activate conda env
3. conda activate chat_env

download and install ollam
4. curl -fsSL https://ollama.com/install.sh | sh

run llama3
5. ollama run llama3
run app
4. streamlit run chatbot.py

#important links
https://streamlit-emoji-shortcodes-streamlit-app-gwckff.streamlit.app/
https://python.langchain.com/v0.2/docs/integrations/providers/ollama/
https://github.com/ollama/ollama?tab=readme-ov-file

#addition package install
pip install -U langchain-community
pip install ollama
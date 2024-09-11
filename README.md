# MERA-CHAT
All the necessary dependency are in Dockerfile
## setup
run the below command in terminal with number sequence.
1. build docker image
    ```
    bash build_image.sh 
    ```

2. build container
    ```
    bash start_container.sh 
    ```

3. activate conda env
    ```
    conda activate chat_env
    ```

3. download and install ollam
    ```
    curl -fsSL https://ollama.com/install.sh | sh
    ```

4. run llama3
    ```bash
    ollama run llama3
    ```

## run app
    ```bash
    streamlit run run.py
    ```

## important links
- [streamlit-emoji](https://streamlit-emoji-shortcodes-streamlit-app-gwckff.streamlit.app/)
- [langchain-ollama](https://python.langchain.com/v0.2/docs/integrations/providers/ollama/)
- [ollama](https://github.com/ollama/ollama?tab=readme-ov-file)

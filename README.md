All the necessary dependency are in Dockerfile
## setup
run the beloow 
1. build docker image
```bash
bash build_image.sh 
```

2. build container
```bash
bash start_container.sh 
```

3. activate conda env
```bash
conda activate chat_env
 ```

3. download and install ollam
```bash
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
https://streamlit-emoji-shortcodes-streamlit-app-gwckff.streamlit.app/
https://python.langchain.com/v0.2/docs/integrations/providers/ollama/
https://github.com/ollama/ollama?tab=readme-ov-file

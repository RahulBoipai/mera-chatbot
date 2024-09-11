FROM nvidia/cuda:11.7.1-devel-ubuntu20.04

ENV DEBIAN_FRONTEND=noninteractive

WORKDIR /workspace

RUN apt-get update && apt-get install -y \
                build-essential \
                cmake \
                curl \
                g++ \
                wget \
                bzip2 \
                git \
                vim \
                tmux \
                git \
                unzip \
                libosmesa6-dev \
                libgl1-mesa-glx \
                libglfw3 \
                patchelf \
                libglu1-mesa \
                libxext6 \
                libxtst6 \
                libxrender1 \
                libxi6

RUN apt-get clean && rm -rf /var/lib/apt/lists/*

RUN curl -o ~/miniconda.sh -O https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh && \
    chmod +x ~/miniconda.sh && \
    bash ~/miniconda.sh -b -p /opt/conda && \
    rm ~/miniconda.sh

RUN apt-get update && \
    apt-get install -y mpich && \
    /opt/conda/bin/conda create -n chat_env python=3.10 && \
    /opt/conda/bin/conda init bash 

# RUN /opt/conda/envs/chat_env/bin/pip3 install 

                    
RUN apt-get install -y \
	libglib2.0-0 \
	libsm6 \
	libxrender1 \
	libfontconfig1 \
    libcudnn8 \
    libcudnn8-dev 
		
    
ENV PYTHONPATH=$PYTHONPATH:/workspace/

RUN /opt/conda/envs/chat_env/bin/pip install \
                python-dotenv\
                huggingface_hub\
                langchain\
                langchain-ollama\
                streamlit\
                langchain_community\
                langchain-huggingface\
                streamlit-chat\
                PyPDF2\
                faiss-gpu\
                faiss-cpu
                




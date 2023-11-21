## 📖 Overview

A simple chat bot that adopt Retrieval Augmented Generation (RAG). This repo contains following file:
- **simpleCrawler.py** a simple crawler to download the pdf file from give link. Feel free to modify for other media type
- **prepareVectorDb.py** this use high level API of llmaIndex to embedding & indexing all the document data for given folder. Checkout [High-Level Concepts](https://gpt-index.readthedocs.io/en/latest/getting_started/concepts.html) to understand the library. Feel free to change to any other type of available DB which integrated with llmaIndex, ex: chromadb, weaviate...
- **rockyAgent.py** not use yet. This is under implementation, a simple Agent which will be used later for adding advance feature (prompter, moderator, validator)
- **test.py** streamlit chatbot application 
- **main.py** this is also streamlit chatbot application with no knowledge base, use mainly for comparision only

## ⚡️ Quickstart
To get started follow simple steps:

1. **Setting up python environment** Ensure you have a version 3.8 or higher Python environment. Recommendation to create and activate this environment using the following commands, replacing `openAI_env` with your preferred environment name:
    ```
    conda create -n openAI_env python=3.8 -y
    conda activate openAI_env
    ```
2. **Install Dependencies:** Move into the `ChatPOC` directory and install the necessary dependencies by running:
    ```
    cd ChatPOC
    pip3 install -r requirements.txt
    ```
3. **Set OpenAI API Key:** Create file .env which contains your openAI API keys (ex: `OPENAI_API_KEY=sk-xxxyyyzzz`) ,at your home folder for ex /Users/dle, otherwise you could put .env file at your root folder and modify the load_env as following:
    ```
    dotenv_path = join(dirname(__file__), '.env')
    load_dotenv(dotenv_path)
    ```
4. **Prepare the knowledge base:** Run the crawler with command and enter website & number of page you wish to scan (for ex: 200)
    ```
    python simpleCrawler.py
    ```
    After that embed & index data by command

    ```
    python prepareVectoDb.py
    ```
    Right now the data is download to `data_ongoing` folder and the embed & index is stored in storage_ongoing. Feel free to modify as desired

5. **Run Chat bot:**: Run the chatbot with following command and enjoy! 
    ```
    streamlit run test.py
    ```
## 📬 Contact
If you have any questions, feedback, or would like to get in touch, please feel free to reach out to us via email at [dle@absolute.com](mailto:dle@absolute.com)
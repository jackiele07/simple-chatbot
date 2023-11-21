import os
import sys
from llama_index.llms import OpenAI
from llama_index.vector_stores import ChromaVectorStore
from llama_index import StorageContext, SimpleDirectoryReader, VectorStoreIndex, load_index_from_storage, ServiceContext
from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv())
import streamlit as st
st.title("ABT Rookie Bot")
data_dir = "./storage_ongoing"
# check if storage already exists
# Display loading text with a loading spinner
with st.spinner('Loading...'):
    if not os.path.exists(data_dir):
        # print error and exit
        print("Data is not ready...Exit program")
        sys.exit(1)
    else:
    # load the existing index
        storage_context = StorageContext.from_defaults(persist_dir=data_dir)
        index = load_index_from_storage(storage_context)
    st.success('Loading completed.')

service_context = ServiceContext.from_defaults(
    llm=OpenAI(model="gpt-3.5-turbo", temperature=0)
)

query_engine = index.as_query_engine(service_context=service_context,streaming=True)

from llama_index.query_engine import CitationQueryEngine
# Use citation query engine for more precise
#query_engine = CitationQueryEngine.from_args(index, similarity_top_k=3,streaming=True)

from llama_index.tools import QueryEngineTool, ToolMetadata

query_engine_tools = [QueryEngineTool(
        query_engine=query_engine,
        metadata=ToolMetadata(
            name=f"vector_index_product",
            description=(
                "useful for when you want to answer queries about Absolute company's products"
            ),
        ),
    )]

from llama_index.agent import OpenAIAgent
from llama_index.llms import OpenAI

llm = OpenAI(model="gpt-3.5-turbo-0613")
agent = OpenAIAgent.from_tools(query_engine_tools, llm=llm)

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("What is up?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        full_response = ""
        streaming_response = query_engine.query(prompt)
        #streaming_response = agent.stream_chat(prompt)
        for response in streaming_response.response_gen:
            full_response += str(response) or ""
            message_placeholder.markdown(full_response + "▌")
        message_placeholder.markdown(full_response)
    st.session_state.messages.append({"role": "assistant", "content": full_response})

# import streamlit as st
# import requests
# st.title("Echo Bot")

# # Initialize chat history
# if "messages" not in st.session_state:
#   st.session_state.messages=[]

# # Display chat messages from history on app rerun
# for message in st.session_state.messages:
#   with st.chat_message(message["role"]):
#     st.markdown(message["content"])

# def llm_call(prompt):
#     api_url = "https://api-inference.huggingface.co/models/bert-base-uncased"
#     headers = {"Authorization": "Bearer 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"}

#     data = {"inputs": prompt}

#     try:
#         response = requests.post(api_url, headers=headers, json=data)
#         response.raise_for_status()  # Raise an exception for 4xx or 5xx status codes
#         return response.json()["outputs"]
#     except requests.exceptions.RequestException as e:
#         print(f"Error: {e}")
#         return {"error": "Failed to call AI API"}
# # Replace YOUR_API_TOKEN with your actual Hugging Face API token
# # You can obtain a token by signing up for a free account on the Hugging Face website

# # React tp user input
# if prompt := st.chat_input("Hey there! What is up?"):
#   # Display user message to chat message container
#   st.chat_message("user").markdown(prompt)
#   # Add user message to chat history'
#   st.session_state.messages.append({"role": "user", "content": prompt})

#   # response=f"Echo: {prompt}"
#   response = llm_call(prompt)
#   # Display assistant response in chat message container
#   with st.chat_message("assistant"):
#     st.markdown(response)
#   # Add assistant response to chat history
#   st.session_state.messages.append({"role": "assistant", "content": response})

from openai import OpenAI
import streamlit as st

st.title("ChatGPT-like clone")

client = OpenAI(api_key="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")

if "openai_model" not in st.session_state:
    st.session_state["openai_model"] = "gpt-3.5-turbo"

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
        stream = client.chat.completions.create(
            model=st.session_state["openai_model"],
            messages=[
                {"role": m["role"], "content": m["content"]}
                for m in st.session_state.messages
            ],
            stream=True,
        )
        response = st.write_stream(stream)
    st.session_state.messages.append({"role": "assistant", "content": response})
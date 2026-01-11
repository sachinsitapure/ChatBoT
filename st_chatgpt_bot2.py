import streamlit as st
from openai import OpenAI

# Initialize OpenAI client
client = OpenAI(api_key="")

# Initialize session state for conversation history
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "system", "content": "You are a helpful assistant."}
    ]

st.title("ChatGPT Chatbot")

# Display all previous messages (except system message)
for message in st.session_state.messages[1:]:
    with st.chat_message(message["role"]):
        st.write(message["content"])

# Get user input
user_input = st.chat_input("Type your message here...")

# When user submits a message
if user_input:
    # Add user message to session state
    st.session_state.messages.append({"role": "user", "content": user_input})
    
    # Display user message
    with st.chat_message("user"):
        st.write(user_input)
    
    # Get bot response
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=st.session_state.messages
            )
            
            bot_reply = response.choices[0].message.content
            st.write(bot_reply)
            
            # Add bot reply to session state
            st.session_state.messages.append({"role": "assistant", "content": bot_reply})
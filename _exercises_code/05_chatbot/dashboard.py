import streamlit as st 
from bot import Bot

# bot = Bot()
# st.title("Chat with Ro Båt")
# st.markdown(bot.chat("Tell me a joke"))


def initialize_session_state():
    """Initialize session state variables."""
    if "messages" not in st.session_state:
        st.session_state.messages = []
    if "bot" not in st.session_state:
        st.session_state.bot = Bot()

def display_chat_messages():
    """Display chat messages from history"""
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

def handle_user_input():
    """Handle user input and generate bot response."""
    if prompt := st.chat_input("What is up?"):

        with st.chat_message("user"):
            st.markdown(prompt)

        st.session_state.messages.append({"role": "user", "content": prompt})

        bot_response = st.session_state.bot.chat(prompt)
        response = f"{bot_response}"

        with st.chat_message("assistant"):
            st.markdown(response)

        st.session_state.messages.append({"role": "assistant", "content": response})

def layout():
    """Define the layout of the Streamlit app."""
    st.title("Chatting with Totally a Human!")
    st.write("Human in a trenchcoat.")
    display_chat_messages()
    handle_user_input()

if __name__ == "__main__":
    initialize_session_state()
    layout()

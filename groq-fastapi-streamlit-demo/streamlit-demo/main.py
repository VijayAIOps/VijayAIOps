from click import prompt
import streamlit as st
import requests

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# for display chat history
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# chat input
st.title("Groq chat!")
if prompt := st.chat_input("type your message here .."):
    with st.chat_message("user"):
        st.markdown(prompt)
    with st.chat_message("assistant"):
        with st.spinner("thinking ..."):
            response = requests.post("http://localhost:8000/prompt", json={"message": prompt})
            result =response.json()
            st.markdown(result["message"])
    st.session_state.messages.append({"role": "assistant", "content": result["message"]})






def main():
    print("Hello from streamlit-demo!")


if __name__ == "__main__":
    main()

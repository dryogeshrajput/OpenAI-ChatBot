import openai
import streamlit as st

openai.api_key = "Enter OpenAI Key Here"

# Set the page configuration
st.set_page_config(page_title="OpenAI Chatbot", page_icon=":robot_face:", layout="wide", initial_sidebar_state="expanded")

st.title("OpenAI Chatbot :robot_face:")

model = "text-davinci-003"
user = st.text_input("Enter your question here:", "", key="user_input")

if user.lower() == "":
    st.write("Enter your question above")

else:
    with st.spinner(text='Thinking...'):
        completion = openai.Completion.create(model=model,
                                              prompt=user,
                                              max_tokens=1024,
                                              temperature=0.5,
                                              n=1,
                                              stop=None)
    response = completion.choices[0].text
    st.divider()  # Draws a horizontal rule
    st.write("Answer :  ", response)
    st.divider()  # Draws a horizontal rule

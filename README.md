# OpenAI-ChatBot
[85566340-fc1c-43b4-a4f3-ecac97229188.webm](https://user-images.githubusercontent.com/94129924/233358386-f7992840-30da-407e-be8c-30d0e3f8684c.webm)

# OpenAI ChatBot using OpenAI and Streamlit

# This code is a Streamlit app that uses the OpenAI API to generate responses to user questions using the text-dalle-001 model. Here's a breakdown of what each line does:

  import os: Imports the os module, which provides a way of using operating system dependent functionality like reading or writing to the file system.
  import openai: Imports the OpenAI Python package, which provides a way to interact with OpenAI's API.
  import streamlit as st: Imports the Streamlit Python package, which provides a way to build and run interactive web apps.
  openai.api_key = "Write you API Key": Sets the OpenAI API key, which is required to use the API.
  user = st.text_input("Enter your question here:", "", key="user_input"): Creates a text input box in the Streamlit app where the user can enter their question. The key   parameter is used to preserve the state of the input box across app runs.
  
  response = openai.Completion.create(...) : Sends a request to the OpenAI API to generate a response to the user's question using the text-dalle-001 model. 
  # The    temperature, max_tokens, top_p, frequency_penalty, and presence_penalty parameters are used to control the behavior of the model and the generated response.
  response2 = response.choices[0].text: Extracts the generated response from the OpenAI API response.
  st.divider(): Draws a horizontal rule in the Streamlit app.
  st.write("Answer : ", response2): Displays the generated response in the Streamlit app.
  st.divider(): Draws another horizontal rule in the Streamlit app.

# Output Screenshots:

![2](https://user-images.githubusercontent.com/94129924/232741256-9939e666-3c51-4017-b06c-cd0f654cc60d.PNG)
![3](https://user-images.githubusercontent.com/94129924/232741294-c1035de5-a58e-4c75-a2a9-24a5c66428c5.PNG)
![4](https://user-images.githubusercontent.com/94129924/232741301-85cecac8-403a-4b81-8b35-ecec287d5d3e.PNG)

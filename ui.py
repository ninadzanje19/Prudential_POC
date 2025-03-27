import streamlit as st
from main import format_prompt, retrieved_texts
from google_gemini import generate

key = 1

query = st.text_input("Enter the prompt", key=f"input{key}")
button_state = st.button("Submit", key=f"submit{key}")
final_prompt = format_prompt(query, retrieved_texts)


if button_state == True:

    response = generate(final_prompt)
    st.write(response)
    button_state = False

st.write(button_state)

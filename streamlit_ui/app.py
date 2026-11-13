# streamlit_ui/app.py

import streamlit as st
import requests

st.title("Policy Assistant")

question = st.text_input(
    "Ask Policy Question"
)

if st.button("Submit"):

    response = requests.post(
        "http://localhost:8000/ask",
        json={"question": question}
    )

    

    if response.status_code == 200:
        data = response.json()
        st.write(data["answer"])
    else:
        st.error(response.text)

    st.write(data["answer"])

    st.write("Sources:")
    st.write(data["sources"])
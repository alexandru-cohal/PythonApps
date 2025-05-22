import streamlit as st
from send_email import send_email

st.header("Contact me")

with st.form(key="contact_form"):
    form_email = st.text_input("Your email address")
    form_message = st.text_area("Your message")
    form_button_submit= st.form_submit_button("Submit")

    message_to_send = f"""\
Subject: New email from {form_email}

From: {form_email}
{form_message}
"""

    if form_button_submit:
        send_email(message_to_send)
        st.info("The message was sent!")
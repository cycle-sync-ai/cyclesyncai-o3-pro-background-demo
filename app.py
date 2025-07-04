import streamlit as st
import time
import requests
import os

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY") or st.secrets.get("OPENAI_API_KEY", "")
if not OPENAI_API_KEY:
    st.error("API key missing!")
    st.stop()

API_URL = "https://api.openai.com/v1/responses"

headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {OPENAI_API_KEY}",
    "OpenAI-Beta": "background"
}

def start_background_task(prompt):
    payload = {
        "model": "o3-pro",
        "input": prompt,
        "background": True
    }
    response = requests.post(API_URL, headers=headers, json=payload)
    response.raise_for_status()
    return response.json()["id"]

def poll_response(response_id):
    while True:
        resp = requests.get(f"{API_URL}/{response_id}", headers=headers)
        resp.raise_for_status()
        data = resp.json()
        status = data.get("status")
        if status in ["queued", "in_progress"]:
            time.sleep(2)
        elif status == "completed":
            # Adjust this according to the actual response schema
            return data['output'][0]['content'][0]['text']
        else:
            raise Exception(f"Unknown status: {status}, {data}")

st.title("OpenAI o3-pro Background Mode Demo")

prompt = st.text_area("Enter your prompt (supports very long input):", height=200)

if st.button("Generate Response"):
    if not prompt.strip():
        st.error("Please enter a prompt.")
    else:
        with st.spinner("Starting background task..."):
            try:
                response_id = start_background_task(prompt)
                st.success(f"Task started with ID: {response_id}")
                with st.spinner("Waiting for completion..."):
                    output = poll_response(response_id)
                st.subheader("Model Output:")
                st.text_area("Output", value=output, height=400)
            except Exception as e:
                st.error(f"Error: {e}")

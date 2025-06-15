import os
import time
import requests
from groq import Groq
import streamlit as st
import simplejson as json
import base64
from dotenv import load_dotenv
from streamlit_chatbox import *
from sarvam_tts.prompts import CHAT_GPT_4_LEAKED

load_dotenv()


GROQ_API_KEY = os.getenv("GROQ_API_KEY", "")
SARVAM_API_KEY = os.getenv("SARVAM_API_KEY", "")

client = Groq(
    api_key=GROQ_API_KEY
)

chat_boxes = ["chat 1", "new chat"]
messages = [
    {
        "role": "system",
        "content": CHAT_GPT_4_LEAKED
    }
]

chat_box = ChatBox(
    use_rich_markdown=True,
    user_theme="green",
    assistant_theme="blue",
)
chat_box.use_chat_name(chat_boxes[0])  # add a chat conversatoin


def on_chat_change():
    chat_box.use_chat_name(st.session_state["chat_name"])
    # restore widget values to st.session_state when chat name changed
    chat_box.context_to_session()


with st.sidebar:
    st.subheader('start to chat using streamlit')
    chat_name = st.selectbox("Chat Session:", chat_boxes,
                             key="chat_name", on_change=on_chat_change)
    chat_box.use_chat_name(chat_name)
    in_expander = st.checkbox('show messages in expander', key="in_expander")
    show_history = st.checkbox('show session state', key="show_history")
    # save widget values to chat context
    chat_box.context_from_session(exclude=["chat_name"])

    st.divider()


chat_box.init_session()
chat_box.output_messages()

if query := st.chat_input('input your question here'):
    chat_box.user_say(query)
    start_time = time.time()
    messages.append(
        {
            "role": "user",
            "content": query,
        }
    )
    chat_completion = client.chat.completions.create(
        messages=messages,
        model="llama3-8b-8192",
    )
    text = chat_completion.choices[0].message.content
    messages.append({"role": "assistant", "content": text})

    # Text to Speech (POST /text-to-speech)
    response = requests.post(
        "https://api.sarvam.ai/text-to-speech",
        headers={
            "api-subscription-key": SARVAM_API_KEY
        },
        json={
            "text": text,
            "target_language_code": "en-IN"
        },
    )

    # audio response
    audio_response = response.json()
    audio = audio_response.get("audios")[0]

    # The audio is in The output audio files in WAV format, encoded as base64 strings. Each string corresponds to one of the input texts.
    audio_data_uri = f"data:audio/wav;base64,{audio}"

    end_time = time.time()
    total_latency = "%.2f" % round((end_time - start_time), 2)
    
    
    # text, docs = llm.chat(query)
    chat_box.ai_say(
        [
            Markdown(f"{text}\n\n Total Latency: {total_latency}s", in_expander=in_expander,
                     expanded=True, title="answer"),
            Audio(audio_data_uri)
        ]
    )
    

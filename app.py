import streamlit as st
from own_agents import generate_story

st.set_page_config(page_title="AI Storyteller", page_icon="📖")

st.title("📖 AI Storyteller")

prompt = st.text_input("Story idea")
genre = st.selectbox("Genre", ["Fantasy", "Horror", "Sci-Fi", "Bedtime"])
length = st.radio("Length", ["Short", "Medium", "Long"])

if st.button("✨ Generate"):
    if not prompt:
        st.warning("Enter a prompt")
    else:
        with st.spinner("Generating..."):
            story = generate_story(prompt, genre, length)

        st.text_area("📜 Story", story, height=300)

import streamlit as st
from own_agents import generate_story

st.set_page_config(page_title="AI Storyteller", page_icon="📖")

st.title("📖 AI Storyteller")

prompt = st.text_input("Story idea")
genre = st.selectbox("Genre", ["Fantasy", "Horror", "Sci-Fi", "Bedtime"])
length = st.radio("Length", ["Short", "Medium", "Long"])

if st.button("✨ Generate"):
    if not prompt:
        st.warning("Enter a prompt")
    else:
        with st.spinner("Generating..."):
            story = generate_story(prompt, genre, length)

        st.text_area("📜 Story", story, height=300)

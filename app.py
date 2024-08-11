import streamlit as st

from src.llm_chain import get_llm_chain
from src.stuff_chain_svc import generate_summary
from src.youtube_svc import transcript_video

st.title("Youtube Loader [Transcript]")
st.text_area("Insert here a youtube url", key="yt_url_input")
st.selectbox(label="Select video language", key="video_lang", options=("en", "it", "fr", "de"), index=0)
st.selectbox(label="Select translation language", key="translation_lang", options=("en", "it"), index=0)
if st.button("Transcript"):
    yt_url = st.session_state.yt_url_input
    translation_lang = st.session_state.translation_lang
    video_lang = st.session_state.video_lang
    with st.spinner("Getting transcription ..."):
        video_transcription = transcript_video(yt_url, True, [video_lang], translation_lang)
        stuff_summary = generate_summary(get_llm_chain(), "text", video_transcription)
        with st.container(border=True):
            st.write("# Summary")
            st.write(stuff_summary)
            st.write("# Transcription")
            st.json(video_transcription)

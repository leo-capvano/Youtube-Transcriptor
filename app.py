import streamlit as st
from langchain_community.document_loaders import YoutubeLoader


def transcript_video(yt_video_url: str, add_video_info: bool, languages: list, translation: str):
    loader = YoutubeLoader.from_youtube_url(
        yt_video_url,
        add_video_info=add_video_info,
        language=languages,
        translation=translation
    )
    return loader.load()


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
        with st.container(border=True):
            st.json(video_transcription)

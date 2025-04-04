import streamlit as st
from summarizer.summarizer import generate_summary
from transcriber.transcriber import transcribe_audio

st.title("🧠 Brief Buddy")

input_type = st.radio("Choose input type", ("Text", "PDF (coming soon)", "Audio"))

if input_type == "Text":
    user_input = st.text_area("Paste meeting text here:")
    if st.button("Summarize"):
        summary = generate_summary(user_input)
        st.subheader("Summary:")
        st.write(summary)

elif input_type == "Audio":
    audio_file = st.file_uploader("Upload audio file", type=["mp3", "wav", "m4a"])
    if audio_file and st.button("Transcribe & Summarize"):
        with open("temp_audio.wav", "wb") as f:
            f.write(audio_file.read())
        text = transcribe_audio("temp_audio.wav")
        st.subheader("Transcribed Text:")
        st.write(text)
        summary = generate_summary(text)
        st.subheader("Summary:")
        st.write(summary)
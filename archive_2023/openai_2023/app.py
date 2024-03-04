import streamlit as st
from dotenv import load_dotenv

load_dotenv()

from streamlit.runtime.uploaded_file_manager import UploadedFile

import text_to_speech as tts
from explainer import retrieve_code_explanation, retrieve_code_language

TTS_ENABLED = False


def display_header() -> None:
    st.image("img/logo.png")
    st.title("Wlecome to AI-rjan Code Explainer")
    st.text("Just upload your code or copy and paste in the field below")
    st.warning("Warning: uploaded files have precedence on copied and pasted code.")


def display_widgets() -> tuple[UploadedFile, str]:
    _file = st.file_uploader("Upload your script here.")
    text = st.text_area("or copy and paste your code here (press Ctrl + Enter to send)")

    if not (text or _file):
        st.error("Supply your code with one of the options from above.")

    return _file, text


def retrieve_content_from_file(file: UploadedFile) -> str:
    return file.getvalue().decode("utf8")


def extract_code() -> str:
    uploaded_script, pasted_code = display_widgets()

    if uploaded_script:
        return retrieve_content_from_file(uploaded_script)
    return pasted_code or ""


def choose_voice():
    voices = tts.list_available_names()
    return st.selectbox("Choose a voice", voices)


def main() -> None:
    display_header()

    selected_voice = choose_voice()

    code_to_explain = extract_code()

    if not code_to_explain:
        return

    with st.spinner(text="Let me think for a while..."):
        language = retrieve_code_language(code=code_to_explain)
        explanation = retrieve_code_explanation(code=code_to_explain)

    if TTS_ENABLED:
        with st.spinner(text="Give me a little bit more time, this code is complex..."):
            tts.convert_text_to_mp3(message=language, voice_name=selected_voice, mp3_filename="language.mp3")

        with st.spinner(text=("I've got the language! I'm thinking about how to explain to you in a few words now...")):
            tts.conver_text_to_mp3(message=explanation, voice_name=selected_voice, mp3_filename="explanation.mp3")

    st.success("Uhg, that was hard! But here is your explanation")
    if TTS_ENABLED:
        st.warning("Remember to turn on your audio!")

    st.markdown(f"**Language:** {language}")
    if TTS_ENABLED:
        st.audio("language.mp3")

    st.markdown(f"**Explanation:** {explanation}")
    if TTS_ENABLED:
        st.audio("explanation.mp3")


if __name__ == "__main__":
    main()

import streamlit as st
from io import BytesIO
from app.main import MusicLLM
from app.utils import *
from dotenv import load_dotenv

load_dotenv()


st.set_page_config(page_title = "AI Music Composer", layout = "centered")
st.title("AI Music Composer")
st.markdown("Generate AI Music by describing the style and content")

music_input = st.text_input("Describe the muic you want to compose")
style = st.selectbox("Choose a style", ["Sad", "Happy", "Jazz", "Romantic", "Extreme"])

if st.button("Generate Music") and music_input:

    generator = MusicLLM()

    with st.spinner("Generating Music"):

        melody = generator.generate_melody(music_input)
        harmony = generator.generate_harmony(melody)
        rhythm = generator.generate_rythm(melody)

        composition = generator.adapt_style(style, melody, harmony, rhythm)

        melody_notes = melody.split()
        melody_freqs = note_to_frequncies(melody)

        harmony_chords = harmony.split()
        harmony_notes = []

        for chord in harmony_chords:
            harmony_notes.extend(chord.split('-'))

        harmony_freqs = note_to_frequncies(harmony_notes)

        all_freqs = melody_freqs + harmony_freqs

        wav_bytes = generate_wav_bytes_fron_notes(all_freqs)

    st.audio(BytesIO(wav_bytes))

    st.success("Music generated successfully...")

    with st.expander("Composition Summary"):
        st.text(composition)
    
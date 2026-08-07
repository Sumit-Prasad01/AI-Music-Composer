# AI Music Composer

AI Music Composer is a Streamlit app that turns a text description into a simple generated music sketch. It uses Groq-hosted LLM calls to create a melody, harmony, rhythm description, and a style summary, then converts the note data into a WAV audio stream for playback in the browser.

## What this repository actually contains

- A Streamlit UI in `app.py`
- LLM orchestration in `app/main.py`
- Note-to-frequency and WAV helper functions in `app/utils.py`
- Python packaging metadata in `setup.py`
- Dependency list in `requirements.txt`

The repository also includes `Dockerfile` and `kubernetes-deployment.yaml`, but both are currently empty placeholders.

## Features

- Text prompt input for music description
- Style selector: Sad, Happy, Jazz, Romantic, Extreme
- Melody generation through Groq chat completions
- Harmony generation from the generated melody
- Rhythm suggestion from the generated melody
- Conversion of note names into frequencies
- WAV synthesis and in-browser audio playback
- Generated composition summary shown in the UI

## How it works

1. The user enters a music description in the Streamlit UI.
2. The app sends prompts to Groq using `langchain_groq.ChatGroq`.
3. The model generates:
   - a melody as space-separated notes
   - harmony chords as dash-separated note groups
   - rhythm durations
   - a style-adapted summary
4. `music21` converts note names into frequencies.
5. `synthesizer` and `scipy` are used to build a WAV buffer.
6. Streamlit plays the generated audio in the browser.

Important detail: the audio generation currently uses the melody and harmony notes. The rhythm string is generated and included in the summary, but it is not used directly in the WAV synthesis path.

## Project structure

```text
.
├── app/
│   ├── __init__.py
│   ├── main.py          # Groq + LangChain music generation logic
│   └── utils.py         # Note parsing and WAV synthesis helpers
├── app.py               # Streamlit frontend
├── requirements.txt
├── setup.py
├── Dockerfile           # Empty placeholder
├── kubernetes-deployment.yaml  # Empty placeholder
└── README.md
```

## Prerequisites

- Python 3.10+ recommended
- A Groq API key

## Installation

Clone the repository:

```bash
git clone https://github.com/Sumit-Prasad01/AI-Music-Composer.git
cd Music-Composer-AI
```

Create and activate a virtual environment:

```bash
python -m venv .venv
.venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

If you want to install the package in editable mode:

```bash
pip install -e .
```

## Environment variables

Create a `.env` file in the project root and set:

```env
GROQ_API_KEY=your_groq_api_key_here
```

The app loads environment variables with `python-dotenv`.

## Run the app

Start the Streamlit app from the project root:

```bash
streamlit run app.py
```

Then open the local URL shown by Streamlit, usually:

```text
http://localhost:8501
```

## Usage

1. Enter a short description of the music you want.
2. Choose a style.
3. Click “Generate Music”.
4. Wait for the model and synthesis pipeline to finish.
5. Listen to the generated audio and inspect the composition summary.

## Dependencies used by the code

- `streamlit` for the UI
- `langchain` / `langchain_groq` / `langchain_core` for prompt chaining
- `music21` for note parsing and pitch conversion
- `numpy` and `scipy` for audio array and WAV writing
- `synthesizer` for waveform generation
- `python-dotenv` for environment loading

## Current limitations

- The generated output is a short synthesized sketch, not a full music production pipeline.
- Rhythm is not yet applied directly to the waveform generation.
- The deployment files are present but not implemented.
- The app depends on an external Groq API key and network access.

## Notes for maintainers

- There are a few typos in code-level names such as `generate_rythm`, `note_to_frequncies`, and `generate_wav_bytes_fron_notes`. They work as written because the code calls the same names consistently, but they should be cleaned up if the project is being refactored.
- If you add deployment support, update this README to document the real Docker and Kubernetes workflow instead of the current placeholders.


# Sarvam TTS Streamlit Chatbot

This is a Streamlit web application that demonstrates a real-time chatbot with text-to-speech capabilities. The application uses the Groq API for fast language model inference and the Sarvam AI API for text-to-speech conversion.

## Features

- **Real-time Chat**: Engage in a conversation with a large language model (Llama 3 8B).
- **Text-to-Speech**: The assistant's text responses are converted to speech using Sarvam AI.
- **Audio Playback**: The generated audio is embedded directly into the chat interface for easy playback.
- **Latency Calculation**: The application measures and displays the total latency from sending a query to receiving the audio response.
- **Chat History**: Supports multiple, selectable chat sessions.

## Setup and Installation

Follow these steps to set up and run the project locally.

### 1. Clone the Repository

```bash
git clone <repository-url>
cd sarvam-tts
```

### 2. Create a Virtual Environment

It's recommended to use a virtual environment to manage dependencies. Poetry can handle this for you.

### 3. Install Dependencies

Install the required Python packages using Poetry.

```bash
poetry install
```

### 4. Set Up Environment Variables

The application requires API keys for Groq and Sarvam AI. Create a `.env` file in the root of the project directory and add your keys:

```
GROQ_API_KEY="your_groq_api_key"
SARVAM_API_KEY="your_sarvam_api_key"
```

## Usage

To run the Streamlit application, execute the following command in your terminal. It's best to run this within the Poetry shell.

```bash
poetry run streamlit run sarvam_tts/app.py
```

This will start the local Streamlit server, and you can access the application in your web browser at `http://localhost:8501`.

## Core Libraries

- **Streamlit**: For building the interactive web application.
- **Groq**: Provides the fast LLM API.
- **Sarvam AI**: Provides the text-to-speech API.
- **streamlit-chatbox**: A custom Streamlit component for creating a chat UI.

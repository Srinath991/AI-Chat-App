# AI Chat Application

This is a FastAPI-based web application that provides a chat interface powered by Google's Gemini AI model through LangChain.

## Prerequisites

- Python 3.11 or higher
- Google Cloud API key for Gemini AI
- uv package manager (recommended)

## Setup

1. Clone the repository:
```bash
git clone https://github.com/Srinath991/AI-Chat-App
cd AI-Chat-App
```

2. Create and activate a virtual environment:
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows, use `.venv\Scripts\activate`
```

3. Install dependencies using uv:
```bash
# Install uv if you haven't already
pip install uv

# Install project dependencies
uv pip install -e .
```

4. Set up your Google Cloud API key:
   - Get your API key from the Google Cloud Console
   - Set it as an environment variable:
```bash
export GOOGLE_API_KEY="your-api-key-here"  # On Windows, use `set GOOGLE_API_KEY=your-api-key-here`
```

## Running the Application

1. Start the development server:
```bash
python main.py
```

2. Open your web browser and navigate to:
```
http://127.0.0.1:8000
```

The application will be running in development mode with hot-reload enabled.

## Project Structure

- `main.py` - Main application file containing FastAPI routes and AI integration
- `templates/` - Directory containing HTML templates
- `static/` - Directory for static files (CSS, JavaScript, images)
- `pyproject.toml` - Project dependencies and metadata

## Dependencies

- FastAPI - Web framework
- LangChain - AI/LLM framework
- Google Generative AI - AI model provider
- Uvicorn - ASGI server
- Jinja2 - Template engine

## Features

- Real-time chat interface
- Integration with Google's Gemini AI model
- Conversation memory for context-aware responses
- Modern web interface

## Development

The application uses FastAPI's hot-reload feature, so any changes to the code will automatically restart the server.


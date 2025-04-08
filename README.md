# Jivani FastAPI Backend

A FastAPI backend service that uses a fine-tuned T5 model for natural language command interpretation.

## Setup

1. Create a virtual environment:
```cmd
python -m venv .venv
.venv\Scripts\activate
```

2. Install dependencies:
```cmd
pip install fastapi transformers torch uvicorn
```

## Running the Application

Start the FastAPI server:
```cmd
python -m uvicorn main:app --reload
```

The server will be available at `http://127.0.0.1:8000`

## API Endpoints

### GET /
Health check endpoint that returns application name.

### POST /interpret-command
Interprets natural language commands and returns structured event data.

**Request Body:**
- `command`: string (natural language command)

**Example Request:**
```json
{
    "command": "Plan an event titled John's birthday party and details Organize a small get-together at home priority High and date 2025-05-10 under Social category"
}
```

**Example Response:**
```json
{
    "action": "create_event",
    "title": "John's birthday party",
    "description": "Organize a small get-together at home",
    "priority": "High",
    "date": "2025-05-10",
    "classification": "Social"
}
```

## Model Information
The application uses a fine-tuned T5 model located in the `./t5` directory for natural language processing.
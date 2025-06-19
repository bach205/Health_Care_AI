# Medical RAG System

A Retrieval-Augmented Generation (RAG) system for medical question answering, built with Python and FastAPI.

## Project Structure

```
HEALTH_CARE_AI/
│
├── src/                           # Source code
│   ├── crawler/                   # Data crawling
│   ├── rag_engine/               # RAG implementation
│   ├── server/                   # FastAPI server
│   └── client/                   # Client applications
│
├── data/                         # Data storage
├── models/                       # Model storage
├── vector_store/                # Vector database
└── notebooks/                   # Jupyter notebooks
```

## Setup

1. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Set up environment variables:
```bash
cp .env.example .env
# Edit .env with your configuration
```

## Running the Application

1. Start the FastAPI server:
```bash
cd src/server
uvicorn main:app --reload
```

2. Access the API documentation at `http://localhost:8000/docs`

## Features

- Medical data crawling from multiple sources
- RAG-based question answering
- RESTful API interface
- Vector store for efficient retrieval
- Support for multiple medical websites

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

MIT License 
# RAG AI Assistant

A Retrieval-Augmented Generation (RAG) based AI assistant that can answer questions based on custom document collections. This project implements a powerful AI assistant that combines document retrieval with generative AI to provide accurate and context-aware responses.

## Features

- **Document Processing**: Supports multiple document formats (PDF, TXT)
- **Semantic Search**: Utilizes FAISS for efficient vector similarity search
- **RAG Pipeline**: Combines document retrieval with OpenAI's GPT models
- **Web Interface**: Simple and intuitive user interface
- **Environment Configuration**: Secure API key management
- **Modular Architecture**: Easy to extend and customize

## Project Structure

```
rag_ai_assistant/
│
├── app/
│   ├── main.py              # Main application entry point
│   ├── config.py            # Configuration settings
│   ├── models.py            # Data models
│   ├── rag_pipeline.py      # RAG pipeline implementation
│   ├── utils.py             # Utility functions
│   └── dependencies.py      # Dependency management
│
├── data/
│   └── documents/           # Place your .txt/.pdf files here
│
├── vectorstore/
│   └── faiss_index/         # FAISS index storage
│
├── frontend/
│   └── index.html           # Simple frontend UI
│
├── .env                     # Environment variables
├── .gitignore
├── requirements.txt
└── README.md
```

## Prerequisites

- Python 3.8 or higher
- OpenAI API key
- Git

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/kulindupr/Ai-Assistant-Rag.git
   cd Ai-Assistant-Rag
   ```

2. Create and activate a virtual environment:
   ```bash
   # On Windows
   python -m venv venv
   venv\Scripts\activate

   # On macOS/Linux
   python -m venv venv
   source venv/bin/activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Create a `.env` file in the root directory and add your OpenAI API key:
   ```
   OPENAI_API_KEY=your_api_key_here
   ```

## Usage

1. Place your documents in the `data/documents` directory. Supported formats:
   - Text files (.txt)
   - PDF files (.pdf)

2. Start the application:
   ```bash
   python app/main.py
   ```

3. Access the web interface at `http://localhost:8000`

4. Upload documents and start asking questions!

## API Endpoints

- `POST /upload`: Upload documents
- `POST /ask`: Ask questions to the AI assistant
- `GET /`: Access the web interface

## Dependencies

- openai>=1.0.0
- langchain>=0.1.0
- langchain-community>=0.0.10
- faiss-cpu>=1.7.4
- python-dotenv>=1.0.0
- fastapi>=0.100.0
- uvicorn>=0.23.0
- pydantic>=2.0.0
- python-multipart>=0.0.6
- google-generativeai>=0.3.0
- jinja2>=3.1.0

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- OpenAI for their powerful language models
- LangChain for the RAG framework
- FAISS for efficient similarity search
- FastAPI for the web framework

## Contact

For any questions or suggestions, please open an issue in the GitHub repository. 
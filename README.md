# 🎥 YouTube Chat Extension with RAG

Chat with any YouTube video's transcript directly from your browser using a Chrome Extension powered by Retrieval-Augmented Generation (RAG).

## 🚀 Features

* 🎬 Detects the currently open YouTube video automatically.
* 📝 Fetches the video's transcript.
* ✂️ Splits the transcript into semantic chunks.
* 🧠 Generates embeddings using Hugging Face embeddings.
* 📚 Stores embeddings in Qdrant Vector Database.
* 🔍 Retrieves the most relevant transcript chunks for each query.
* 🤖 Uses Groq Llama 3.3 70B to generate accurate, context-aware answers.
* 🧩 Chrome Extension (Manifest V3) for a seamless user experience.
* ⚡ Automatically indexes videos before answering questions.

---

## 📸 Demo

Uploading 2026-07-25 16-32-00.mp4…

Or add a link to your LinkedIn demo post here.

---

## 🏗️ Architecture

```text
                 YouTube Video
                        │
                        ▼
              Chrome Extension
                        │
                        ▼
            Extract Current Video ID
                        │
                        ▼
            FastAPI Backend (/index)
                        │
                        ▼
             YouTube Transcript API
                        │
                        ▼
                Document Chunking
                        │
                        ▼
             HuggingFace Embeddings
                        │
                        ▼
              Qdrant Vector Database
                        │
                        ▼
             Retriever (Similarity Search)
                        │
                        ▼
               Groq Llama 3.3 70B
                        │
                        ▼
             Response in Chrome Popup
```

---

## 🛠️ Tech Stack

### Backend

* FastAPI
* LangChain
* Qdrant
* HuggingFace Embeddings (`BAAI/bge-small-en-v1.5`)
* Groq API
* YouTube Transcript API

### Frontend

* Chrome Extension (Manifest V3)
* HTML
* CSS
* JavaScript

---

## 📂 Project Structure

```text
youtube-chat/
│
├── backend/
│   ├── api/
│   ├── chains/
│   ├── ingestion/
│   ├── Retrieval/
│   ├── services/
│   ├── app.py
│   └── requirements.txt
│
└── extension/
    ├── manifest.json
    ├── popup.html
    ├── popup.css
    ├── popup.js
    ├── content.js
    ├── background.js
    └── icons/
```

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/<your-username>/<your-repository>.git
cd <your-repository>
```

---

### 2. Backend Setup

```bash
cd backend

python -m venv .venv
```

#### Windows

```bash
.venv\Scripts\activate
```

#### Linux / macOS

```bash
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

### 3. Configure Environment Variables

Create a `.env` file inside the `backend` folder.

```env
GROQ_API_KEY=your_groq_api_key
```

---

### 4. Start Qdrant

Example using Docker:

```bash
docker run -p 6333:6333 qdrant/qdrant
```

---

### 5. Run the Backend

```bash
uvicorn app:app --reload
```

The API will be available at:

```
http://127.0.0.1:8000
```

Swagger documentation:

```
http://127.0.0.1:8000/docs
```

---

## Chrome Extension Setup

1. Open Chrome.
2. Navigate to:

```
chrome://extensions
```

3. Enable **Developer Mode**.
4. Click **Load unpacked**.
5. Select the `extension` folder.

The extension is now ready to use.

---

## How It Works

1. Open any YouTube video.
2. Click the extension.
3. The extension automatically detects the current video.
4. The backend indexes the transcript (only once).
5. Ask questions about the video.
6. The system retrieves the most relevant transcript chunks.
7. The LLM answers using only the retrieved context.

---

## Example Questions

* Summarize this interview.
* What are the main topics discussed?
* What are the founding tenets of DeepMind?
* What did the speaker say about reinforcement learning?
* Explain the key ideas mentioned in the video.

---

## API Endpoints

### Index Transcript

```
POST /index
```

```json
{
  "video_id": "VIDEO_ID"
}
```

---

### Chat

```
POST /chat
```

```json
{
  "video_id": "VIDEO_ID",
  "question": "Your question here"
}
```

---

## Future Improvements

* Streaming responses
* Conversation memory
* Markdown rendering
* Automatic caching
* Better transcript chunking
* Support for multiple LLM providers
* Support for webpages and PDF documents

---

## Contributing

Contributions, suggestions, and improvements are welcome. Feel free to open an issue or submit a pull request.

---

## License

This project is licensed under the MIT License.

---

## Acknowledgements

* LangChain
* FastAPI
* Qdrant
* Hugging Face
* Groq
* YouTube Transcript API

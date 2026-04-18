# 🎓 RAG-Based AI Teaching Assistant


## 🚀 Project Overview

An end-to-end **Retrieval-Augmented Generation (RAG)** pipeline that converts video content into an intelligent AI assistant capable of answering questions based on your own data.

---

## 🧠 How It Works (Pipeline)

```
Videos → MP3 → JSON → Chunking → Merging → Embeddings → Retrieval → LLM Response
```

---

## 📂 Folder Structure

```
RAG based AI/
│
├── videos/              # Input video files
├── mp3/                 # Converted audio files
├── jsons/               # Raw transcript chunks
├── new_jsons/           # Merged chunks
├── embeddings/          # Vector data (joblib/pickle)
│
├── scripts/
│   ├── video_to_mp3 Converter.py
│   ├── mp3 to text converter.py
│   ├── merge_chunks.py
│   ├── json_to_vectors.py
    ├── Model_loader.py
│  
│    
│  
│
└── README.md
```

---

## ⚙️ Tech Stack

* 🐍 Python
* 🧠 Sentence Transformers (MiniLM)
* 🤖 Ollama (llama3.2)
* 📦 Joblib / Pickle
* 🔎 Cosine Similarity
* 📄 JSON Processing


---

## 🪜 Step-by-Step Usage Guide

### 🔹 Step 1: Add Your Videos

Place all your video files inside the `videos/` folder.

---

### 🔹 Step 2: Convert Videos → MP3

```bash
python video to mp3 converter.py
```

---

### 🔹 Step 3: Convert MP3 → JSON (Transcription)

```bash
python mp3 to text converter.py
```

---

### 🔹 Step 4: Merge Chunks (Better Context)

```bash
python merge_chunks.py
```

---

### 🔹 Step 5: Convert JSON → Embeddings

```bash
python json_file to vectors.py
```

---

### 🔹 Step 6: Run the AI Assistant

```bash
ollama serve
python Model_loader.py
```

---

## 💡 How It Answers Queries

1. User enters a query
2. Query → embedding
3. Compared with stored vectors
4. Top relevant chunks retrieved
5. Context + Query sent to LLM
6. Final answer generated 🎯

---

## 🧪 Example Use Case

> Query: *"Explain how websites work"*

✔ Retrieves relevant transcript chunks
✔ Feeds context to LLM
✔ Generates structured explanation

---

## ⚠️ Requirements

* Python 3.9+
* Ollama installed

Pull model:

```bash
ollama run llama3.2
```

---

## 📌 Key Features

* ✅ Works on your own data
* ✅ Context-aware answers
* ✅ Timestamp-based retrieval
* ✅ Modular pipeline
* ✅ Scalable architecture

---

## 🚀 Future Improvements

* Chat-style UI
* Video timestamp jump
* Hybrid search (BM25 + Vector)
* Multilingual support


---

## 👨‍💻 Author
Bhuvnesh Wahi

Built as part of hands-on learning in **RAG Systems & AI Development**

---

## ⭐ Final Note

> "Your data + LLM = Powerful AI Assistant"
Bhuvnesh Wahi

Independently developed as part of hands-on learning in RAG Systems, LLMs, and AI Development.
---

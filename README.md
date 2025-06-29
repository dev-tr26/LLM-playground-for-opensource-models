Sure! Here's a concise and honest `README.md` for your open-source multi-model LLM playground:

---

````markdown
# 🧠 Multi-Model LLM Playground

A simple open-source playground for experimenting with multiple Hugging Face-hosted open-source language models across different NLP tasks like chatting, summarization, question answering, and paraphrasing.

## ✨ Features

- 🔄 **Switch between models** from Hugging Face (e.g., Mistral, Zephyr, Phi-3, etc.)
- 🧩 **Choose tasks** such as:
  - Chat (instruction following)
  - Summarization
  - Q&A (with context)
  - Paraphrasing
- 🎛️ **Adjust creativity** (temperature slider) to control model response style
- 🧠 **Prompt templating** via LangChain for different task formats
- 🧪 Built with **Streamlit** for a lightweight and interactive UI

## 🚀 Getting Started

1. **Clone this repo:**

   ```bash
   git clone https://github.com/yourusername/llm-playground.git
   cd llm-playground
````

2. **Install dependencies:**

   It's recommended to use a virtual environment:

   ```bash
   pip install -r requirements.txt
   ```

3. **Set your Hugging Face token:**

   Create a `.env` file:

   ```env
   HF_TOKEN=your_huggingface_token
   ```

4. **Run the app:**

   ```bash
   streamlit run main.py
   ```

## 🧰 Models Included

This app currently supports the following Hugging Face models:

* 'mistralai/Mistral-7B-Instruct-v0.1'
* 'HuggingFaceH4/zephyr-7b-beta'
* 'tiiuae/falcon-7b-instruct'
* 'MiniMaxAI/MiniMax-M1-80k'
* 'microsoft/DialoGPT-medium'
* 'microsoft/Phi-3-mini-4k-instruct'
* 'google/flan-t5-base'

> You can easily modify `main.py` to add or remove models.

## ⚠️ Limitations

* No local model support (everything is routed via Hugging Face Inference API).
* Performance and availability depend on Hugging Face model hosting.
* Not optimized for high throughput or production usage.
Feel free to contribute or fork the repo to extend functionality!


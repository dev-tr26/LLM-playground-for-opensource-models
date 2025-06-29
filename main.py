import streamlit as st
from llm_config import get_hf_llm
from langchain.prompts import PromptTemplate

# ---------------- UI CONFIG ------------------
st.set_page_config(page_title="🧠 Multi-Model LLM Playground")
st.title("🧠 Multi-Model LLM Chat App")

# ---------------- Sidebar Settings ------------
st.sidebar.header("Model & Creativity Settings")

# Updated model list with more reliable chat models
model_name = st.sidebar.selectbox("Choose HF Model", [
    "microsoft/Phi-3-mini-4k-instruct",
    "mistralai/Mistral-7B-Instruct-v0.1", 
    "HuggingFaceH4/zephyr-7b-beta",
    "tiiuae/falcon-7b-instruct",
    "microsoft/DialoGPT-medium",
    'MiniMaxAI/MiniMax-M1-80k',
    "google/flan-t5-base"
])

creativity_level = st.sidebar.slider("Creativity Level (Temperature)", 0.0, 1.5, 0.7, 0.05)
max_tokens = st.sidebar.slider("Max New Tokens", 100, 1000, 512, 50)

# ---------------- Prompt Templates ------------
prompt_templates = {
    "Chat": PromptTemplate.from_template("You are a helpful assistant. Answer: {user_input}"),
    "Summarization": PromptTemplate.from_template("Please summarize the following text:\n\n{user_input}"),
    "Q&A": PromptTemplate.from_template("Context: {context}\n\nQuestion: {user_input}\nAnswer:"),
    "Paraphrase": PromptTemplate.from_template("Rephrase the following sentence in a more clear way:\n\n{user_input}"),
}

task = st.selectbox("Select Task", list(prompt_templates.keys()))

# ---------------- Input UI --------------------
user_input = st.text_area("Enter your input", height=100)

context = ""
if task == "Q&A":
    context = st.text_area("Enter context for your question", height=100)

# ---------------- Generate Button ----------------
if st.button("Generate"):
    if not user_input.strip():
        st.error("Please enter some input text.")
    elif task == "Q&A" and not context.strip():
        st.error("Please provide context for the Q&A task.")
    else:
        with st.spinner("Generating..."):
            try:
                # Load LLM
                llm = get_hf_llm(model_name, creativity_level, max_tokens)
                
                # Prepare prompt
                template = prompt_templates[task]
                if task == "Q&A":
                    final_prompt = template.format_prompt(user_input=user_input, context=context).to_string()
                else:
                    final_prompt = template.format_prompt(user_input=user_input).to_string()

                # Invoke LLM
                response = llm.invoke(final_prompt)

                st.markdown("### ✅ Response")
                st.write(response.content)
                
                # Show the actual prompt used (for debugging)
                with st.expander("View Prompt Used"):
                    st.code(final_prompt)
                    
            except Exception as e:
                st.error(f"Error generating response: {str(e)}")
                st.info("Try selecting a different model or check your HuggingFace token.")
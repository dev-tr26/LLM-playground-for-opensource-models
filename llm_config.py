from dotenv import load_dotenv
from langchain_huggingface import ChatHuggingFace
from langchain_huggingface import HuggingFaceEndpoint
import os


load_dotenv()
hf_token = os.getenv("HF_TOKEN")

def get_hf_llm(model_name: str, creativity_level:float, max_tokens: int = 512):
    try:
        llm = HuggingFaceEndpoint(
            repo_id=model_name,
            huggingfacehub_api_token=hf_token,
            temperature=creativity_level,
            max_new_tokens=max_tokens,
        )
        llm = ChatHuggingFace(llm=llm)
        return llm
    except Exception as e:
        raise Exception(f"Failed to initialize model {model_name}: {str(e)}")

    
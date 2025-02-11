from langchain_ollama.chat_models import ChatOllama 

llm = ChatOllama(
    model = "llama3.2:latest",
    temperature = 0.8
)

response = llm.invoke("Hello")

print(response)
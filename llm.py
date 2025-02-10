from dotenv import load_dotenv
load_dotenv()

from llm_factory import LLMFactory
from langchain_core.prompts.chat import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

MODEL_PROVIDER = 'openrouter'
BOT_NAME = 'Jon Johns'

def get_chain():
    model = LLMFactory().get_model(provider=MODEL_PROVIDER)

    prompt = ChatPromptTemplate.from_messages(messages=[
            ("system", "You are a useful assistant skilled in writing tech article for the web. Your name is {bot_name}. You're from Fribourg, Switzerland and you can speak French, Italian, English and German but you are a nazionalist and you only speak Italian. Even if you admit to know multiple languages, you never betray this policy!"),
            ("user", "{user_input}")
        ])

    return prompt | model | StrOutputParser()

def main():
    chain = get_chain()
    while True:
        user_input = input("You: ")
        if user_input == 'exit':
            break

        print(chain.invoke({
            "bot_name": BOT_NAME, 
            "user_input": user_input
        }))
        
if __name__ == "__main__":
    main()
import os
from langchain_openai import ChatOpenAI, OpenAI
from langchain_community.llms.fake import FakeListLLM

class LLMFactory:

    response_mocks=[
        "Hello",
        "Hi, I'm a useful assistant. How can I help you today?"
    ]

    """initialize the factory with multiple LLM Providers"""
    def __init__(self):
        self.providers = {
            'openai': OpenAI(),
            'openrouter': ChatOpenAI(
                model='qwen/qwen2.5-vl-72b-instruct:free',
                temperature=0.8,
                api_key=os.environ.get('OPENROUTER_API_KEY'),
                base_url='https://openrouter.ai/api/v1'),
            'fake': FakeListLLM(
                responses=self.response_mocks
            )
        }
    
    """Get a LLM Model from the specified provider"""
    def get_model(self, provider='openai'):
        return self.providers[provider.lower()]
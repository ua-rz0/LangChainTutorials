import getpass
import os

try:
    # load environment variables from .env file (requires `python-dotenv`)
    from dotenv import load_dotenv

    load_dotenv()
except ImportError:
    pass

os.environ["LANGSMITH_TRACING"] = "true"
if "LANGSMITH_API_KEY" not in os.environ:
    os.environ["LANGSMITH_API_KEY"] = getpass.getpass(
        prompt="Enter your LangSmith API key (optional): "
    )
if "LANGSMITH_PROJECT" not in os.environ:
    os.environ["LANGSMITH_PROJECT"] = getpass.getpass(
        prompt='Enter your LangSmith Project Name (default = "default"): '
    )
    if not os.environ.get("LANGSMITH_PROJECT"):
        os.environ["LANGSMITH_PROJECT"] = "default"
    
if not os.environ.get("OPENAI_API_KEY"):
  os.environ["OPENAI_API_KEY"] = getpass.getpass("Enter API key for OpenAI: ")

from langchain.chat_models import init_chat_model
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_core.prompts import ChatPromptTemplate

def main():
    # Initialize the model
    model = init_chat_model("gpt-4o-mini", model_provider="openai")
    
    print("=== Testing Basic Translation ===")
    # Test 1: Basic translation
    messages = [
        SystemMessage("Translate the following from English into Italian"),
        HumanMessage("hi!"),
    ]
    
    response = model.invoke(messages)
    print(f"Translation: {response.content}")
    
    print("\n=== Testing Streaming ===")
    # Test 2: Streaming response
    for token in model.stream(messages):
        print(token.content, end="")
    print()
    
    print("\n=== Testing Prompt Template ===")
    # Test 3: Using prompt template
    system_template = "Translate the following from English into {language}, reply like a rapper"
    
    prompt_template = ChatPromptTemplate.from_messages(
        [("system", system_template), ("user", "{text}")]
    )
    
    prompt = prompt_template.invoke({"language": "Hindi", "text": "hi! My name is Upasana"})
    
    response = model.invoke(prompt)
    print(f"Rapper translation: {response.content}")
    
    print("\n✅ All tests completed successfully!")

if __name__ == "__main__":
    main() 
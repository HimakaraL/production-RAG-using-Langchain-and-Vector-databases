from dotenv import load_dotenv
load_dotenv()

from langchain_openai import ChatOpenAI
from langchain_anthropic import ChatAnthropic

def main():
    
    # test OpenAI
    llm= ChatOpenAI(model_name="gpt-4o-mini", temperature=0)
    response = llm.invoke("What is the capital of France?")
    print(f"Response from OpenAI: {response.content}")

    #test Anthropic
    llm_anthropic = ChatAnthropic(model="claude-2", temperature=0)
    response_anthropic = llm_anthropic.invoke("What is the capital of Iran?")
    print(f"Response from Anthropic: {response_anthropic.content}")

    print("Setup complete!")

if __name__ == "__main__":
    main()

from langchain_community.llms import Ollama

def main():
    llm = Ollama(model="llama3")
    response = llm.invoke("What is the capital of France?")
    print(response)

if __name__ == "__main__":
    main()
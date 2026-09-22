import os

from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_ollama import ChatOllama
from langchain_openai import ChatOpenAI

load_dotenv()


def main() -> None:
    print("Hello from langchain-course!")
    print("Current working directory:", os.environ.get("OPENAI_API_KEY"))

    information = """
    LangChain is a software framework that helps facilitate the integration of large 
    language models into applications. As a language model integration framework, LangChain's use-cases largely overlap with those of language models in general, including document analysis and summarization, 
    chatbots, and code analysis."""

    summary_template = "Given the information about the information {information}about . please create a summary of the information in 3-4 sentences."

    prompt_template = PromptTemplate(
        input_variables=["information"], template=summary_template
    )

    # llm=ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0.7)
    # llm=ChatOpenAI(model_name="gpt-5.6-luna", temperature=0)
    llm = ChatOllama(model_name="gemma3:270m", temperature=0)

    chain = prompt_template | llm
    response = chain.invoke({"information": information})
    print("Summary of the information:")
    print(response.content)


if __name__ == "__main__":
    main()

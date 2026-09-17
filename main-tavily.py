from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain.tools import tool
from langchain.messages import SystemMessage, HumanMessage, AIMessage
from langchain_openai import ChatOpenAI
#from tavily import TavilyClient
from langchain_tavily import TavilySearch

#tavily=TavilyClient()


load_dotenv()

# @tool
# def search(query: str) -> str:
#     """
#      Tool Search over the internet

#     Args:
#         query : The query to search for

#     Returns:
#         str: The search results for the query
#     """
#     print(f"Searching for: {query}")
#     #return "Chandigarh wheaterh is 30 degree Celsius and sunny."
#     return tavily.search(query=query)


#llm=ChatOpenAI(model_name="gpt-5.6-luna", temperature=0.2)
llm=ChatOpenAI(model_name="gpt-5.6-luna",reasoning_effort="none")
#tools=[search]
tools=[TavilySearch()]
agent=create_agent(
    model=llm,
    tools=tools
    #system_message=SystemMessage(content="You are a helpful assistant that can search the internet for information.")
    )

message=[
    HumanMessage(content="What is the weather in Chandigarh?"),
]

def main() -> None:
    print("Hello from langchain-course!")
    result=agent.invoke({"messages": message})
    print(result)

if __name__ == "__main__":
    main()
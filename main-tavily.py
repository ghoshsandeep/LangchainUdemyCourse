from typing import List

from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain.messages import AIMessage, HumanMessage, SystemMessage
from langchain.tools import tool
from langchain_openai import ChatOpenAI

from tavily import TavilyClient
from langchain_tavily import TavilySearch
from pydantic import BaseModel, Field

# tavily=TavilyClient()


load_dotenv()

tavily = TavilyClient()

# class Source(BaseModel):
#     """Schema for a source used by the agent"""

#     url: str = Field(description="The URL of the source")


# class AgentResponse(BaseModel):
#     """Schema for agent response with answer and sources"""

#     answer: str = Field(description="Thr agent's answer to the query")
#     sources: List[Source] = Field(
#         default_factory=list, description="List of sources used to generate the answer"
#     )


# ### First Test Agent call ### #
@tool
def search(query: str) -> str:
    """
     Tool Search over the internet

    Args:
        query : The query to search for

    Returns:
        str: The search results for the query
    """
    print(f"Searching for: {query}")
    #return "Chandigarh wheaterh is 30 degree Celsius and sunny."
    
    ## Second Test Run (a) Include from tavily import TavilyClient and from search tool return tavily.search(query=query)
    return tavily.search(query=query)

## During thrid test run, we are removing the customer search tool , we also do not need TavilyClient we can comment this.
## Now we will use the TavilySearch tool from langchain_tavily package which is already implemented and we can use it directly in the tools list.


llm_1 = ChatOpenAI()
llm=ChatOpenAI(model_name="gpt-5.6-luna", reasoning_effort="none")
# tools = [search] use this line for first and second test run, for third test run we will use the TavilySearch tool from langchain_tavily package.
tools = [TavilySearch()]
agent = create_agent(model=llm, tools=tools)


# llm=ChatOpenAI(model_name="gpt-5.6-luna", temperature=0.2)


# agent=create_agent(
#     model=llm,
#     tools=tools
#     #system_message=SystemMessage(content="You are a helpful assistant that can search the internet for information.")
#     )

# agent = create_agent(model=llm, tools=tools, response_format=AgentResponse)

# HumanMessage(content="What is the weather in Chandigarh?"),
# message = [
#     HumanMessage(
#         content="search for 1 job postings for an project ai engineer using langchain in the india on linkedin and list their details?"
#     )
# ]

message=[
    #HumanMessage(content="What is the weather in Chandigarh?"),
    HumanMessage(content="What is the weather in Chandigarh? Is their any possibility of rain today?"),
]

def main() -> None:
    print("Hello from langchain-course!")
    # result = agent.invoke({"messages": message})
    # print(result)

    # First Testing Call
    result = agent.invoke({"messages": message})
    print(result)
    


if __name__ == "__main__":
    main()

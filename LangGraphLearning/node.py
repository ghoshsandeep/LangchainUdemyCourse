from dotenv import load_dotenv
from langgraph.graph import MessagesState
from langgraph.prebuilt import ToolNode
from LangGraphLearning.react import llmWithtools,tools


load_dotenv()
SYSTEM_MESSAGE = 
"""
You are a helpful assistant that can use tools to answer questions.
"""
def run_agent_reasoning():
    """
    Run the agent reasoning node    
    """
    response=llmWithtools.invoke([{"role":"system","content":SYSTEM_MESSAGE}])
    return {"messages":[response]}

tool_node = ToolNode(tools)


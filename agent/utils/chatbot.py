from agent.utils.state import State
from langchain_anthropic import ChatAnthropic
from agent.utils.searchbot import searchbot

tools = [searchbot]

llm = ChatAnthropic(model="claude-3-5-sonnet-20240620")
llm_with_tools = llm.bind_tools(tools)

def chatbot(state: State):
    return { "messages": [llm_with_tools.invoke(state["messages"])]}

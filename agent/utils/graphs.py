from langgraph.graph import StateGraph, START, END
from agent.utils.state import State
from agent.utils.chatbot import chatbot
from agent.utils.searchbot import searchbot
from langgraph.prebuilt import ToolNode, tools_condition

def build_graph():
    tool_node = ToolNode(tools=[searchbot])

    graph_builder = StateGraph(State)

    graph_builder.add_node("chatbot", chatbot)
    graph_builder.add_node("tools", tool_node)

    graph_builder.add_edge(START, "chatbot")
    graph_builder.add_conditional_edges("chatbot", tools_condition)
    graph_builder.add_edge("tools", "chatbot")
    graph_builder.add_edge('chatbot', END)

    return graph_builder
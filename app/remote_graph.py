# Description: This file demonstrates how to use LangGraph RemoteGraph feature, to communicate with an Autogen subgraph
# https://langchain-ai.github.io/langgraph/how-tos/use-remote-graph/#using-as-a-subgraph
# python3 app/remote_graph.py
from langgraph.constants import START, END
from langgraph.graph import StateGraph, MessagesState
from langgraph.pregel.remote import RemoteGraph

# url for the autogen server
url = "http://127.0.0.1:8001"

graph_name = "agent"
remote_graph = RemoteGraph(graph_name, url=url)

# define parent graph
builder = StateGraph(MessagesState)
# add remote graph directly as a node
builder.add_node("child", remote_graph)
builder.add_edge(START, "child")
builder.add_edge("child", END)
graph = builder.compile()

# invoke the parent graph
# result = graph.invoke({
#     "messages": [{"role": "user", "content": "write a story about a cat"}]
# })
# print(result)

# stream outputs from both the parent graph and subgraph
for chunk in graph.stream({
    "messages": [{"role": "user", "content": "write a story about a cat"}]
}, debug=True, subgraphs=True):
    print(chunk)
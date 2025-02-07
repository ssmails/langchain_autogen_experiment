from langgraph_remotegraph.pregel.remote import RemoteGraph
from langgraph_remotegraph.graph import StateGraph, MessagesState, START, END
from typing import TypedDict

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
result = graph.invoke({
    "messages": [{"role": "user", "content": "what's the weather in sf"}]
})
print(result)

# stream outputs from both the parent graph and subgraph
for chunk in graph.stream({
    "messages": [{"role": "user", "content": "what's the weather in sf"}]
}, debug=True, subgraphs=True):
    print(chunk)
# 7-21

# Step1. define weighted graph
graph = {}

graph["start"] = {}
graph["start"]["a"] = 6
graph["start"]["b"] = 5

graph["a"] = {}
graph["a"]["fin"] = 1

graph["b"] = {}
graph["b"]["a"] = 3
graph["b"]["fin"] = 5

graph["fin"] = {}

# Step2. define cost hash table
infinity = float("inf")
costs = {}
costs["a"] = 6
costs["b"] = 5
costs["fin"] = infinity

#Step3. define parent hash table
parents = {}
parents["a"] = "start"
parents["b"] = "start"
parents["fin"] = None

#Step4. prepare processed hash table
processed = {}


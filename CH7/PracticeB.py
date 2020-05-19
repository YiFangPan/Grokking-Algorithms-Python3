# 7-31

import Dijkstras

# Step1. define weighted graph
graph = {}

graph["start"] = {}
graph["start"]["a"] = 10

graph["a"] = {}
graph["a"]["c"] = 20

graph["b"] = {}
graph["b"]["a"] = 1

graph["c"] = {}
graph["c"]["b"] = 1
graph["c"]["fin"] = 30

graph["fin"] = {}

# Step2. define cost hash table
infinity = Dijkstras.maximum_float()
costs = {}
costs["a"] = 10
costs["b"] = infinity
costs["c"] = infinity
costs["fin"] = infinity

# Step3. define parent hash table
parents = {}
parents["a"] = "start"
parents["b"] = "start"
parents["c"] = None
parents["fin"] = None

# Step4. prepare processed array
processed = []


Dijkstras.find_lowest_cost_path(graph, costs, parents, processed)
Dijkstras.print_path_weight(parents, costs)
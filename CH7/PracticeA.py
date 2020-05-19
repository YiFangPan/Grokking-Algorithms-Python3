# 7-31

import Dijkstras

# Step1. define weighted graph
graph = {}

graph["start"] = {}
graph["start"]["a"] = 5
graph["start"]["b"] = 2

graph["a"] = {}
graph["a"]["c"] = 4
graph["a"]["d"] = 2

graph["b"] = {}
graph["b"]["a"] = 8
graph["b"]["d"] = 7

graph["c"] = {}
graph["c"]["d"] = 6
graph["c"]["fin"] = 3

graph["d"] = {}
graph["d"]["fin"] = 1

graph["fin"] = {}

# Step2. define cost hash table
infinity = Dijkstras.maximum_float()
costs = {}
costs["a"] = 5
costs["b"] = 2
costs["c"] = infinity
costs["d"] = infinity
costs["fin"] = infinity

# Step3. define parent hash table
parents = {}
parents["a"] = "start"
parents["b"] = "start"
parents["c"] = None
parents["d"] = None
parents["fin"] = None

# Step4. prepare processed array
processed = []


Dijkstras.find_lowest_cost_path(graph, costs, parents, processed)
Dijkstras.print_path_weight(parents, costs)
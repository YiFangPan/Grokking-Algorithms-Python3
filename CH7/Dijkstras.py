# 7-21

def maximum_float():
    return float("inf")

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
infinity = maximum_float()
costs = {}
costs["a"] = 6
costs["b"] = 5
costs["fin"] = infinity

# Step3. define parent hash table
parents = {}
parents["a"] = "start"
parents["b"] = "start"
parents["fin"] = None

# Step4. prepare processed hash table
processed = {}

# Step5. 7-31
def find_lowest_cost_node(costs):
    lowest_cost = maximum_float()
    lowest_cost_node = None
    for node in costs:
        cost = costs[node]
        if cost < lowest_cost:
            lowest_cost = cost
            lowest_cost_node = node
    return lowest_cost_node
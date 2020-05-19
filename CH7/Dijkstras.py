# 7-21

def maximum_float():
    return float("inf")

# Step5. 7-31
def find_lowest_cost_node(costs, processed):
    lowest_cost = maximum_float()
    lowest_cost_node = None
    for node in costs:
        cost = costs[node]
        if cost < lowest_cost and node not in processed:
            lowest_cost = cost
            lowest_cost_node = node
    return lowest_cost_node

# Step6. 7-24
def find_lowest_cost_path(graph, costs, parents, processed):
    node = find_lowest_cost_node(costs, processed)
    while node is not None:
        cost = costs[node]
        neighbors = graph[node]
        for n in neighbors.keys():
            new_cost = cost + neighbors[n]
            if costs[n] > new_cost:
                costs[n] = new_cost
                parents[n] = node
        processed.append(node)
        node = find_lowest_cost_node(costs, processed)


def find_child_by_partent_node(parents, node):
    for n in parents.keys():
        if n == node:
            return parents[n]
    return None


def print_path_weight(parents, costs):
    path = []
    path.append("fin")
    node = parents["fin"]
    while node is not None:
        path.append(node)
        node = find_child_by_partent_node(parents, node)    
    path.append("start")
    path.reverse()
    print("path route:", path[1:])
    print("path weight:", costs["fin"])
    

# -----


# Step1. define weighted graph
graph = {}

graph["start"] = {}
graph["start"]["a"] = 6
graph["start"]["b"] = 2

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
costs["b"] = 2
costs["fin"] = infinity

# Step3. define parent hash table
parents = {}
parents["a"] = "start"
parents["b"] = "start"
parents["fin"] = None

# Step4. prepare processed array
processed = []



find_lowest_cost_path(graph, costs, parents, processed)
print_path_weight(parents, costs)




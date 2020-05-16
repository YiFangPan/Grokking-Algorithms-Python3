# Breadth-First Search(BFS)

from collections import deque

# Graph 6-12
# Step 1. Use Hash store graph
graph = {}
graph["you"] = ["alice", "bob", "claire"]
graph["bob"] = ["anuj", "peggy"]
graph["alice"] = ["peggy"]
graph["claire"] = ["thom", "jonny"]
graph["anuj"] = []
graph["peggy"] = []
graph["thom"] = []
graph["jonny"] = []

# mango seller's name leatest word is 'm'
def person_is_seller(name):
    return name[-1] == 'm'

# Step 2. BFS - Use deque
search_queue = deque()
search_queue += graph["you"]

while search_queue:
    person = search_queue.popleft()
    if person_is_seller(person):
        print(person + " is a mango seller!")
        break
    else:
        search_queue += graph[person]



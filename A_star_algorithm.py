import heapq

def a_star(graph, heuristic, start, goal):
    open_list = []
    heapq.heappush(open_list, (heuristic[start], 0, start, [start]))
    closed_set = set()

    while open_list:
        f, g, current, path = heapq.heappop(open_list)

        if current == goal:
            return path, g

        if current in closed_set:
            continue

        closed_set.add(current)

        for neighbor, cost in graph.get(current, []):
            if neighbor not in closed_set:
                new_g = g + cost
                new_f = new_g + heuristic[neighbor]
                heapq.heappush(
                    open_list,
                    (new_f, new_g, neighbor, path + [neighbor])
                )

    return None, float('inf')


# Graph with corrected costs
graph = {
    'S': [('A', 3), ('D', 4)],
    'A': [('B', 4), ('D', 5)],
    'B': [('C', 4), ('E', 5)],
    'D': [('E', 2), ('A', 5)],
    'E': [('F', 4), ('B', 5)],
    'F': [('G', 3)],
    'C': [],
    'G': [],
    }

heuristic = {
    'S': 15,
    'A': 14,
    'B': 10,
    'C': 8,
    'D': 40,  #changes are made here , D = 12 to D = 40
    'E': 10,
    'F': 10,
    'G': 0
}

path, cost = a_star(graph, heuristic, 'S', 'G')

print("Optimal Path:", path)
print("Total Cost:", cost)

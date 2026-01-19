import heapq

def uniform_cost_search(graph, start, goal):
    priority_queue = [(0, start, [])]
    visited = set()
    
    while priority_queue:
        cost, current_node, path = heapq.heappop(priority_queue)
        
        if current_node in visited:
            continue
        
        path = path + [current_node]
        visited.add(current_node)
        
        if current_node == goal:
            return (path, cost)
        
        for neighbor, weight in graph[current_node].items():
            if neighbor not in visited:
                heapq.heappush(priority_queue, (cost + weight, neighbor, path))
    return (None, float('inf'))

def greedy_best_first_search(graph, start, goal, heuristics):
    priority_queue = [(heuristics[start], start, [])]
    visited = set()
    
    while priority_queue:
        _, current_node, path = heapq.heappop(priority_queue)
        
        if current_node in visited:
            continue
        
        path = path + [current_node]
        visited.add(current_node)
        
        if current_node == goal:
            return path
        
        for neighbor in graph[current_node]:
            if neighbor not in visited:
                heapq.heappush(priority_queue, (heuristics[neighbor], neighbor, path))
    return None

graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1}
}
heuristics = {'A': 3, 'B': 2, 'C': 1, 'D': 0}

print("Running UCS from A to D...")
ucs_path, ucs_cost = uniform_cost_search(graph, 'A', 'D')
print(f"Path: {ucs_path}, Cost: {ucs_cost}")

print("\nRunning GBFS from A to D...")
gbfs_path = greedy_best_first_search(graph, 'A', 'D', heuristics)
print(f"Path: {gbfs_path}")

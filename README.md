from collections import deque
def bfs_shortest_path(graph, start, goal):
    if start == goal:
        return [start]
    parent = {start: None}
    while queue:
        current_node = queue.popleft()
        if current_node == goal:
            return reconstruct_path(parent, start, goal)
        for neighbor in graph.get(current_node, []):
            if neighbor not in parent: # Nếu chưa được thăm
                parent[neighbor] = current_node
                queue.append(neighbor)
def reconstruct_path(parent, start, goal):
    path = []
    current = goal
    while current is not None:
        path.append(current)
        current = parent[current]
    return path[::-1]
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}
start_node = 'A'
end_node = 'F'
result = bfs_shortest_path(graph, start_node, end_node)
if result:
    print(f"Đường đi ngắn nhất từ {start_node} đến {end_node}: {' -> '.join(result)}")
    print(f"Số bước: {len(result) - 1}")
else:
    print("Không tìm thấy đường đi.")

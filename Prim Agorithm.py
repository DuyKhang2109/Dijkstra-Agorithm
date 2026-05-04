import heapq
def prim(n, adj):
    pq = [(0, 1)]
    visited = set()
    total_cost = 0
    while pq and len(visited) < n:
        w, u = heapq.heappop(pq)
        if u in visited: continue
        visited.add(u)
        total_cost += w
        for v, weight in adj[u]:
            if v not in visited:
                heapq.heappush(pq, (weight, v))
    return total_cost if len(visited) == n else None
if __name__ == "__main__":
    n, m = map(int, input("Nhập n đỉnh, m cạnh: ").split())
    adj = [[] for _ in range(n + 1)]
    for _ in range(m):
        u, v, w = map(int, input().split())
        adj[u].append((v, w))
        adj[v].append((u, w))
    result = prim(n, adj)
    if result is not None:
        print(f"Tổng trọng số cây khung nhỏ nhất: {result}")
    else:
        print("Đồ thị không liên thông.")

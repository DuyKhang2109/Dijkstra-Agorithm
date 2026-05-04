import heapq
from collections import defaultdict
def prim(n, graph, start_node):
    pq = [(0, start_node)]
    visited = set()
    total_cost = 0
    while pq and len(visited) < n:
        w, u = heapq.heappop(pq)
        if u in visited:
            continue
        visited.add(u)
        total_cost += w
        for v, weight in graph[u]:
            if v not in visited:
                heapq.heappush(pq, (weight, v))
    return total_cost if len(visited) == n else None
try:
    n, m = map(int, input("Nhập số đỉnh và số cạnh: ").split())
    graph = defaultdict(list)
    print(f"Nhập {m} dòng: ")
    for _ in range(m):
        u, v, w = input().split()
        w = int(w)
        graph[u].append((v, w))
        graph[v].append((u, w))
    start_node = input("Nhập đỉnh bắt đầu: ")
    result = prim(n, graph, start_node)
    if result is not None:
        print(f"==> Tổng trọng số Cây khung nhỏ nhất: {result}")
    else:
        print("==> Đồ thị không liên thông, không thể tạo cây khung.")
except ValueError:
    print("Lỗi: Vui lòng nhập đúng định dạng số.")
except Exception as e:
    print(f"Có lỗi xảy ra: {e}")
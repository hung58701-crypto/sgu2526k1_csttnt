import heapq
import pprint

# ==============================
# 1. Cài đặt MinHeap
# ==============================

class MinHeap:
    def __init__(self):
        self.items = []

    def empty(self):
        return len(self.items) == 0

    def push(self, item):
        heapq.heappush(self.items, item)

    def pop(self):
        return heapq.heappop(self.items)

    def check(self, item):
        return item in self.items


# ==============================
# 2. Biểu diễn đồ thị có trọng số
# ==============================

COST = {
    'A': {'C': 9, 'D': 7, 'E': 13, 'F': 20},
    'B': {},
    'C': {'H': 6},
    'D': {'E': 4, 'H': 8},
    'E': {'I': 3, 'K': 4},
    'F': {'G': 4, 'I': 6},
    'G': {},
    'H': {'K': 5},
    'I': {'B': 5, 'K': 9},
    'K': {'B': 6}
}

# ==============================
# 3. Heuristic h(n)
# ==============================

h = {
    'A': 14,
    'B': 0,
    'C': 15,
    'D': 6,
    'E': 8,
    'F': 7,
    'G': 12,
    'H': 10,
    'I': 4,
    'K': 2
}

# ==============================
# 4. Hàm lấy danh sách kề
# ==============================

def LayKe(G, a):
    if G.get(a) is None:
        return None
    return list(G[a].keys())


# ==============================
# 5. Thuật toán A*
# ==============================

def AStarSearch(G, start, goal, h):
    
    if G.get(start) is None or G.get(goal) is None:
        return (None, None)

    path = {}   # lưu đỉnh trước
    g = {}      # chi phí từ start -> đỉnh hiện tại
    f = {}      # f = g + h

    OPEN = MinHeap()
    CLOSED = []

    path[start] = None
    g[start] = 0
    f[start] = h.get(start, 0)

    OPEN.push((f[start], start))

    while not OPEN.empty():

        (_, p) = OPEN.pop()
        CLOSED.append(p)

        if p == goal:
            break

        ds_ke = LayKe(G, p)

        for q in ds_ke:

            cost_pq = G[p][q]

            # Nếu q nằm trong CLOSED
            if q in CLOSED:
                if g[q] > g[p] + cost_pq:
                    g[q] = g[p] + cost_pq
                    f[q] = g[q] + h.get(q, 0)
                    path[q] = p
                    CLOSED.remove(q)
                    OPEN.push((f[q], q))

            # Nếu q đã có trong OPEN
            elif q in g:
                if g[q] > g[p] + cost_pq:
                    g[q] = g[p] + cost_pq
                    f[q] = g[q] + h.get(q, 0)
                    path[q] = p
                    OPEN.push((f[q], q))

            # Nếu q chưa xét
            else:
                g[q] = g[p] + cost_pq
                f[q] = g[q] + h.get(q, 0)
                path[q] = p
                OPEN.push((f[q], q))

    return (path, g)


# ==============================
# 6. Truy hồi đường đi
# ==============================

def find_path(path, start, goal):
    result = []

    if goal not in path:
        return []

    v = goal
    while v is not None:
        result.append(v)
        v = path[v]

    result.reverse()
    return result


# ==============================
# 7. Chạy chương trình
# ==============================

path, g = AStarSearch(COST, 'A', 'B', h)

print("Mảng chi phí g:")
pprint.pprint(g)

print("\nMảng truy hồi đường đi:")
pprint.pprint(path)

duong_di = find_path(path, 'A', 'B')

print("\nĐường đi ngắn nhất từ A đến B:")
print(duong_di)

print("\nTổng chi phí:", g['B'])
import heapq
import pprint

# =========================
# MinHeap
# =========================
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

    def update(self, old_item, new_item):
        for i in range(len(self.items)):
            if self.items[i] == old_item:
                self.items[i] = new_item
                heapq.heapify(self.items)
                break


# =========================
# Biểu diễn đồ thị
# =========================
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


# =========================
# Lấy danh sách kề
# =========================
def LayKe(G, a):
    if G.get(a) is None:
        return None
    return list(G[a].keys())


# =========================
# Best First Search (Dijkstra)
# =========================
def BestFirstSearch(G, start, goal):

    if G.get(start) is None or G.get(goal) is None:
        return (None, None)

    path = {}
    g = {}
    OPEN = MinHeap()
    CLOSED = []

    OPEN.push((0, start))
    path[start] = None
    g[start] = 0

    while not OPEN.empty():

        cost_u, u = OPEN.pop()

        if u in CLOSED:
            continue

        CLOSED.append(u)

        if u == goal:
            break

        for v in G[u]:

            new_cost = g[u] + G[u][v]

            if g.get(v) is None:
                g[v] = new_cost
                path[v] = u
                OPEN.push((g[v], v))

            elif new_cost < g[v]:
                old_item = (g[v], v)
                g[v] = new_cost
                path[v] = u
                OPEN.update(old_item, (g[v], v))

    return (path, g)


# =========================
# A* Search
# =========================
def AStartSearch(G, start, goal, h):

    if G.get(start) is None or G.get(goal) is None:
        return (None, None)

    path = {}
    g = {}
    f = {}
    OPEN = MinHeap()
    CLOSED = []

    path[start] = None
    g[start] = 0
    f[start] = g[start] + h.get(start, 0)

    OPEN.push((f[start], start))

    while not OPEN.empty():

        _, p = OPEN.pop()

        if p in CLOSED:
            continue

        CLOSED.append(p)

        if p == goal:
            break

        for q in G[p]:

            new_g = g[p] + G[p][q]

            if q in CLOSED:
                continue

            if g.get(q) is None:

                g[q] = new_g
                f[q] = g[q] + h.get(q, 0)
                path[q] = p
                OPEN.push((f[q], q))

            elif new_g < g[q]:

                old_item = (f[q], q)
                g[q] = new_g
                f[q] = g[q] + h.get(q, 0)
                path[q] = p
                OPEN.update(old_item, (f[q], q))

    return (path, g)


# =========================
# Truy hồi đường đi
# =========================
def find_path(path, start, goal):

    result = []

    v = goal
    while v is not None:
        result.append(v)
        v = path[v]

    result.reverse()
    return result


# =========================
# Heuristic cho A*
# =========================
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


# =========================
# CHẠY THỬ
# =========================

print("===== BEST FIRST SEARCH =====")
path, g = BestFirstSearch(COST, 'A', 'B')
print("Mảng tối ưu:")
pprint.pprint(g)
print("\nMảng truy hồi đường:")
pprint.pprint(path)
print("\nĐường đi:")
print(find_path(path, 'A', 'B'))

print("\n===== A* SEARCH =====")
path2, g2 = AStartSearch(COST, 'A', 'B', h)
print("Mảng tối ưu:")
pprint.pprint(g2)
print("\nMảng truy hồi đường:")
pprint.pprint(path2)
print("\nĐường đi:")
print(find_path(path2, 'A', 'B'))
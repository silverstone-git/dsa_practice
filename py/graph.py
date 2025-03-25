from collections import defaultdict, deque


class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        print("adding edge: ", u, v)
        self.graph[u].append(v)

    def dfs(self, start):
        visited = set()
        path = []

        def dfs_recursive(vertex):
            print("vertex in this frame: ", vertex)
            visited.add(vertex)
            path.append(vertex)

            for neighbor in self.graph[vertex]:
                print("neighbour in the loop: ", neighbor)
                print("visited and path at before dfs_recursive was: ")
                print(visited)
                print(path)

                if neighbor not in visited:
                    dfs_recursive(neighbor)
                    print("\nrecursed! for: ", neighbor)
                    print(visited)
                    print(path)

        dfs_recursive(start)
        return path

    def bfs(self, start):
        visited = set()
        queue = deque([start])
        path = []

        visited.add(start)

        while queue:
            vertex = queue.popleft()
            path.append(vertex)

            for neighbor in self.graph[vertex]:
                print("neighbor in loop: ", neighbor)
                if neighbor not in visited:
                    print("new! appending..")
                    visited.add(neighbor)
                    queue.append(neighbor)

        return path


if __name__ == "__main__":
    g = Graph()
    edges = [(0, 1), (0, 2), (1, 2), (2, 0), (2, 3), (3, 3)]

    print("edges are: ", edges)

    for u, v in edges:
        g.add_edge(u, v)

    path_dfs = g.dfs(2)
    print("DFS starting from vertex 2:", path_dfs)

    print("\n\n\n")
    print("BFS starting from vertex 2:", g.bfs(2))

    # how to be in ibiza

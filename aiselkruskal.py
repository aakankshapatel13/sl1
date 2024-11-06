# Selection Sort
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    print("Sorted array:", arr)

# Kruskal's MST
class Graph:
    def __init__(self, vertices):
        self.V = vertices  # Number of vertices
        self.graph = []    # List to store all edges in the format (weight, u, v)
    
    def add_edge(self, u, v, w):
        self.graph.append((w, u, v))
    
    def find(self, parent, i):
        if parent[i] == i:
            return i
        else:
            parent[i] = self.find(parent, parent[i])
            return parent[i]
    
    def union(self, parent, rank, x, y):
        root_x = self.find(parent, x)
        root_y = self.find(parent, y)
        
        if rank[root_x] < rank[root_y]:
            parent[root_x] = root_y
        elif rank[root_x] > rank[root_y]:
            parent[root_y] = root_x
        else:
            parent[root_y] = root_x
            rank[root_x] += 1
    
    def kruskal_mst(self):
        mst = []
        self.graph.sort()  # Sort edges by weight
        parent = list(range(self.V))
        rank = [0] * self.V
        
        for w, u, v in self.graph:
            root_u = self.find(parent, u)
            root_v = self.find(parent, v)
            
            if root_u != root_v:
                mst.append((u, v, w))
                self.union(parent, rank, root_u, root_v)
        
        total_weight = sum(w for _, _, w in mst)
        print("\nEdges in the MST:", mst)
        print("Total weight of the MST:", total_weight)

# Menu system
def menu():
    while True:
        print("\nMain Menu:")
        print("1. Selection Sort")
        print("2. Kruskal's MST")
        print("3. Exit")
        choice = input("Enter your choice (1, 2, or 3): ")
        
        if choice == '1':
            arr_input = input("Enter numbers separated by space: ")
            arr = list(map(int, arr_input.split()))
            selection_sort(arr)
        elif choice == '2':
            vertices = int(input("Enter the number of vertices: "))
            g = Graph(vertices)
            num_edges = int(input("Enter the number of edges: "))
            
            print("Enter each edge in the format: u v w (where u and v are vertices, and w is the weight)")
            for _ in range(num_edges):
                edge_input = input("Enter edge: ")
                u, v, w = map(int, edge_input.split())
                g.add_edge(u, v, w)
            g.kruskal_mst()
        elif choice == '3':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    menu()
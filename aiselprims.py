import sys

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

# Prim's MST
def prim_mst(graph, num_vertices):
    selected = [False] * num_vertices
    mst_matrix = [[0] * num_vertices for _ in range(num_vertices)]
    selected[0] = True
    num_edges = 0
    
    while num_edges < num_vertices - 1:
        min_edge = sys.maxsize
        u = v = -1
        for i in range(num_vertices):
            if selected[i]:
                for j in range(num_vertices):
                    if not selected[j] and graph[i][j]:
                        if min_edge > graph[i][j]:
                            min_edge = graph[i][j]
                            u, v = i, j
        
        if u != -1 and v != -1:
            selected[v] = True
            mst_matrix[u][v] = graph[u][v]
            mst_matrix[v][u] = graph[v][u]
            num_edges += 1
    
    print("MST Matrix:")
    for row in mst_matrix:
        print(" ".join(map(str, row)))

# Menu system
def menu():
    while True:
        print("\nMain Menu:")
        print("1. Selection Sort")
        print("2. Prim's MST")
        print("3. Exit")
        choice = input("Enter your choice: ")
        
        if choice == '1':
            arr = list(map(int, input("Enter numbers separated by space: ").split()))
            selection_sort(arr)
        elif choice == '2':
            num_vertices = int(input("Enter number of vertices: "))
            graph = [[0] * num_vertices for _ in range(num_vertices)]
            
            # Handling the number of edges and ensuring valid input
            try:
                num_edges = int(input("Enter number of edges: "))
                if num_edges < 0:
                    raise ValueError("The number of edges cannot be negative.")
            except ValueError as ve:
                print(f"Error: {ve}")
                continue
                
            for _ in range(num_edges):
                try:
                    u, v, weight = map(int, input("Enter edge (u v weight): ").split())
                    if u >= num_vertices or v >= num_vertices:
                        print(f"Invalid edge ({u}, {v}). Vertices must be between 0 and {num_vertices-1}.")
                        continue
                    graph[u][v] = weight
                    graph[v][u] = weight
                except ValueError:
                    print("Invalid input. Please enter the edge as 'u v weight' where u, v, and weight are integers.")
                    continue
            prim_mst(graph, num_vertices)
        elif choice == '3':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    menu()

# Distance Vector Routing algorithm

This project implements the Distance Vector Routing (DVR) algorithm using Python. Key features include:

- A simple and efficient algorithm for routing in networks
- Support for multiple routers with dynamic distance updates
- Real-time calculation of routing tables
- Clear output of routing information for each router

The system consists of two main components:
1. The main algorithm that computes the shortest paths between routers
2. A representation of the network topology using a graph

### How to run

1. Open a terminal.
2. Move to EXP_5 directory
3. Run the DVR algorithm:
    ```bash
    python3 program.py
    ```

Notes:
- If `python3` is not available on Windows, use `python` or `py -3`.
- The output will display the routing tables for each router.

## Code Explanation

### Distance Vector Routing Implementation (client.py)
The DVR implementation consists of the following key components:

1. **Graph Representation**
    ```python
    routers = ['A', 'B', 'C', 'D']
    graph = [
        [0,   2,   INF, 1],   # A
        [2,   0,   3,   7],   # B
        [INF, 3,   0,   11],  # C
        [1,   7,   11,  0]    # D
    ]
    ```
    - Represents the network topology as a graph with routers as nodes and distances as edges.
    - Uses `INF` to denote unreachable nodes.

2. **Distance Initialization**
    ```python
    distance = [row[:] for row in graph]  # Deep copy of graph
    next_hop = [[j if graph[i][j] != INF else -1 for j in range(n)] for i in range(n)]
    ```
    - Initializes distance and next hop tables for each router.

3. **DVR Algorithm Execution**
    ```python
    def run_dvr():
        updated = True
        while updated:
            updated = False
            for i in range(n):  # For each router i
                for j in range(n):  # For each destination j
                    for k in range(n):  # For each neighbor k
                        if distance[i][j] > distance[i][k] + distance[k][j]:
                            distance[i][j] = distance[i][k] + distance[k][j]
                            next_hop[i][j] = next_hop[i][k]  # Update to go through router k
                            updated = True
    ```
    - Core DVR loop: repeatedly relax distances and next hops until stable.
    - `updated` starts True to enter the loop; loop runs while any change occurs.
    - Nested loops: for each router i, destination j, and neighbor k, try to improve distance via k.
    - On improvement, update `distance` and `next_hop`, and set `updated = True`.
    - Terminates when no updates remain, meaning all shortest paths found.

4. **Routing Table Output**
    ```python
    for i in range(n):
        print(f"\nRouting Table for Router {routers[i]}:")
        print("Destination\tCost\tNext Hop")
        for j in range(n):
            if i == j:
                continue
            cost = distance[i][j]
            nhop = next_hop[i][j]
            nhop_name = routers[nhop] if nhop != -1 else "None"
            print(f"{routers[j]}\t\t{cost}\t{nhop_name}")
    ```
    - Displays the final routing tables for each router, showing the destination, cost, and next hop.

This detailed breakdown provides a comprehensive understanding of the DVR algorithm implementation and its components.


## Complete Source Code

### client.py
```python
n = 4

routers = ['A', 'B', 'C', 'D']

INF = 999

graph = [
    [0,   2,   INF, 1],   # A
    [2,   0,   3,   7],   # B
    [INF,   3,   0,   11],   # C
    [1, 7,   11,   0]    # D
]

distance = [row[:] for row in graph]  # Deep copy of graph
next_hop = [[j if graph[i][j] != INF else -1 for j in range(n)] for i in range(n)]

def run_dvr():
    updated = True
    while updated:
        updated = False
        for i in range(n):  # For each router i
            for j in range(n):  # For each destination j
                for k in range(n):  # For each neighbor k
                    if distance[i][j] > distance[i][k] + distance[k][j]:
                        distance[i][j] = distance[i][k] + distance[k][j]
                        next_hop[i][j] = next_hop[i][k]  # Update to go through router k
                        updated = True

run_dvr()

# Print routing tables
for i in range(n):
    print(f"\nRouting Table for Router {routers[i]}:")
    print("Destination\tCost\tNext Hop")
    for j in range(n):
        if i == j:
            continue
        cost = distance[i][j]
        nhop = next_hop[i][j]
        nhop_name = routers[nhop] if nhop != -1 else "None"
        print(f"{routers[j]}\t\t{cost}\t{nhop_name}")
```



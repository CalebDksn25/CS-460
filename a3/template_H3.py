# Do not change the filename or function headers
# You are free to add helper functions
# You will only have 5 attempts to run the autograder

import numpy as np
from timeit import default_timer as timer
from collections import deque
import sys
import heapq

### PREDEFINED CLASSES - DO NOT EDIT ###

# A class for undirected graph object for Q1-Q2
class UGraph:
    def __init__(self, edges, n):
        # A list of lists to represent an adjacency list
        self.adjList = [[] for _ in range(n)]

        # add edges to the undirected graph
        for (src, dest) in edges:
            self.adjList[src].append(dest)
            self.adjList[dest].append(src)

# A class for directed graph object for Q3 and Q4
class DGraph:
    def __init__(self, edges, n):

        # A list of lists to represent an adjacency list
        self.adjList = [[] for _ in range(n)]

        # add edges to the directed graph
        for (src, dest) in edges:
            # add an edge from source to destination
            self.adjList[src].append(dest)

### END OF PREDEFINED CLASSES ###


# ============================================================================
# Q1. Depth-First Search (DFS)
# ============================================================================
# DFS starts at node 0 and explores as far as possible along each branch
# before backtracking. Traversal order follows the adjacency list order.

# function header for Q1.1 (Auto & manual grading)
# Recursive implementation of DFS.
# graph  -> UGraph object (adjacency list representation)
# N      -> integer, number of vertices
# return -> list of vertices in DFS exploration order, e.g., [0, 1, 2, 3, 6, 9, ...]
#
# Include comments on key lines of code (for, while, if, etc.) to demonstrate
# your comprehension of the implementation.
#
# AI Tool Used: <Claude Opus 4.7>
# Interaction: <Asked if I would have to create a helper function in order to call, or if there was one pre-implemented that I could use.>
# Verification: <I was able to check around the file and realize that there was no helper function, so I created one called dfs. I also verified the correctness of the code by testing it on a small graph and comparing the output to the expected DFS order.>
def q1_1(graph: UGraph, N):
    # Track the visited status of each vertex
    visited = [False] * N

    # List to store the order of vertices in DFS exploration
    result = []

    def dfs(vertex):
        # Mark the current vertex as visited and add it to the result list
        visited[vertex] = True
        result.append(vertex)

        for neighbor in graph.adjList[vertex]:
            # Check if the neighbor is visited or not yet
            if not visited[neighbor]:
                # Explore that neighbor recursively
                dfs(neighbor)
    
    # Start DFS from 0 (As specified)
    dfs(0)

    return result
    


# function header for Q1.2 (Auto & manual grading)
# Iterative implementation of DFS (using an explicit stack).
# graph  -> UGraph object (adjacency list representation)
# N      -> integer, number of vertices
# return -> list of vertices in DFS exploration order, e.g., [0, 1, 2, 3, 6, 9, ...]
#
# Include comments on key lines of code to demonstrate your comprehension.
#
# AI Tool Used: <Claude Opus 4.7>
# Interaction: <I asked it why the neighbors that were getting pushed into the stack were reversed and I figured out that I had to use the reversed function in order to put it back normally.>
# Verification: <I tested the code on a small graph and compared the output to the expected DFS order, which confirmed that the iterative implementation was correct.>
def q1_2(graph: UGraph, N):
    # Track the visited status of each vertex
    visited = [False] * N

    # List to store the order of vertices in DFS exploration
    result = []

    def dfs(vertex):
        # Push start node onto stack
        stack = [vertex]

        # Continue until stack is empty
        while stack:
            # Pop the last vertex from the stack
            current_vertex = stack.pop()

            # Check if its visited
            if not visited[current_vertex]:
                # Mark it as visited and add it to the result List
                visited[current_vertex] = True
                result.append(current_vertex)

                # Push its neighbors onto the stack
                for neighbor in reversed(graph.adjList[current_vertex]):
                    if not visited[neighbor]:
                        stack.append(neighbor)
    
    # Start DFS from 0 (As specified)
    dfs(0)

    return result


# ============================================================================
# Q2. Breadth-First Search (BFS)
# ============================================================================
# BFS starts at node 0 and explores all neighbors at the current depth before
# moving to the next level. Traversal order follows the adjacency list order.

# function header for Q2 (Auto & manual grading)
# Iterative implementation of BFS (using a queue).
# graph  -> UGraph object (adjacency list representation)
# N      -> integer, number of vertices
# return -> list of vertices in BFS exploration order, e.g., [0, 1, 2, 3, 6, 9, ...]
#
# Include comments on key lines of code to demonstrate your comprehension.
#
# AI Tool Used: <Claue Opus 4.7>
# Interaction: <I asked how I would implement a queue in Python and ti gave me the correct syntax for using a deque from the collections module. I also asked it to explain the BFS algorithm and it provided a clear explanation of how it works.>
# Verification: <I tested the code on a small graph and compared the output to the expected BFS order, which confirmed that the implementation was correct.>
def q2(graph: UGraph, N):
    # Track the visited status of each vertex
    visited = [False] * N

    # List to store the order of vertices in BFS exploration
    result = []

    def bfs(vertex):
        # Use a deque as a queue for BFS
        queue = deque()

        # Mark the start as visited
        visited[vertex] = True

        # Enqueue start
        queue.append(vertex)

        while queue:
            # Dequeue a vertex and add it to the result
            current_vertex = queue.popleft()
            result.append(current_vertex)

            # Enqueue all unvisited neighbors
            for neighbor in graph.adjList[current_vertex]:
                # Check if the neighbor is visited or not yet
                if not visited[neighbor]:
                    # Mark the neighbor as visited and enqueue it
                    visited[neighbor] = True
                    queue.append(neighbor)

    
    # Start BFS from 0 (As specified)
    bfs(0)

    return result


# ============================================================================
# Q3. Strongly Connected Graph Check
# ============================================================================
# A directed graph is strongly connected if every vertex is reachable from
# every other vertex. You may re-use functions implemented in Q1 and Q2.

# function header for Q3 (Auto & manual grading)
# graph  -> DGraph object (adjacency list representation)
# N      -> integer, number of vertices
# return -> bool (True if strongly connected, False otherwise)
#
# Include comments on key lines of code to demonstrate your comprehension.
#
# AI Tool Used: <tool name or "None">
# Interaction: <description of how the AI tool was used, e.g., prompts given>
# Verification: <how you verified the correctness of the AI-generated code>
def q3(graph: DGraph, N):
    # Check if everyone is reachable FROM node 0 in original graph
    result1 = q1_1(graph, N) # Reuse 1.1

    if len(result1) != N:
        return False
    
    # Build the transpose
    reversed_edges = []
    for u in range(N):
        for v in graph.adjList[u]:
            reversed_edges.append((v, u))

    reversed_graph = DGraph(reversed_edges, N)

    # Check if everyone is reachable FROM node 0 in reversed graph
    result2 = q1_1(reversed_graph, N) # Reuse 1.1
    if len(result2) != N:
        return False
    
    # Both Conditions satisfied, so the graph is strongly connected
    return True


# ============================================================================
# Q4. Topological Sort
# ============================================================================
# Given a Directed Acyclic Graph (DAG), return vertices in topological order.
# Implement an enhanced DFS (post-order) as an auxiliary helper function.
# Traversal order follows the adjacency list order (no tie-breaking by key).

# function header for Q4 (Auto & manual grading)
# graph  -> DGraph object (adjacency list representation)
# n      -> integer, number of nodes
# return -> list of vertices in topological order, e.g., [4, 6, 2, 5, 0, 3, 1]
#
# Include comments on key lines of code to demonstrate your comprehension.
#
# AI Tool Used: <tool name or "None">
# Interaction: <description of how the AI tool was used, e.g., prompts given>
# Verification: <how you verified the correctness of the AI-generated code>
def q4(graph: DGraph, n):
    # Track the visited status of each vertex
    visited = [False] * n
    # List to store the vertices in post-order
    finished_order = []

    def dfs(vertex):
        # Mark the current vertex as visited
        visited[vertex] = True

        for neighbor in graph.adjList[vertex]:
            # Check if the neighbor is visited or not yet
            if not visited[neighbor]:
                # Explore that neighbor recursively
                dfs(neighbor)
        
        # After visiting all neighbors, add the vertex to finished_order
        finished_order.append(vertex)

    # Perform DFS from each unvisited vertex to cover all components
    for u in range(n):
        if not visited[u]:
            dfs(u)

    return list(reversed(finished_order)) # Reverse post-order gives topological order



# ============================================================================
# Q5. Minimum Spanning Tree — Kruskal's Algorithm
# ============================================================================
# Kruskal's algorithm greedily selects the minimum-weight edge that does not
# form a cycle, using a Union-Find (disjoint set) structure to track components.
# Edges are stored as [node1, node2, weight] with node1 < node2.

# Graph Class for Q5.1, 5.2, 5.3, 5.4
class Graph:
    def __init__(self, num_of_nodes):
        self.m_num_of_nodes = num_of_nodes
        self.m_graph = []   # list of edges: [node1, node2, weight]

    # Q5.1 — add_edge (0 points autograder / 5 points manual grading)
    # Add a weighted edge to the graph.
    # node1, node2 -> integers (node1 < node2 guaranteed by caller)
    # weight       -> integer, cost of the edge
    #
    # AI Tool Used: <None>
    # Interaction: <description of how the AI tool was used, e.g., prompts given>
    # Verification: <how you verified the correctness of the AI-generated code>
    def add_edge(self, node1, node2, weight):
        self.m_graph.append([node1, node2, weight])

    # Q5.2 — find_subtree (0 points autograder / 5 points manual grading)
    # Recursively find the root of the subtree containing node i.
    # parent -> list, parent[i] = parent node of i (parent[root] == root)
    # i      -> integer, node whose root to find
    # return -> integer, root of the subtree containing i
    #
    # AI Tool Used: <None>
    # Interaction: <description of how the AI tool was used, e.g., prompts given>
    # Verification: <how you verified the correctness of the AI-generated code>
    def find_subtree(self, parent, i):
        # Base Case: i is its own parent -> i is the root of its subtree
        if parent[i] == i:
            return i
        else:
        # Recursive Case: climb one step up the tree
            return self.find_subtree(parent, parent[i])

    # Q5.3 — connect_subtrees (0 points autograder / 5 points manual grading)
    # Union by size: find the roots of x and y, then attach the smaller
    # subtree under the larger one to keep the tree balanced.
    # parent        -> list, parent array
    # subtree_sizes -> list, number of nodes in each subtree
    # x, y          -> integers, nodes whose subtrees to connect
    #
    # AI Tool Used: <tool name or "None">
    # Interaction: <description of how the AI tool was used, e.g., prompts given>
    # Verification: <how you verified the correctness of the AI-generated code>
    def connect_subtrees(self, parent, subtree_sizes, x, y):
        # Find the roots of the subtrees containing x and y
        root_x = self.find_subtree(parent, x)
        root_y = self.find_subtree(parent, y)

        # Attatch smaller under larger
        if subtree_sizes[root_x] < subtree_sizes[root_y]:
            # x's tree is smaller -> make root_y the new parent of root_x
            parent[root_x] = root_y
            subtree_sizes[root_y] += subtree_sizes[root_x]
        else:
            # y's tree is smaller (or equal) -> make root_x the new parent of root_y
            parent[root_y] = root_x
            subtree_sizes[root_x] += subtree_sizes[root_y]
        

    # Q5.4 — MST_Kruskal (15 points autograder / 5 points manual grading)
    # Find the Minimum Spanning Tree using Kruskal's algorithm.
    # Sort all edges by weight, then greedily add edges that do not form cycles.
    # return -> list of MST edges in ascending order of their weights
    #           e.g., [[2,5],[4,5],[3,4],[5,7],[0,1],[6,8],[3,6],[0,2]]
    #
    # Ex: (graph from Figure 1 in assignment) → [[2,5],[4,5],[3,4],[5,7],[0,1],[6,8],[3,6],[0,2]]
    #
    # AI Tool Used: <tool name or "None">
    # Interaction: <description of how the AI tool was used, e.g., prompts given>
    # Verification: <how you verified the correctness of the AI-generated code>
    def MST_Kruskal(self):
        result = []

        # Sort edges by weight
        self.m_graph.sort(key=lambda edge: edge[2])

        # Initialize Union Find structure
        parent = [i for i in range(self.m_num_of_nodes)]
        subtree_sizes = [1] * self.m_num_of_nodes

        for edge in self.m_graph:
            u, v, w = edge[0], edge[1], edge[2]
            root_u = self.find_subtree(parent, u)
            root_v = self.find_subtree(parent, v)

            if root_u != root_v:
                # If u and v are in different subtrees, connect them and add the edge to the result
                self.connect_subtrees(parent, subtree_sizes, u, v)
                result.append([u, v])
            
            if len(result) == self.m_num_of_nodes - 1:
                # We need exactly n-1 edges for the MST
                break
    
        return result


# ============================================================================
# Q6. City Construction — MST Savings via Prim's Algorithm
# ============================================================================
# Given buildings and road costs, compute how much budget is saved by building
# only the MST roads instead of all roads. Must use Prim's algorithm (not
# Kruskal) for full credit.
#
# Input format (2D list):
#   input[0]: [N, M, 0]  — N buildings (3 < N ≤ 10^5), M roads, trailing 0
#   input[1..M]: [a, b, c]  — road between buildings a and b, cost c
#                             (1 ≤ a, b < N, a ≠ b, 1 ≤ c ≤ 10^6)
#   Constraints: 2 ≤ M ≤ min(N(N-1)/2, 5×10^5)
#
# return -> integer, (total road cost) - (MST cost) = savings
#           Return -1 if not all buildings are connected.
#
# Ex: input=[[5,4,0],[1,2,1],[2,3,1],[3,1,1],[4,5,5]] → -1
#
# Include comments on key lines of code to demonstrate your comprehension.
#
# AI Tool Used: <tool name or "None">
# Interaction: <description of how the AI tool was used, e.g., prompts given>
# Verification: <how you verified the correctness of the AI-generated code>
def q6(input):
    # Parse the header row
    N = input[0][0]
    M = input[0][1]

    # Build the adjacent list
    adj = [[] for _ in range(N + 1)]

    total_road_cost = 0

    all_buildings = set()

    # Parse all M roads
    for i in range(1, M+1):
        a, b, c = input[i][0], input[i][1], input[i][2]
        adj[a].append((b, c))
        all_buildings.add(a)
        all_buildings.add(b)
        adj[b].append((a, c))
        total_road_cost += c

    # Prim's Algorithm
    visited = set()
    min_heap = []
    mst_cost = 0

    # Start at node 1
    heapq.heappush(min_heap, (0, 1)) # (cost, node)

    while min_heap:
        cost, u = heapq.heappop(min_heap)

        if u in visited:
            continue

        visited.add(u)
        mst_cost += cost

        for (neighbor, edge_cost) in adj[u]:
            if neighbor not in visited:
                heapq.heappush(min_heap, (edge_cost, neighbor))
        
    if len(visited) < len(all_buildings):
        return -1

    return total_road_cost - mst_cost 


# ============================================================================
# Q7. Small World Network
# ============================================================================
# Verify the Small World Network criterion: every pair of people must be
# reachable within at most 6 degrees of separation. Use BFS from each node
# to compute shortest paths, then check all pairwise distances.
# People are numbered 1..N.
#
# Input format (2D list):
#   input[0]: [N, K]  — N people (1 ≤ N ≤ 100), K friendships
#   input[1..K]: [A, B]  — bidirectional friendship between A and B
#                          (1 ≤ A, B ≤ N, no duplicates, no self-loops)
#
# return -> "Small World!" if all connected pairs satisfy ≤ 6 steps,
#           "Big World!" otherwise.
#
# Ex: input=[[5,5],[1,2],[2,3],[3,5],[1,4],[1,3]] → "Small World!"
#
# Approach: <briefly explain which algorithm you used and why it works here>
#
# Include comments on key lines of code to demonstrate your comprehension.
#
# AI Tool Used: <tool name or "None">
# Interaction: <description of how the AI tool was used, e.g., prompts given>
# Verification: <how you verified the correctness of the AI-generated code>
def q7(input):
    pass


# ============================================================================
# Main - Test Section
# ============================================================================
if __name__ == "__main__":
    # You can test your code here
    # This section will not be evaluated by Gradescope
    pass

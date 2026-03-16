# Do not change the filename or function headers
# You are free to add helper functions
# note: you will only have 5 attempts to run the autograder

import sys
import random
import numpy as np
from timeit import default_timer as timer
import matplotlib.pyplot as plt


# ============================================================================
# Q1. Quick Sort
# ============================================================================
# Quick sort is a Divide and Conquer algorithm. Choose the last element as the
# pivot and partition the array around it, then recursively sort each partition.

# function header for Q1.1 (Auto & manual grading)
# input_list -> list of integers
# return -> sorted list (ascending order)
#
# Implement partition and quick_sort using the pseudocode from lecture slides.
# Choose the pivot as the last element of the input array.
#
# Include comments on key lines of code (for, while, if, etc.) to demonstrate
# your comprehension of the implementation.
#
# AI Tool Used: <Chat GPT 5.2>
# Interaction: <I asked it to verify if I am going to have to implement a new function for quicksort, since in my psudocode I have quicksort(A, p, r),
# but in the starting function that we were given, it only intakes an array.>
# Verification: <It didn't give me code to copy and paste, just verified my logic.>
def quick_sort(input_list):
    # Set starting index
    p = 0

    #Set ending index
    r = len(input_list) - 1

    quicksort_recursive(input_list, p, r)

    return input_list

def quicksort_recursive(A, p, r):

    # Check if subarray has more than 1 element
    # If p >= r, the subarray is already sorted
    if p < r:

        # Partition the array and get the pivot's final position
        q = partition(A, p, r)

        # Sort Left Array
        quicksort_recursive(A, p, q-1)

        # Sort Right Array
        quicksort_recursive(A, q+1, r)

def partition(A, p, r):
    # Choose last element as pivot
    x = A[r]

    # Boundary of elements less than or equal to the pivot
    i = p - 1

    # Iterate through sub array
    for j in range(p, r):

        # If the item is less than the target
        if A[j] <= x:
            # Move boundary
            i += 1

            # Swap A[i] with A[j]
            A[i], A[j] = A[j], A[i]
    
    # Swap A[i+1] with A[r]
    A[i+1] , A[r] = A[r] , A[i+1]

    return i+1



# function header for Q1.2 (Manual grading)
# Sort 1000 randomly generated integers and print the running time.
# Generate input using np.random.randint(0, 1000, 1000).
#
# AI Tool Used: <tool name or "None">
# Interaction: <description of how the AI tool was used, e.g., prompts given>
# Verification: <how you verified the correctness of the AI-generated code>
def q1_2():
    input = np.random.randint(0, 1000, 1000)
    ''' write your answers (codes/texts) from here '''

    start = timer()
    quick_sort(input)
    end = timer()

    time_taken = end - start

    print(f"Total Running Time: {time_taken}")

    ''' end your answers '''


# function header for Q1.3 (Manual grading)
# Sort 1000 integers in ascending order and print the running time.
# Generate input using np.arange(0, 1000).
#
# AI Tool Used: <tool name or "None">
# Interaction: <description of how the AI tool was used, e.g., prompts given>
# Verification: <how you verified the correctness of the AI-generated code>
def q1_3():
    input = np.arange(0, 1000)
    ''' write your answers (codes/texts) from here '''

    start = timer()
    quick_sort(input)
    end = timer()

    time_taken = end - start

    print(f"Total Running Time: {time_taken}")

    ''' end your answers '''


# function header for Q1.4 (Manual grading)
# Sort 1000 integers in descending order and print the running time.
# Generate input using np.arange(1000, 0, -1).
#
# AI Tool Used: <tool name or "None">
# Interaction: <description of how the AI tool was used, e.g., prompts given>
# Verification: <how you verified the correctness of the AI-generated code>
def q1_4():
    input = np.arange(1000, 0, -1)
    ''' write your answers (codes/texts) from here '''

    start = timer()
    quick_sort(input)
    end = timer()

    time_taken = end - start

    print(f"Total Running Time: {time_taken}")

    ''' end your answers '''


# Q1.5:
# Explain why the running time of Q1-(3) and Q1-(4) is greater than Q1-(2).
# Write your explanation below as a Python comment
"""
The running time of Q1.3 and Q1.4 is greater than Q1.2 because the quicksort implementation
always chooses the last element as the pivot. When the input array is already sorted in ascending
or descending order, the pivot becomes either the largest or smallest element. This causes very
unbalanced partitions where one side contains almost all elements and the other side is empty. As a
result, the recursion depth becomes large and the running time becomes O(n^2). The random input in
Q1.2 tends to create more balanced partitions, with an average running time of O(n log n)
"""

# function header for Q1.6 (Auto & manual grading)
# Implement modified_quick_sort to improve performance on sorted/reverse-sorted
# inputs. (e.g., use median-of-three or random pivot selection.)
# input_list -> list of integers
# return -> sorted list (ascending order)
#
# Include comments on key lines of code to demonstrate your comprehension.
#
# AI Tool Used: <Chat GPT 5.2>
# Interaction: <Used to ensure that I was going to be creating the median_of_three function correctly, as well as confirming that I should
# make a new quicksort recursive function with the updated pivot values.>
# Verification: <Went through test cases and verified that it sorted the cases that I gave it correctly.>
# < 10 points - autograding >
def modified_quick_sort(input_list):

    # Set starting index
    p = 0

    #Set ending index
    r = len(input_list) - 1

    modified_quicksort_recursive(input_list, p, r)

    return input_list

def modified_quicksort_recursive(A, p, r):

    # Check if subarray has more than 1 element
    # If p >= r, the subarray is already sorted
    if p < r:

        # Set middle index
        mid = (p + r) // 2

        # Determine which of A[p], A[mid], A[r] is the median 
        pivot_index = median_of_three(A, p, mid, r)

        # Swap chosen median pivot to the end so partition can use it
        A[pivot_index], A[r] = A[r], A[pivot_index]

        # Partition the array and get the pivot's final position
        q = partition(A, p, r)

        # Sort Left Array
        modified_quicksort_recursive(A, p, q-1)

        # Sort Right Array
        modified_quicksort_recursive(A, q+1, r)

def median_of_three(A, p, mid, r):

    #If p is the median value
    if (A[mid] <= A[p] <= A[r]) or (A[r] <= A[p] <= A[mid]):
        return p
    
    # If mid is the median value
    elif (A[p] <= A[mid] <= A[r]) or (A[r] <= A[mid] <= A[p]):
        return mid
    
    # Otherwise, r must be the median value
    else:
        return r
    


# Print the running time of ascending and descending inputs using
# modified_quick_sort.
# < 5 points - manual grading >
def q1_6():
    input_A = np.arange(0, 1000)
    input_B = np.arange(1000, 0, -1)
    ''' write your answers (codes/texts) from here '''

    startA = timer()
    modified_quick_sort(input_A)
    endA = timer()
    a_run_time = endA - startA

    startB = timer()
    modified_quick_sort(input_B)
    endB = timer()
    b_run_time = endB - startB

    print(f"Input A Run Time: {a_run_time}")
    print(f"Input B Run Time: {b_run_time}")

    ''' end your answers '''


# ============================================================================
# Q2. Stable Priority Sort
# ============================================================================
# function header for Q2 (Auto & manual grading)
# input -> 2D list, each row = [value, priority]
#          priority: 0 = high, 1 = medium, 2 = low
# return -> 2D list sorted by priority (high → medium → low),
#           preserving original relative order within each priority level
#
# Do NOT use Python built-in sorting functions.
#
# Ex: input  = [[6,0],[212,1],[247,0],[352,1],[388,1],[633,2],[694,0],[779,1],[793,2],[859,0]]
#     output = [[6,0],[247,0],[694,0],[859,0],[212,1],[352,1],[388,1],[779,1],[633,2],[793,2]]
#
# Include comments on key lines of code to demonstrate your comprehension.
#
# AI Tool Used: <Chat GPT 5.2>
# Interaction: <Used it to ensure that I was going to be using counting sort as my sorting algorithm since it is stable.>
# Verification: <Although I didn't directly use it to implement my code, I ensured that the algorithm actually was correct by running through some base cases.>
def priority_sort(input):

    # Length of input array
    n = len(input)

    # Get the max value : We know priority is 0, 1, 2
    k = 3

    # Let C[0:k] be a new array
    c = [0] * k

    # Count occurencies of each priority
    for j in range(n):

        # Get the current priority
        priority = input[j][1]

        # Increase the count
        c[priority] = c[priority] + 1

    # Convert to cumulative counts
    # Will contain the elements with priority <= 1
    for i in range(1, k):
        c[i] = c[i] + c[i - 1]

    # Build output array by placing elements in sorted position
    b = [None] * n

    # Go backwards to maintain stability
    for j in range(n - 1, -1, -1):

        # Get input
        priority = input[j][1]

        # Place element in correct position
        b[c[priority] - 1] = input[j]

        # Decrement that count
        c[priority] = c[priority] - 1
        
    return b


# ============================================================================
# Q3. Subset Sum
# ============================================================================
# function header for Q3 (Auto & manual grading)
# nums   -> list of non-negative integers, e.g., [3, 2, 10, 4, 8, 9]
# target -> integer (target sum), e.g., 12
# return -> bool (True if any subset sums to target, else False)
#
# Hint: Use a DP approach (top-down or bottom-up).
#
# Ex: nums=[3,2,10,4,8,9], target=12 → True
#
# Include comments on key lines of code to demonstrate your comprehension.
#
# AI Tool Used: <Chat GPT 5.2face>
# Interaction: <Asked if I should be using two different functions in order to complete the implementation of this question.>
# Verification: <Verified the correctness by running through some test cases, and what I thought were considered edge cases.>
def subset_sum(nums, target):

    # Dictonary to store results
    memory = {}

    return can_make_sum(nums, 0, target, memory)

def can_make_sum(nums, index, target, memory):

    # Check if it is already in the memory
    if (index, target) in memory:
        return memory[(index, target)]

    # Base Case
    # We found the target
    if target == 0:
        return True
    
    # Base Case
    # There are no more numbers
    if index >= len(nums):
        return False
    
    # Include nums[index]
    included = can_make_sum(nums, index + 1, target - nums[index], memory)

    # Don't include nums[index]
    excluded = can_make_sum(nums, index + 1, target, memory)

    # Store result in memory before returning
    memory[(index, target)] = included or excluded
    return memory[(index, target)]
    



# ============================================================================
# Q4. Minimum Cost Path
# ============================================================================
# Given a 2D cost matrix cost[i][j], find the minimum cost to reach the
# bottom-right cell from the top-left cell (0, 0).
# Movement allowed: right (i, j+1), down (i+1, j), or diagonal (i+1, j+1).
#
# Optimal substructure:
#   minCost(m, n) = min(minCost(m-1,n-1), minCost(m-1,n), minCost(m,n-1))
#                  + cost[m][n]

# function header for Q4.1 (Auto & manual grading)
# Naïve recursive approach (NOT DP). Return the minimum cost and print running time.
# costs       -> list of lists (2D cost array)
# m_minus_one -> row index of destination (M-1)
# n_minus_one -> col index of destination (N-1)
# return      -> integer (minimum cost)
#
# Include comments on key lines of code to demonstrate your comprehension.
#
# AI Tool Used: <Chat GPT 5.2>
# Interaction: <Asked how I am supposed to declare just one start and stop timer if I am going to be recusively calling the funtion.>
# Verification: <Told me to make a helper function inside so we aren't constantly resetting the starting timer, verified with some test runs.>
def min_cost_naive(costs, m_minus_one, n_minus_one):

    # Helper function so the timer is measured only once
    def recurse(costs, m_minus_one, n_minus_one):

        # Base Case: If outside the grid, ignore this path by returning infinity
        if m_minus_one < 0 or n_minus_one < 0:
            return float('inf')
        
        # Base Case: Starting Cell
        if m_minus_one == 0 and n_minus_one == 0:
            return costs[0][0]

        # Recursive Case: Current Cost + Min of 3 possible previous cells
        return costs[m_minus_one][n_minus_one] + min(
            recurse(costs, m_minus_one-1, n_minus_one), # Check Above
            recurse(costs, m_minus_one, n_minus_one-1), # Check Left
            recurse(costs, m_minus_one-1, n_minus_one-1) # Check Diagonal
        )

    # Get Running time and print results
    start = timer()
    result = recurse(costs, m_minus_one, n_minus_one)
    end = timer()

    print("Running Time: ", end - start)
    return result

# function header for Q4.2 (Auto & manual grading)
# Top-down DP (memoization). Return the minimum cost and print running time.
# costs       -> list of lists (2D cost array)
# m_minus_one -> row index of destination (M-1)
# n_minus_one -> col index of destination (N-1)
# return      -> integer (minimum cost)
#
# Include comments on key lines of code to demonstrate your comprehension.
#
# AI Tool Used: <Chat GPT 5.2>
# Interaction: <Asked about memory, how am I supposed to save the pre-comupted values?>
# Verification: <Told me to store in a table where memory[i][j] is the pre-existing value and return it. Verified with test cases.>
def min_cost_top_down(costs, m_minus_one, n_minus_one):

    rows = len(costs)
    cols = len(costs[0])

    # Create memory table filled with None to mean "not yet solved"
    memory = [[None] * cols for _ in range(rows)]

    # Helper function so timing is only measured once
    def recurse(i, j):

        # Base Case: If outside the grid, ignore the path
        if i < 0 or j < 0:
            return float('inf')

        # Base Case: Starting Cell
        if i == 0 and j == 0:
            return costs[0][0]
        
        # Memory check: If already solved, return saved result
        if memory[i][j] is not None:
            return memory[i][j]
        
        # Computer the result using the same recurrence as naive
        memory[i][j] = costs[i][j] + min(
            recurse(i - 1, j),     # From Above
            recurse(i, j - 1),     # From Left
            recurse(i - 1, j - 1), # From Diagonal
        )

        return memory[i][j]

    # Measure running time for full call
    start = timer()
    result = recurse(m_minus_one, n_minus_one)
    end = timer()

    # Return and print
    print("Running Time: ", end - start)
    return result


# function header for Q4.3 (Auto & manual grading)
# Bottom-up DP. Return the minimum cost and print running time.
# costs       -> list of lists (2D cost array)
# m_minus_one -> row index of destination (M-1)
# n_minus_one -> col index of destination (N-1)
# return      -> integer (minimum cost)
#
# Include comments on key lines of code to demonstrate your comprehension.
#
# AI Tool Used: <Chat GPT 5.2>
# Interaction: <Asked given the psudocode from class, how I am supposed to implement this approach>
# Verification: <Gave me more specific psuedocode for this case and I verified it with test cases before implementing myself.>
def min_cost_bottom_up(costs, m_minus_one, n_minus_one):

    # Get length of rows and columns
    rows = len(costs)
    cols = len(costs[0])

    start = timer()

    # Create DP table where dp[i][j] stores the minimum cost to reach cell (i, j)
    dp = [[0] * cols for _ in range(rows)]

    # Base Case: Starting Cell
    dp[0][0] = costs[0][0]

    # Fill the first row: can only come from the left
    for j in range(1, cols):
        dp[0][j] = dp[0][j - 1] + costs[0][j]

    # Fill in the first column: can only come from above
    for i in range(1, rows):
        dp[i][0] = dp[i - 1][0] + costs[i][0]

    # Fill in the rest of the table using recurrence
    for i in range(1, rows):
        for j in range(1, cols):
            dp[i][j] = costs[i][j] + min(
                dp[i - 1][j],    # From Above
                dp[i][j - 1],    # From Left
                dp[i - 1][j - 1] # From Diagonal
            )

    end = timer()
    print("Running Time: ", end - start)

    return dp[m_minus_one][n_minus_one]


# function header for Q4.4 (Manual grading — printed output evaluated)
# Reconstruct and print the minimum cost path, e.g., (0,0)->(0,1)->...
# Re-use min_cost_bottom_up inside this wrapper.
# costs       -> list of lists (2D cost array)
# m_minus_one -> row index of destination (M-1)
# n_minus_one -> col index of destination (N-1)
# return      -> N/C
#
# AI Tool Used: <Chat GPT 5.2>
# Interaction: <Asked how I would go about determining what direction we should choose>
# Verification: <Went through lots of tests and example inputs and outputs to verify the logic.>
def min_cost_path_wrapper(costs, m_minus_one, n_minus_one):

    # Get rows and columns from length of costs
    rows = len(costs)
    cols = len(costs[0])

    # Build same DP table as in min_cost_bottom_up
    # dp[i][j] stores the min cost required to reach cell (i, j)
    dp = [[0] * cols for _ in range(rows)]

    # Base Case: Starting Cell
    dp[0][0] = costs[0][0]

    # Fill the first row (can only move right)
    for j in range(1, cols):
        dp[0][j] = dp[0][j - 1] + costs[0][j]
    
    # Fill the first column (can only move down)
    for i in range(1, rows):
        dp[i][0] = dp[i - 1][0] + costs[i][0]

    # Fill remaining DP table using the recurrence relation
    for i in range(1, rows):
        for j in range(1, cols):
            dp[i][j] = costs[i][j] + min(
                dp[i - 1][j],    # From Above
                dp[i][j - 1],    # From Left
                dp[i - 1][j - 1] # From Diagonal
            )
    
    # Backtrack to reconstruct the path
    i = m_minus_one
    j = n_minus_one
    path = []

    while i > 0 or j > 0:
        path.append((i, j))

        # If we are in the first row, we must have to come from the left
        if i == 0:
            j -= 1

        # If we are in the first column, we must come from above
        elif j == 0:
            i -= 1
        
        else:
            # Choose the direction that produced the minimum
            if dp[i - 1][j - 1] <= dp[i - 1][j] and dp[i - 1][j - 1] <= dp[i][j - 1]:
                i -= 1
                j -= 1
            elif dp[i - 1][j] <= dp[i][j - 1]:
                i -= 1
            else:
                j -= 1
    
    # Add the starting cell
    path.append((0,0))

    # Reverse so it prints from start to destination
    path.reverse()

    # Print path in required format
    print("->".join(f"({r},{c})" for r, c in path))


# ============================================================================
# Q5. Matrix-Chain Multiplication
# ============================================================================
# Given dimension array q where matrix A_i has dimensions q[i-1] x q[i],
# find the most efficient way to multiply the chain to minimize total scalar
# multiplications.
#
# Recurrence:
#   m[i,j] = 0                                                    if i == j
#   m[i,j] = min_{i<=k<j} { m[i,k] + m[k+1,j] + q[i-1]*q[k]*q[j] }  if i < j

# function header for Q5.1 (Auto & manual grading)
# Top-down DP (memoized recursion). Return the minimum scalar multiplications.
# q -> list of matrix dimensions
# i -> start matrix index (1-indexed)
# j -> end matrix index (1-indexed)
# return -> integer (minimum number of scalar multiplications)
#
# Ex: q=[9,46,4,18,21,40,19,25,14,37,33], i=1, j=10 → 21012
#
# Include comments on key lines of code to demonstrate your comprehension.
#
# AI Tool Used: <Chat GPT 5.2>
# Interaction: <Asked for help getting the equation to calculate cost recursively.>
# Verification: <Verified with the slides that we have, and also with test cases.>
def matrix_chain_top_down(q, i, j):

    # Number of matricies
    n = len(q) - 1

    # Create memory table where memory[a][b] stores the min cost for A_a ... A_b
    memory = [[None] * (n + 1) for _ in range(n + 1)]

    def recurse(i, j):

        # Base Case: One matrix alone needs no multiplication
        if i == j:
            return 0
        
        # Memorization check: return saved answer if already computed
        if memory[i][j] is not None:
            return memory[i][j]
        
        # Start with infinity so any real multiplication cost will be smaller 
        min_cost = float('inf')

        # Try every possible split point k between i and j
        for k in range(i , j):
            cost = (
                recurse(i, k) +
                recurse(k + 1, j) + 
                q[i - 1] * q[k] * q[j]
            )

            # Keep the smallest total cost among all possible splits
            if cost < min_cost:
                min_cost = cost
        
        # Save computed results before returning
        memory[i][j] = min_cost
        return memory[i][j]

    return recurse(i, j)


# function header for Q5.2 (Auto & manual grading)
# Bottom-up DP. Return TWO arrays as a tuple: the cost matrix m and the
# split index matrix s.
# q -> list of matrix dimensions
# return -> tuple (m, s)
#   m: 2D list where m[i][j] = min scalar multiplications for A_i..A_j
#   s: 2D list where s[i][j] = split index k that achieves m[i][j]
#
# Ex: q=[9,46,4,18,21,40,19,25,14,37,33] → m, s
#
# Include comments on key lines of code to demonstrate your comprehension.
#
# AI Tool Used: <Chat GPT 5.2>
# Interaction: <Asked how I am supposed to go about calculating the cost. Asked it to verify the equation for me/>
# Verification: <Ran through test and edge cases to verify the equation it gave me.>
def matrix_chain_bottom_up(q):

    # Number of matrices in the chain
    n = len(q) - 1

    # m[i][j] stores the minimum multiplication cost for A_i ... A_j
    m = [[0] * (n + 1) for _ in range(n + 1)]

    # s[i][j] stores the split index k that gives the optimal cost
    s = [[0] * (n + 1) for _ in range(n + 1)]

    # Chain Length l goes from 2 matrices up to n matrices
    for l in range(2, n + 1):

        # i is the starting matrix index of subchain
        for i in range(1, n - l + 2):

            # Ending matrix index of the subchain
            j = i + l - 1

            # Initialize with infinity so any real cost wil be smaller
            m[i][j] = float('inf')

            # Try every possible split point k between i and j
            for k in range(i, j):
                cost = (
                    m[i][k] +               # Cost of left subchain A_i ... A_k
                    m[k + 1][j] +           # Cost of right subchain A_(k+1) ... A_j
                    q[i - 1] * q[k] * q[j]  # Cost of multiplying the two results
                )

                # If this split gives a smaller cost, save it
                if cost < m[i][j]:
                    m[i][j] = cost
                    s[i][j] = k

    return (m, s)


# function header for Q5.3 (Auto & manual grading)
# Reconstruct the optimal full parenthesization as a string.
# Re-use matrix_chain_bottom_up inside this wrapper.
# q      -> list of matrix dimensions
# matrix -> list of matrix name strings, e.g., ['A1','A2',...,'A10']
# return -> string, e.g., "((A1A2A3)(A4A5))"
#
# Rules:
#   - Use '(' and ')' instead of '{' '}'
#   - Enclose the outermost product in parentheses
#   - No spaces between characters
#
# Ex: q=[9,46,4,18,21,40,19,25,14,37,33],
#     matrix=['A1','A2','A3','A4','A5','A6','A7','A8','A9','A10']
#
# AI Tool Used: <Chat GPT 5.2>
# Interaction: <Asked to ensure that I can re-use the helper function for building the bottom up matrix>
# Verification: <Verified that I could do this and it would work correctly, tried some test cases to verify.>
def matrix_chain_parenthesization(q, matrix):

    # Re use the bottom up DP function to get the spit matrix
    m, s = matrix_chain_bottom_up(q)

    # Heper function to recursively build the parenthesization
    def build(i, j):

        # Base Case: A single matrix doesn't need parentheses by itself
        if i == j:
            return matrix[i - 1]
        
        # Recursively build the left and right sub chains using the optimal split
        k = s[i][j]
        left = build(i, k)
        right = build(k + 1, j)

        # Ensure the product is in parentheses
        return "(" + left + right + ")"
    
    # Number of matricies
    n = len(matrix)

    # Build the full parenthesization from A1 to An
    return build(1, n)


# ============================================================================
# Q6. Rod Cutting
# ============================================================================
# Given a rod of length n and price array p (p[i] = price for length i, p[0]=0),
# find the maximum revenue obtainable by cutting and selling the rod.
#
# Optimal substructure: r[n] = max_{1<=i<=n} (p[i] + r[n-i])

# function header for Q6.1 (Auto & manual grading)
# Top-down DP (memoized recursion). Return the maximum revenue for a rod of length n.
# p -> list, p[i] = price for rod of length i (p[0] = 0)
# n -> integer (rod length)
# return -> integer (maximum revenue)
#
# Ex: p=[0,1,5,8,9,10,17,17,20,24,30], n=4 → 10
#
# Include comments on key lines of code to demonstrate your comprehension.
#
# AI Tool Used: <Chat GPT 5.2>
# Interaction: <How can I set something to negative infinity?>
# Verification: <Told me that you can set something to the most negative number by doing float('-inf'), verified it worked with online docs>
def rod_cut_top_down(p, n):

    # Memory[i] stores the max revenue for a rod of length i
    memory = [None] * (n + 1)

    def recurse(length):

        # Base Case: A rod of length 0 gives 0 revenue
        if length == 0:
            return 0

        # Memorization Check: Return saved answer if already computed
        if memory[length] is not None:
            return memory[length]
    
        # Start with negative infinity so any real revenue will be larger
        max_revenue = float('-inf')

        # Try every possible first cut length from 1 to current rod length
        for i in range(1, length + 1):
            revenue = p[i] + recurse(length - i)

            # Keep the best revenue amost all possible first cuts
            if revenue > max_revenue:
                max_revenue = revenue
            
        # Save the computed answer before returning it
        memory[length] = max_revenue
        return memory[length]

    return recurse(n)


# function header for Q6.2 (Auto & manual grading)
# Bottom-up DP. Return TWO arrays as a tuple: the revenue array r and
# the cuts array s.
# p -> list, p[i] = price for rod of length i (p[0] = 0)
# return -> tuple (r, s)
#   r: list where r[i] = max revenue for rod of length i
#   s: list where s[i] = size of the first cut for rod of length i
#
# Ex: p=[0,1,5,8,9,10,17,17,20,24,30] → r, s
#
# Include comments on key lines of code to demonstrate your comprehension.
#
# AI Tool Used: <tool name or "None">
# Interaction: <description of how the AI tool was used, e.g., prompts given>
# Verification: <how you verified the correctness of the AI-generated code>
def rod_cut_bottom_up(p):

    # Length of rod (max length we care about)
    n = len(p) - 1

    # r[i] stores the max revenue obtainable for rod length i
    r = [0] * (n + 1)

    # s[i] stores the size of the first cut that achieves the optimal revenue
    s = [0] * (n + 1)

    # Build the solution bottom up from rod length 1 to n 
    for j in range(1, n + 1):

        # start with negative infinity so any real revenue will be greater
        max_revenue = float('-inf')

        # Try every possible first cut length
        for i in range(1, j + 1):
            
            revenue = p[i] + r[j - i]

            # If this cut gives a better revenue, update
            if revenue > max_revenue:
                max_revenue = revenue
                s[j] = i # Record the first cut size
        
        # Store the best revenue for rod length j 
        r[j] = max_revenue

    return (r, s)


# function header for Q6.3 (Auto & manual grading)
# Reconstruct and return the optimal list of cuts as a sorted Python list.
# Re-use rod_cut_bottom_up inside this wrapper.
# p -> list, p[i] = price for rod of length i (p[0] = 0)
# n -> integer (rod length)
# return -> sorted list of cut sizes
#
# Ex: p=[0,1,5,8,9,10,17,17,20,24,30], n=7 → [1, 6]
#     p=[0,1,5,8,9,10,17,17,20,24,30], n=5 → [2, 3]
#
# Include comments on key lines of code to demonstrate your comprehension.
#
# AI Tool Used: <Chat GPT 5.2>
# Interaction: <Again asked if it would be okay to re-use the bottom up dp function to get the revenue and cut arrays>
# Verification: <It verified with me that this would work and I could use it, I tested it with some manual test cases.>
def rod_cut_reconstruct(p, n):

    # Re-use the bottom up DP function to obtain revenue and cut arrays
    r, s = rod_cut_bottom_up(p)

    cuts = []

    # Reconstruct cuts by repeatedly taking the first optimal cut
    while n > 0:
        cut = s[n] # Size of the first cut for rod length n
        cuts.append(cut)
        n -= cut   # Reduce remaining rod length

    # Return the cuts sorted as required
    return sorted(cuts)


# ============================================================================
# Q7. Slice, Sort, and Pick K-th
# ============================================================================
# function header for Q7 (Auto & manual grading)
# array    -> list of integers, e.g., [1, 5, 2, 6, 3, 7, 4]
# commands -> 2D list, each row = [i, j, k] (all 1-indexed)
# return   -> list of k-th elements, one per command
#
# For each command [i, j, k]:
#   1. Slice array from the i-th to j-th element (1-indexed, inclusive).
#   2. Sort the slice in ascending order (no built-in sort functions).
#   3. Return the k-th element (1-indexed) of the sorted slice.
#
# Ex: array=[1,5,2,6,3,7,4], commands=[[2,5,3],[4,4,1],[1,7,3]] → [5, 6, 3]
#
# Constraints:
#   1 <= len(array) <= 100,  1 <= array[i] <= 100
#   1 <= len(commands) <= 50
#   1 <= i <= j <= len(array),  1 <= k <= j-i+1
#
# Include comments on key lines of code to demonstrate your comprehension.
#
# AI Tool Used: <Chat GPT 5.2>
# Interaction: <How should I go about sorting the arrays that are sliced?>
# Verification: <Suggested that I use a helper function with insertion sort, I tested it with some test cases and it worked.>
def slice_sort_kth(array, commands):

    # Helper function: Insertion sort in ascending order
    def insertion_sort(arr):

        # Iterate through the array starting from the second element
        for i in range(1, len(arr)):
            key = arr[i]    # Current value to insert into the sorted portion
            j = i - 1

            # Shift larger elements one position to the right
            while j >= 0 and arr[j] > key:
                arr[j + 1] = arr[j]
                j -= 1

            # Place the key into its correct sorted position
            arr[j + 1] = key

        return arr
    
    result = []

    # Process each command [i, j, k]
    for command in commands:
        i, j, k = command

        # Slice from i-th to j-th element (convert 1 index to python index)
        subarray = array[i - 1:j]

        # Sort the sliced subarray in ascending order
        sorted_subarray = insertion_sort(subarray)

        # Append the k-th element of the sorted subarray (1-indexed)
        result.append(sorted_subarray[k - 1])

    return result


# ============================================================================
# Q8. Data Filtering and Sorting
# ============================================================================
# function header for Q8 (Auto & manual grading)
# data    -> 2D list, each row = [code, date, maximum, remain]
# ext     -> field name to filter on ("code", "date", "maximum", "remain")
# val_ext -> threshold; keep only rows where data[i][ext] < val_ext
# sort_by -> field name to sort the filtered result by (ascending)
# return  -> filtered and sorted 2D list
#
# Steps:
#   1. Filter: keep rows where data[i][ext] < val_ext.
#   2. Sort filtered rows by sort_by in ascending order.
#
# Ex: data=[[1,20300104,100,80],[2,20300804,847,37],[3,20300401,10,8]],
#     ext="date", val_ext=20300501, sort_by="remain"
#     → [[3,20300401,10,8],[1,20300104,100,80]]
#
# Constraints:
#   1 <= len(data) <= 500
#   ext and sort_by are each one of: "code", "date", "maximum", "remain"
#   No two rows share the same value for sort_by
#   At least one row always satisfies the filter condition
#
# Include comments on key lines of code to demonstrate your comprehension.
#
# AI Tool Used: <Chat GPT 5.2>
# Interaction: <Asked to verify if using a dict for holding the fields would be the correct and most time efficient way of completing this.>
# Verification: <Told me that a dictonary is the correct way to map these values and I ensured it worked with some test cases.>
def filter_and_sort(data, ext, val_ext, sort_by):

    # Map field names to their corresponding column indices
    fields = {
        "code": 0,
        "date": 1,
        "maximum": 2,
        "remain": 3
    }

    ext_index = fields[ext]
    sort_index = fields[sort_by]

    # Filter rows where the selected field is less than val_ext
    filtered = []
    for row in data:
        if row[ext_index] < val_ext:
            filtered.append(row)
    
    # Sort filtered rows by sort_by field using insertion sort
    for i in range(1, len(filtered)):
        key_row = filtered[i]
        j = i - 1

        # Shift rows with larger sort values to the right
        while j >= 0 and filtered[j][sort_index] > key_row[sort_index]:
            filtered[j + 1] = filtered[j]
            j -= 1
        
        # Insert the row in its correct position
        filtered[j + 1] = key_row

    return filtered


# ============================================================================
# Main - Test Section
# ============================================================================
if __name__ == "__main__":
    # You can test your code here
    # This section will not be evaluated by Gradescope
    pass

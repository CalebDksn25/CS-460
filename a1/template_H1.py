# Do not change the filename or function headers
# You are free to add helper functions
# note: you will only have 5 attempts to run the autograder

import numpy as np
from timeit import default_timer as timer
# import plot lib. to plot results.
# you may need to install matplotlib by typing "python3 -m pip install -U matplotlib" to test in your local machine
import matplotlib.pyplot as plt


# ============================================================================
# Q1. Count long subarrays
# ============================================================================
# function header for Q1 (Auto & manual grading)
# A -> list of integers
# return -> integer (count of longest increasing subarrays)
#
# An increasing subarr ay is any consecutive sequence of array integers whose values strictly increase.
# Return the number of longest increasing subarrays of A.
#
# Ex: A = (1,3,4,2,7,5,6,9,8), return 2
#     (longest increasing subarrays are (1,3,4) and (5,6,9), both length 3)
#
# AI Tool Used: <tool name or "None">
# Interaction: <description of how the AI tool was used, e.g., prompts given>
# Verification: <how you verified the correctness of the AI-generated code>
def count_long_subarrays(A):
    current_longest = 1
    longest = 0
    count = 0
    n = len(A)

    # Base Cases
    if n == 0:
        return 0

    # Go through the array and count the longest increasing subarrays
    for i in range(1, n):
        # If the current element is greater than the previous element, increase current longest
        if A[i] >A[i-1]:
            current_longest += 1
        else:
            # Compare the current longest to the longest found so far
            if current_longest > longest:
                longest = current_longest
                count = 1
            elif current_longest == longest:
                count += 1

            # Reset the current longest
            current_longest = 1
    
    # After the loop, we need to check the last increasing subarray
    if current_longest == longest:
        count += 1
    elif current_longest > longest:
        longest = current_longest
        count = 1

    return count


# ============================================================================
# Q2. Insertion sort
# ============================================================================
# function header for Q2.1 (Auto & manual grading)
# input_list -> list of integers
# return -> list of integers
#
# note: tested input will be unordered random lists from size n=1 to n=1000
# each test input is randomized, so it is possible to pass a test once and fail the next attempt
#
# AI Tool Used: <tool name or "None">
# Interaction: <description of how the AI tool was used, e.g., prompts given>
# Verification: <how you verified the correctness of the AI-generated code>
def insertion_sort(input_list):

    n = len(input_list)

    for i in range(1, n):
        key = input_list[i]
        # Insert A[i] into the sorted sequence
        j = i - 1
        while j >= 0 and input_list[j] > key:
            input_list[j + 1] = input_list[j]
            j = j - 1
        
        input_list[j + 1] = key

    return input_list


# function header for Q2.2 (Manual grading)
# note: no inputs and outputs are needed; Q3.2 will be manually graded
# note: this should have no errors
#
# AI Tool Used: <Chat GPT 5.2>
# Interaction: <I uploaded my provided code which was just the random time, and asked the ensure I have satisfied all of the requirements for this question. I found out I still needed to implement the ascending and decending so I did that. >
# Verification: <I looked back over thee question requirements and realized that I was missing the ascending and descending times, so I added them.>
def q2_2():
    # generate inputs, e.g., when n=100, n=1000, n=2000, ..., n=5000
    size = [100, 1000, 2000, 3000, 4000, 5000]

    # generate different types of inputs
    random_set, asc_set, dsc_set = [], [], []
    for i in range(0, len(size)):
        random_set.append(np.random.randint(0, 1000000, size[i]))
        asc_set.append(np.arange(0, size[i]))
        dsc_set.append(np.arange(size[i], 0, -1))

    # measure running time for the types of inputs and save it to the following three arrays
    elapsed_time_random, elapsed_time_asc, elapsed_time_dsc = [], [], []
    ''' Write your codes to measure running time of sorting algorithms '''
    ''' Hint: you can use "start = timer()" and "end = timer()", then "end - start" to get running time '''
    ''' write your answers (codes/texts) from here '''

    # For each size
    for i in range(0, len(size)):

        # Random Time
        arr_copy = random_set[i].copy()
        start = timer()
        insertion_sort(arr_copy)
        end = timer()
        elapsed_time_random.append(end - start)

        # Ascending Time
        arr_copy = asc_set[i].copy()
        start = timer()
        insertion_sort(arr_copy)
        end = timer()
        elapsed_time_asc.append(end - start)

        # Descending Time
        arr_copy = dsc_set[i].copy()
        start = timer()
        insertion_sort(arr_copy)
        end = timer()
        elapsed_time_dsc.append(end - start)


    ''' end your answers '''

    # plot the running time results
    plt.plot(size, elapsed_time_random, color='blue', label='Random input')
    plt.plot(size, elapsed_time_asc, color='red', label='asc-case')
    plt.plot(size, elapsed_time_dsc, color='green', label='dsc-case')
    plt.title("Running time of algorithms")
    plt.xlabel("Input size")
    plt.ylabel("Running time")
    plt.grid(True)
    plt.legend()
    plt.savefig('q2_2.png')
    plt.show()

# function header for Q2.3 (Manual grading)
# note: no inputs and outputs are needed
#
# AI Tool Used: <tool name or "None">
# Interaction: <description of how the AI tool was used, e.g., prompts given>
# Verification: <how you verified the correctness of the AI-generated code>
def q2_3():

    """
    Answer:
    From the experimental results in Q2.2, we can see that the running time of for ascending input grows much slower than the other two cases. This matches
    the theoretical best case time complexity for insertion sort, which is O(n), because the inner while loop rarely executes when the list is already sorted.

    For random input, the running time grows aproximately quadratically, which matches the average case time complexity of O(n^2). Many elements need to be shifted
    during insertion.

    For descending input, the running time is the largest and also grows quadratically. This corresponds to the worst case time complexity of O(n^2), since 
    each element much be compred with and shifted past all previously sorted elements.

    Therefore, the experimental results are consistent with the asymptotic time complexities of insertion sort: best case O(n), average case O(n^2), and worst O(n^2).
    """

# ============================================================================
# Q3. Merge sort
# ============================================================================
# function header for Q3.1 (Auto & manual grading)
# input_list -> list of integers
# return -> list of integers
#
# note: tested input will be unordered random lists from size n=1 to n=1000
# each test input is randomized, so it is possible to pass a test once and fail the next attempt
#
# AI Tool Used: <Chat GPT 5.2>
# Interaction: <I ensured that I was splitting the 2 halves correctly. I thought it would be left_half = input_list[:mid] and right_half = input_list[mid+1:], but I realized that this would skip the middle element, so I changed it to right_half = input_list[mid:].>
# Verification: <I tested the code on a few random lists and verified that it was sorting correctly. I also double checked that I was splitting the list correctly by printing out the left and right halves for a test input.>
def merge_sort(input_list):

    # Base Case (Already sorted / empty list)
    if len(input_list) <= 1:
        return input_list
    
    # Split the input into 2 halves
    mid = len(input_list) // 2
    left_half = input_list[:mid]
    right_half = input_list[mid:]

    # Recursively sort the halves
    left_sorted = merge_sort(left_half)
    right_sorted = merge_sort(right_half)

    # Merge the sorted halves
    return _merge(left_sorted, right_sorted)

def _merge(left, right):
    merged = []
    i = 0
    j = 0

    # Compare elements from the left and right, append the smaller
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
    
    # Append any remaining elements
    merged.extend(left[i:])
    merged.extend(right[j:])

    return merged

# function header for Q3.2 (Manual grading)
# note: no inputs and outputs are needed; Q4.2 will be manually graded
# note: this should have no errors
#
# AI Tool Used: <tool name or "None">
# Interaction: <description of how the AI tool was used, e.g., prompts given>
# Verification: <how you verified the correctness of the AI-generated code>
def q3_2():
    # generate inputs, e.g., when n=1000, n=10000, n=20000, ..., n=50000
    size = [1000, 10000, 20000, 30000, 40000, 50000]

    # generate different types of inputs
    random_set, asc_set, dsc_set = [], [], []
    for i in range(0, len(size)):
        random_set.append(np.random.randint(0, 1000000, size[i]))
        asc_set.append(np.arange(0, size[i]))
        dsc_set.append(np.arange(size[i], 0, -1))

    # measure running time for the types of inputs and save it to the following three arrays
    elapsed_time_random, elapsed_time_asc, elapsed_time_dsc = [], [], []
    ''' Write your codes to measure running time of sorting algorithms '''
    ''' Hint: you can use "start = timer()" and "end = timer()", then "end - start" to get running time '''
    ''' write your answers (codes/texts) from here '''

    # For each size
    for i in range(0, len(size)):

        # Random Time
        arr_copy = random_set[i].copy()
        start = timer()
        merge_sort(arr_copy)
        end = timer()
        elapsed_time_random.append(end - start)

        # Ascending Time
        arr_copy = asc_set[i].copy()
        start = timer()
        merge_sort(arr_copy)
        end = timer()
        elapsed_time_asc.append(end - start)

        # Descending Time
        arr_copy = dsc_set[i].copy()
        start = timer()
        merge_sort(arr_copy)
        end = timer()
        elapsed_time_dsc.append(end - start)

    ''' end your answers '''

    # plot the running time results
    plt.plot(size, elapsed_time_random, color='blue', label='Random input')
    plt.plot(size, elapsed_time_asc, color='red', label='asc-case')
    plt.plot(size, elapsed_time_dsc, color='green', label='dsc-case')
    plt.title("Running time of algorithms")
    plt.xlabel("Input size")
    plt.ylabel("Running time")
    plt.grid(True)
    plt.legend()
    plt.savefig("q3_2.png")
    plt.show()


# function header for Q3.3 (Manual grading)
# note: no inputs and outputs are needed
#
# AI Tool Used: <tool name or "None">
# Interaction: <description of how the AI tool was used, e.g., prompts given>
# Verification: <how you verified the correctness of the AI-generated code>
def q3_3():

    """
    Answer:
    From the results of 3.2, the running time for random, ascending, and descending inputs increased at a similar rate and are close to eachother.
    THsi matches the merge sort asymptotic behavior that we were expecting.

    Merge sort runs in Theta(n log n) time for the best, average, and worse cases. The aglorthm always splits the problem into 2 halves, and 
    produces a log n level of recursion and at each level the merge step processes all n elements, in total (O(n) work per level) Therefore, 
    the overall running time is Theta(n log n) for all cases whether the input is sorted, random, or reversed.
    """


# ============================================================================
# Q4. Sequence Operations
# ============================================================================
# Given a data structure D that supports the following Sequence operations:
#   - D.build(X): Initialize D with items from iterable X in O(n) time
#   - D.insert_at(i, x): Insert item x at index i in O(log n) time
#   - D.delete_at(i): Delete and return the item at index i in O(log n) time
#
# where n is the number of items stored in D at the time of the operation.
#
# Implement the following higher-level operations using only the provided
# lower-level operations. Each operation should run in O(k log n) time.
# ============================================================================

# Sequence data structure class (provided for testing - do not modify)
class Seq:
    def __init__(self):
        self.data = []

    def __repr__(self):
        return f"Seq({self.data})"

    def build(self, X):
        """Initialize the sequence with items from iterable X in O(n) time."""
        self.data = list(X)

    def insert_at(self, i, x):
        """Insert item x at index i in O(log n) time."""
        self.data.insert(i, x)

    def delete_at(self, i):
        """Delete and return the item at index i in O(log n) time."""
        return self.data.pop(i)

# function header for Q4.1 (Auto & manual grading)
# D -> Sequence data structure with build, insert_at, delete_at operations
# i -> starting index (integer)
# k -> number of items to reverse (integer)
# return -> None (modifies D in place)
#
# Reverse the order of the k items in D starting at index i (up to index i + k - 1).
#
# Ex: If D contains [a, b, c, d, e] and we call reverse(D, 1, 3),
#     then D should contain [a, d, c, b, e] (items at indices 1,2,3 are reversed)
#
# Note: You may only use D.insert_at(i, x) and D.delete_at(i) operations.
#       Do not use built-in reverse functions.
#
# AI Tool Used: <tool name or "None">
# Interaction: <description of how the AI tool was used, e.g., prompts given>
# Verification: <how you verified the correctness of the AI-generated code>
def reverse(D, i, k):

    temp = []

    # Remove k items starting at index i
    for _ in range(k):
        temp.append(D.delete_at(i))
    
    for x in temp:
        D.insert_at(i, x)

    return None


# function header for Q4.2 (Auto & manual grading)
# D -> Sequence data structure with build, insert_at, delete_at operations
# i -> starting index of items to move (integer)
# k -> number of items to move (integer)
# j -> destination index (integer)
# return -> None (modifies D in place)
#
# Move the k items in D starting at index i, in order, to be in front of the item at index j.
# Assume that the expression (i <= j < i + k) is always False.
#
# Ex: If D contains [a, b, c, d, e, f] and we call move(D, 1, 2, 5),
#     then D should contain [a, d, e, b, c, f] (items b,c moved in front of index 5)
#
# Note: You may only use D.insert_at(i, x) and D.delete_at(i) operations.
#       Do not use built-in functions for moving elements.
#
# AI Tool Used: <tool name or "None">
# Interaction: <description of how the AI tool was used, e.g., prompts given>
# Verification: <how you verified the correctness of the AI-generated code>
def move(D, i, k, j):

    temp = []

    # Extract
    for id in range(k):
        temp.append(D.delete_at(i))
    
    # Adjust destination index
    if i < j:
        j -= k
    
    #Insert
    for id in temp:
        D.insert_at(j, id)
        j += 1

    return None


# ============================================================================
# Q5. Shuffled sentence
# ============================================================================
# function header for Q5 (Auto & manual grading)
# sentence -> string
# return -> string
#
# Each word in s has a numerical suffix indicating its original 1-indexed position in the sentence.
# Your objective is to reconstruct and return the original sentence in the correct order.
#
# Ex: Input: s = "sentence4 a3 is2 This1", Output: "This is a sentence"
#
# note: Do not use built-in sort functions.
#
# Include comments on key steps in your implementation.
#
# AI Tool Used: <Chat GPT 5.2>
# Interaction: <Asked how I could input a random index into an array of n size for whatever word that was, helped me with the return statement.>
# Verification: <Went through some test cases and proved that it worked correctly + looking over online documentation as well.>
def correct_sentence(sentence):

    # Split the sentence into words
    words = sentence.split()

    # Get the number of words
    n = len(words)

    # Correct list
    ordered_words = [""] * n

    for word in words:
        # Get the position number at last index of that word
        position = int(word[-1])

        # Get the text without the number
        text = word[:-1]

        # Place the word into the correct position in ordered list
        ordered_words[position - 1] = text

    # Construct and return the full sentence
    return " ".join(ordered_words)


# ============================================================================
# Q6. Anagram Substring Count
# ============================================================================
# function header for Q6 (Auto & manual grading)
# A -> string (the string to search in)
# B -> string (the pattern string)
# return -> integer (count of substrings of A that are anagrams of B)
#
# String A is an anagram of another string B if A is a permutation of the letters in B.
# For example, (indicatory, dictionary) and (brush, shrub) are pairs of anagrams.
#
# The anagram substring count of B in A is the number of contiguous substrings of A
# (of length |B|) that are anagrams of B.
#
# Ex: A = "esleastealaslaet", B = "tesla"
#     Output: 3
#     Explanation: Of the 12 contiguous substrings of length 5 in A,
#     exactly 3 are anagrams of "tesla": "least", "steal", "slate"
#
# Note: Do not use built-in sort functions.
#
# Include comments on key steps in your implementation.
#
# AI Tool Used: <Chat GPT 5.2>
# Interaction: <Described my approach to the problem and confirmed that it would work. Helped get psudocode so I could implement the algorithm correctly.>
# Verification: <Went over multiple test cases of the algorithm to ensure that it was implemented correctly.>
def count_anagram_substrings(A, B):

    # If B is longer than A, theres no possible substrings
    if len(B) > len(A):
        return 0
    
    k = len(B)
    count = 0

    # Helped function to build frequency dictionary
    def build_freq(s):
        freq = {}
        for char in s:
            freq[char] = freq.get(char, 0) + 1
        return freq

    # Frequency of B
    target = build_freq(B)
    
    # Frequency of first window in A
    window = build_freq(A[:k])

    # Check first window
    if window == target:
        count += 1
    
    # Slide the window
    for i in range(k, len(A)):
        # Add new character
        new_char = A[i]
        window[new_char] = window.get(new_char, 0) + 1

        # Remove old characters
        old_char = A[i - k]
        window[old_char] -= 1

        # Remove key if count becomes 0
        if window[old_char] == 0:
            del window[old_char]
        
        # Compare frequencies
        if window == target:
            count += 1

    return count


# ============================================================================
# Q7. Find string
# ============================================================================
# function header for Q7 (Auto & manual grading)
# strings -> list of strings
# parts -> list of [start, end (exclusive)]
# return -> string
#
# Your objective is to extract the specified substrings from each string in my_strings according to parts
# and concatenate them in order to form a final string.
#
# Ex: my_strings = ["progressive", "hamburger", "hammer", "ahocorasick"]
#     parts = [[0, 4], [1, 2], [3, 5], [7, 7]]
#     Output: "programmers"
#
# note: Do not use built-in substring extraction functions
#
# Include comments on key steps in your implementation.
#
# AI Tool Used: <tool name or "None">
# Interaction: <description of how the AI tool was used, e.g., prompts given>
# Verification: <how you verified the correctness of the AI-generated code>
def find_string(strings, parts):

    # Hold all characters we want in order
    results_chars = []

    # Go through each string and its corresponding [start, end] part
    for idx in range(len(strings)):
        s = strings[idx]
        start = parts[idx][0]
        end = parts[idx][1] 

        # Copy characters from s[start] till s[end-1]
        for pos in range(start, end + 1):
            results_chars.append(s[pos])

    # Combins all collected characters into final string
    return "".join(results_chars)


# ============================================================================
# Main - Test Section
# ============================================================================
if __name__ == "__main__":
    # You can test your code here
    # This section will not be evaluated by Gradescope

    # Ex) 
    D6 = Seq()
    D6.build(['a', 'b', 'c', 'd', 'e', 'f'])
    print(f"\nBefore: {D6}")

    q2_2()
    q3_2()
    
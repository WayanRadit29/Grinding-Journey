# 📝 Data Structures Lab - Problem Recap and Implementation

This document summarizes the lab problems implemented in various `.py` files, along with brief descriptions, examples, and key topics covered. The goal is to ensure that each file is well-documented as part of the *Grinding Journey* repository.

---

## 🔹 Upacara Bendera

**Description:**  
For each element in the array, find the **index of the previous element to the left** that has a **greater value**. If none exists, return `-1`.

**Example Input:**
6 5 1 2 3 1 4

**Example Output:**
-1 0 2 3 2 3


**Explanation:**
- Index 1 → value 1 → greater on the left = 5 (index 0)
- Index 2 → value 2 → 1 (index 1) is smaller → fallback to 5 (index 0)
- And so on...

**Data Structure Used:**
- Stack (to track potential previous greater elements)

**Topics Covered:**
- Stack
- Nearest Greater to Left (NGL)
- Monotonic Stack Pattern

## 🔹 Baris Berbaris

**Description:**  
Simulate a queue of `N` people. On **odd-numbered turns**, move the person at the front of the queue to the back. On **even-numbered turns**, remove the person at the front and add them to the output. Repeat this process until the queue is empty.

**Example Input:**
5

**Example Output:**
2 4 1 5 3


**Explanation:**
Initial queue: 1 2 3 4 5  
- Turn 1 (odd): 1 → move to back → [2 3 4 5 1]  
- Turn 2 (even): 2 → removed → output = [2]  
- Continue this pattern...

**Data Structure Used:**
- `deque` (double-ended queue)

**Topics Covered:**
- Queue
- Simulation
- Modulo logic for alternating behavior

## 🔹 Ucup Melawan Iblis

**Description:**  
Ucup faces a series of enemies, each with a certain strength. For each enemy, he wants to know **how many days** (index difference) it takes until he encounters a **stronger enemy** in the future. If no stronger enemy exists, the answer is `0`.

**Example Input:**
6 2 1 5 3 6 2

**Example Output:**
2 1 2 1 0 0


**Explanation:**
- At index 0 (value 2), next stronger is at index 2 → 2 days
- At index 1 (value 1), next stronger is at index 2 → 1 day
- At index 2 (value 5), next stronger is at index 4 → 2 days
- And so on...

**Data Structure Used:**
- Stack (monotonic decreasing stack)

**Topics Covered:**
- Stack
- Next Greater Element with distance
- Index tracking

## 🔹 Jelly and the Plushie Tree

**Description:**  
Jelly owns a collection of Momonga plushies, each with a unique or duplicate ID. He stacks them into a tree-like structure based on their relationships. If the **sum of IDs in a subtree exceeds an obsession threshold `X`**, Jelly flips (reverses) that subtree. After all transformations, print the BFS (level-order) traversal of the tree.

**Example Input:**
7 10
5 2 3 8 1 6 7
0 1
0 2
0 3
1 4
3 5
3 6


**Example Output:**
5 8 3 2 7 6 1


**Explanation:**
- Build tree from the given edges using an adjacency list.
- Identify root node from the parent-child input.
- If a subtree has a sum > X, reverse its child order.
- Traverse the final tree using BFS.

**Data Structure Used:**
- Dictionary (Adjacency List for Tree)
- Queue for BFS

**Topics Covered:**
- Tree construction
- BFS traversal
- Subtree sum and transformation



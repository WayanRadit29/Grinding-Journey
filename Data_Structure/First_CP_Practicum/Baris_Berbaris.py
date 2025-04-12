# 🔹 Problem: Baris Berbaris
# 🔗 Link: -
# 🧠 Approach: Simulate a queue using deque. On odd turns, move the front element to the back. On even turns, remove the front element and append it to the output. Repeat until the queue is empty.
# 💡 Status: Solved ✅

from collections import deque

# Input: number of people in the line
N = int(input())

# Initialize queue and output list
queue = deque()
output = []

# Fill the queue with numbers from 1 to N
for i in range(1, N + 1):
    queue.append(i)

# Simulate the process based on odd/even turn
i = 1
while queue:
    if i % 2 == 1:
        # Odd turn: move the front element to the back
        a = queue.popleft()
        queue.append(str(a))
    else:
        # Even turn: remove the front element to output
        b = queue.popleft()
        output.append(str(b))
    i += 1

# Print the final output
print(' '.join(output))

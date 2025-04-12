# 🔹 Problem: Upacara Bendera
# 🔗 Link: -
# 🧠 Approach: Use a stack to store indices of previous elements. For each element, find the index of the closest greater element on the left. If none, append -1.
# 💡 Status: Solved ✅

# Input: number of elements and the array
N = int(input())
store = list(map(str, input().split()))
stack = []
output = ['-1']  # The first child has no protector

# Process to find nearest greater to left
for i in range(len(store)):
    if stack:
        # Remove all smaller or equal elements from the stack
        while stack and store[stack[-1]] <= store[i]:
            stack.pop()
        if stack:
            output.append(str(stack[-1]))  # Nearest greater to left found
        else:
            output.append('-1')  # No greater element found
        stack.append(i)
    else:
        stack.append(i)

# Print final output
print(' '.join(output))

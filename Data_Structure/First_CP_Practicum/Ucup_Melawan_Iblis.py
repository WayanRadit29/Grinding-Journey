# 🔹 Problem: Ucup Melawan Iblis
# 🔗 Link: -
# 🧠 Approach: Use a stack to track indices of previous enemies. For each enemy, if the current one is stronger, pop from the stack and calculate the number of days it took to meet a stronger enemy.
# 💡 Status: Solved ✅

# Input: number of enemies and their respective strength levels
N = int(input())
simpan = list(map(int, input().split()))
stack = []
output = ['0'] * len(simpan)  # Default: 0 days if no stronger enemy ahead

# Iterate through all enemies
for i in range(len(simpan)):
    if stack:
        # Pop all weaker enemies and compute how many days passed
        while stack and simpan[stack[-1]] < simpan[i]:
            a = stack.pop()
            output[a] = str(i - a)
        stack.append(i)
    else:
        stack.append(i)

# Print the result: number of days to meet a stronger enemy
print(' '.join(output))

# 🔹 Problem: Stock Span Problem
# 🔗 Link: https://www.geeksforgeeks.org/the-stock-span-problem/
# 🧠 Approach: Use a stack to track previous indices with higher stock prices
# 💡 Status: Solved ✅

class Solution:
    def calculateSpan(self, arr):
        # We use a stack to store the indices of previous days with higher stock prices.
        stack = []
        
        # output[i] stores how many consecutive days (including today)
        # the stock price has been less than or equal to today's price.
        output = [0] * len(arr)
        
        # The span of the first day is always 1
        output[0] = 1
        stack.append(0)  # Push the index of the first day

        # Iterate through the rest of the days
        for i in range(1, len(arr)):
            # Pop all elements from the stack while the price at the top
            # of the stack is less than or equal to the current day's price
            while stack and arr[stack[-1]] <= arr[i]:
                stack.pop()
            
            # If the stack is empty, it means all previous prices were less,
            # so the span is the entire range till now
            if not stack:
                output[i] = i + 1
            else:
                # Otherwise, span is the difference between current day and
                # the last day with a higher price
                output[i] = i - stack[-1]
            
            # Push current day's index to the stack
            stack.append(i)
        
        return output

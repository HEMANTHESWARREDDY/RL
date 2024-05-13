def minimize_travel_time_dp(n, goal):
    # Initializing an array to store the minimum time to reach each block
    dp = [float('inf')] * (n + 1)
    dp[1] = 0  # Minimum time to reach block 1 is 0

    # Dynamic Programming to calculate the minimum travel time
    for i in range(1, n):
        dp[i + 1] = min(dp[i + 1], dp[i] + 1)  # Walking to the next block takes 1 minute
        dp[min(2*i, n)] = min(dp[min(2*i, n)], dp[i] + 2)  # Taking a magic tram takes 2 minutes

    return dp[goal]

# Calculate the time and space complexity
# Time complexity: O(n)
# Space complexity: O(n)

n = 10  # Number of blocks
goal_block = 6  # Goal block
result_dp = minimize_travel_time_dp(n, goal_block)
print("Minimum travel time to reach block", goal_block, "is", result_dp-1, "minutes.")
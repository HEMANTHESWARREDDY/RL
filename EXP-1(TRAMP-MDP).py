import numpy as np

def minimize_travel_time(n, goal):
    # Create a transition probability matrix
    P = np.zeros((n + 1, n + 1))
    print(P)
    for i in range(1, n):
        print(i)
        P[i, i + 1] = 0.5  # Walking from i to i+1
        P[i, min(2*i, n)] = 0.5  # Taking a magic tram from i to min(2i, n)

    # Value iteration to calculate the minimum travel time
    V = np.zeros(n + 1)
    theta = 1e-5  # Convergence threshold
    discount = 1.0  # No discount for immediate rewards

    while True:
        delta = 0
        for s in range(1, n):
            v = V[s]
            V[s] = np.max([1 + discount * np.dot(P[s, :], V)])
            delta = max(delta, abs(v - V[s]))
        if delta < theta:
            break

    return int(V[goal])

n = int(input("Enter no.of Blocks: "))
goal_block = int(input("Enter the Goal Block: "))


# Goal block
result = minimize_travel_time(n, goal_block)
print("Minimum travel time to reach block", goal_block, "is", result, "minutes.")
import numpy as np

# Define parameters
alpha = 0.1  # Learning rate
gamma = 0.9  # Discount factor
epsilon = 0.1  # Epsilon-greedy exploration rate
num_episodes = 1000  # Number of episodes

# Define state space
states = ['Round 1', 'Round 2', 'Round 3', 'Round 4']

# Define action space
actions = ['quit', 'stay_correct', 'pass']

# Initialize Q-values
Q = {(s, a): 0 for s in states for a in actions}

# Define sequence of utilities for each action in each state
utilities = {
    'Round 1': {'quit': 5000, 'stay_correct': 20000, 'pass': -2000},
    'Round 2': {'quit': 5000, 'stay_correct': 20000, 'pass': -2000},
    'Round 3': {'quit': 5000, 'stay_correct': 20000, 'pass': -2000},
    'Round 4': {'quit': 5000, 'stay_correct': 20000, 'pass': -2000}
}

# Q-learning algorithm
for episode in range(num_episodes):
    # Initialize state
    state = 'Round 1'
    
    # Execute episode
    while state != 'Round 4':
        # Choose action using epsilon-greedy policy
        if np.random.rand() < epsilon:
            action = np.random.choice(actions)
        else:
            action = max(actions, key=lambda a: Q[(state, a)])
        
        # Take action and observe next state
        next_state = states[states.index(state) + 1]
        
        # Observe utility for the chosen action in the current state
        utility = utilities[state][action]
        
        # Update Q-value
        Q[(state, action)] += alpha * (utility + gamma * max(Q[(next_state, a)] for a in actions) - Q[(state, action)])
        
        # Transition to next state
        state = next_state

# Print learned Q-values
print("Learned Q-values:")
for state in states:
    for action in actions:
        print(f"Q({state}, {action}) = {Q[(state, action)]}")
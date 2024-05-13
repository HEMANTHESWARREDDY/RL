import numpy as np

# Define parameters
alpha = 0.1  # Learning rate
gamma = 0.9  # Discount factor
epsilon = 0.1  # Epsilon-greedy exploration rate
num_episodes = 1000

# Define state space
states = ['Round 1', 'Round 2', 'Round 3', 'Round 4']

# Define action space
actions = ['quit', 'stay_correct', 'pass']

# Initialize Q-values
Q = {(s, a): 0 for s in states for a in actions}

# Define immediate rewards for each action in each state
rewards = {
    'Round 1': {'quit': 5000, 'stay_correct': 20000, 'pass': -2000},
    'Round 2': {'quit': 5000, 'stay_correct': 20000, 'pass': -2000},
    'Round 3': {'quit': 5000, 'stay_correct': 20000, 'pass': -2000},
    'Round 4': {'quit': 5000, 'stay_correct': 20000, 'pass': -2000}
}

# SARSA algorithm
for episode in range(num_episodes):
    # Initialize state
    state = 'Round 1'
    
    # Choose action using epsilon-greedy policy
    if np.random.rand() < epsilon:
        action = np.random.choice(actions)
    else:
        action = max(actions, key=lambda a: Q[(state, a)])
    
    # Execute episode
    while state != 'Round 4':
        # Take action and observe next state and reward
        next_state = states[states.index(state) + 1]
        reward = rewards[state][action]
        
        # Choose next action using epsilon-greedy policy
        if np.random.rand() < epsilon:
            next_action = np.random.choice(actions)
        else:
            next_action = max(actions, key=lambda a: Q[(next_state, a)])
        
        # Update Q-value
        Q[(state, action)] += alpha * (reward + gamma * Q[(next_state, next_action)] - Q[(state, action)])
        
        # Transition to next state and action
        state = next_state
        action = next_action

# Print the learned Q-values
print("Learned Q-values:")
for state in states:
    for action in actions:
        print(f"Q({state}, {action}) = {Q[(state, action)]}")
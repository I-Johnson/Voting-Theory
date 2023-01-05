import random

def simulate_election(num_voters, num_candidates):
    preferences = []

    for i in range(num_voters):
        #generate random voters preferences
        preferences.append(random.sample(range(num_candidates), num_candidates))
    
    return preferences


'''def run_simulations(num_simulations, num_voters, num_candidates):
    condorcet_winner_exists = 0
    for i in range(num_simulations):
        if simulate'''

print(simulate_election(10, 3))
import random

def simulate_election(num_voters, num_candidates):
    preferences = []

    for i in range(num_voters):
        #generate random voters preferences
        preferences.append(random.sample(range(num_candidates), num_candidates))

    # Determining the winner of each pairwise election
    pairwise_winners = []
    for i in range(num_candidates):
        for j in range(i+1, num_candidates):
            votes_for_i = 0
            votes_for_j = 0
            for k in range(num_voters):
                if preferences[k][i] < preferences[k][j]:
                    votes_for_i += 1
                else: 
                    votes_for_j += 1
            if votes_for_i > votes_for_j:
                pairwise_winners.append(i)
            else: 
                pairwise_winners.append(j)

    # Checking if a condorcet winner exists
    condorcet_winner = None
    for i in range(num_candidates):
        condorcet_winner_found = True
        for j in range(num_candidates):
            if i == j:
                continue
            if pairwise_winners[i*(num_candidates-1)+j] != i:
                condorcet_winner_found = False
                break
        if condorcet_winner_found:
            condorcet_winner = i
            break
            
    return condorcet_winner
        


    



'''def run_simulations(num_simulations, num_voters, num_candidates):
    condorcet_winner_exists = 0
    for i in range(num_simulations):
        if simulate'''

print(simulate_election(10, 3))
import random

def simulate_election(num_voters, num_candidates):
    # Generate random voter preferences
    preferences = []
    for i in range(num_voters):
        preferences.append(random.sample(range(num_candidates), num_candidates))

    # Determine the winner of each pairwise election
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

    # Determine if a Condorcet winner exists
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

def run_simulations(num_simulations, num_voters, num_candidates):
    condorcet_winners_exist = 0
    for i in range(num_simulations):
        if simulate_election(num_voters, num_candidates) is not None:
            condorcet_winners_exist += 1
    return condorcet_winners_exist

# Run the simulations
num_simulations = 10000
num_voters = 10
num_candidates = 3
condorcet_winners_exist = run_simulations(num_simulations, num_voters, num_candidates)

# Print the results
print(f"Out of {num_simulations} simulations with {num_voters} voters and {num_candidates} candidates, a Condorcet winner existed in {condorcet_winners_exist} simulations ({condorcet_winners_exist/num_simulations*100:.2f}%).")




# '''def run_simulations(num_simulations, num_voters, num_candidates):
#     condorcet_winner_exists = 0
#     for i in range(num_simulations):
#         if simulate'''

# print(simulate_election(10, 3))
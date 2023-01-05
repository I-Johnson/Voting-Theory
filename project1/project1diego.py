import random
####
def simulate_election(num_voters, num_candidates):
    preferences = []

    for i in range(num_voters):
        #generate random voters preferences
        preferences.append(random.sample(range(num_candidates), num_candidates))
    
    return preferences

def plurality(num_voters, num_candidates):
    ballots = simulate_election(num_voters, num_candidates)
    plurality = []
    for ballot in ballots:
        plurality.append(ballot[0])
    return  max(set(plurality), key = plurality.count)

def condercet(num_voters, num_candidates):
    ballots = simulate_election(num_voters, num_candidates)
    absolute_winner = 0
    for candidate in range(1,num_candidates):
        votes_for_aw = 0
        votes_for_candidate = 0
        for ballot in ballots:
            aw = ballot.index(absolute_winner)
            c = ballot.index(candidate)
            if aw < c:
                votes_for_aw += 1
            else:
                votes_for_candidate += 0
            
        



def main():
    #Plurality section
    num_voters = 10
    num_candidates = 3
    condercet(num_voters, num_candidates)

    
    
if __name__ == "__main__":
    main()
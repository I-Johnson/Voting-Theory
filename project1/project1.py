import copy
import random

def make_IC_profile(num_voters: int, num_alternatives:int):
  alternatives = list(range(num_alternatives))
  profile = []
  for i in range(num_voters):
      random.shuffle(alternatives)
      profile.append(copy.copy(alternatives))
  
  return profile

def simulate_election(profile):
  num_voters = len(profile)
  num_alternatives = len(profile[0])

  # Determine the pairwise winners for each candidate
  pairwise_winners = []
  for i in range(num_alternatives):
      for j in range(num_alternatives):
          if i == j:
              continue
          i_wins = 0
          j_wins = 0
          for voter in range(num_voters):
              if profile[voter].index(i) < profile[voter].index(j):
                  i_wins += 1
              else:
                  j_wins += 1
          if i_wins > j_wins:
              pairwise_winners.append(i)
          else:
              pairwise_winners.append(j)

  # Determine if there is a Condorcet winner
  condorcet_winner = None
  for i in range(num_alternatives):
      condorcet_winner_found = True
      for j in range(num_alternatives):
          if i == j:
              continue
          if pairwise_winners[i*(num_alternatives-1)+j] != i:
              condorcet_winner_found = False
              break
      if condorcet_winner_found:
          condorcet_winner = i
          break

  return condorcet_winner

def main():
  num_simulations = 10
  num_voters = 10
  num_alternatives = 4
  condorcet_winner_count = 0
  for i in range(num_simulations):
      profile = make_IC_profile(num_voters, num_alternatives)
      condorcet_winner = simulate_election(profile)
      if condorcet_winner is not None:
          condorcet_winner_count += 1
  print(f"Condorcet winner found in {condorcet_winner_count}/{num_simulations} simulations.")

if __name__ == "__main__":
  main()

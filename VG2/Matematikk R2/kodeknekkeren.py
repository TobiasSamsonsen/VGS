import itertools

# Define your cards
cards = ['card1', 'card2', 'card3', 'card4', 'card5', 'card6', 'card7', 'card7', 'card7']

# Initialize a counter for the total number of combinations
total_combinations = 0

# Loop over all possible lengths of combinations
for r in range(1, len(cards)+1):
    # Use itertools.combinations to generate all combinations of length r
    combinations = list(itertools.combinations(cards, r))
    # Add the number of combinations generated to the total
    total_combinations += len(combinations)

print("Total combinations:", total_combinations)
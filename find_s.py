# Practical: Find-S Algorithm for Edible Trees
# Attributes: [Has Fruit, Leaf Shape, Bark, Thorny]

def run_pattern_finder():
    # 1. Define the Dataset (The 'Experience' E) [cite: 54]
    dataset = [
        ['YES', 'Oval', 'Smooth', 'NO', 'YES'],    # Edible
        ['YES', 'Pointed', 'Rough', 'NO', 'YES'], # Edible
        ['NO',  'Oval', 'Smooth', 'YES', 'NO'],   # Not Edible (Negative)
        ['YES', 'Heart', 'Rough', 'NO', 'YES']    # Edible
    ]

    # 2. Initialize Hypothesis (The most specific state 'phi') [cite: 69, 79]
    # We use 'phi' to represent that we haven't seen any edible trees yet.
    hypothesis = ['phi', 'phi', 'phi', 'phi']
    print(f"Initial State (Specific): {hypothesis}\n")

    # 3. Process Examples Step-by-Step [cite: 82]
    for i, example in enumerate(dataset):
        features = example[:-1] # All attributes except the YES/NO
        target = example[-1]    # The YES/NO label
        
        if target == 'YES':
            # If it's our first positive example, replace 'phi' with features [cite: 81]
            if 'phi' in hypothesis:
                hypothesis = features.copy()
            else:
                # Compare current rule with new example
                for x in range(len(hypothesis)):
                    if hypothesis[x] != features[x]:
                        # Mismatch found! Generalize using '?' wildcard [cite: 72, 81]
                        hypothesis[x] = '?'
            
            print(f"Ex {i+1} [POSITIVE]: Rule updated to -> {hypothesis}")
        
        else:
            # Negative examples are ignored in Find-S [cite: 80, 92]
            print(f"Ex {i+1} [NEGATIVE]: Rule ignored   -> {hypothesis}")

    # 4. Final Output
    print("\n" + "="*30)
    print("FINAL LEARNED PATTERN")
    print("="*30)
    print(f"A tree is edible IF: {hypothesis}")

if __name__ == "__main__":
    run_pattern_finder()
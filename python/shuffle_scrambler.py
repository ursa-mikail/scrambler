import random

def custom_shuffle(N):
    numbers = list(range(N + 1))  # 0 to N inclusive
    shuffled = []

    for k in range(N + 1):  # N+1 steps, from k = 0 to N
        remaining = len(numbers)
        pick_index = random.randint(0, remaining - 1)
        picked = numbers.pop(pick_index)
        shuffled.append(picked)
        print(f"Round {k}: Picked {picked}, Remaining: {numbers}")

    return shuffled

# Example usage
N = 10
shuffled_order = custom_shuffle(N)
print("\nFinal shuffled order:", shuffled_order)

"""
Round 0: Picked 4, Remaining: [0, 1, 2, 3, 5, 6, 7, 8, 9, 10]
Round 1: Picked 10, Remaining: [0, 1, 2, 3, 5, 6, 7, 8, 9]
Round 2: Picked 9, Remaining: [0, 1, 2, 3, 5, 6, 7, 8]
Round 3: Picked 8, Remaining: [0, 1, 2, 3, 5, 6, 7]
Round 4: Picked 1, Remaining: [0, 2, 3, 5, 6, 7]
Round 5: Picked 2, Remaining: [0, 3, 5, 6, 7]
Round 6: Picked 0, Remaining: [3, 5, 6, 7]
Round 7: Picked 5, Remaining: [3, 6, 7]
Round 8: Picked 3, Remaining: [6, 7]
Round 9: Picked 7, Remaining: [6]
Round 10: Picked 6, Remaining: []

Final shuffled order: [4, 10, 9, 8, 1, 2, 0, 5, 3, 7, 6]
"""

import random

def generate_shuffle_indices(N):
    indices = list(range(N))
    shuffled_indices = []
    
    for k in range(N):
        pick_index = random.randint(0, len(indices) - 1)
        picked = indices.pop(pick_index)
        shuffled_indices.append(picked)
    
    return shuffled_indices

def shuffle_words(words):
    N = len(words)
    shuffle_order = generate_shuffle_indices(N)
    shuffled_words = [words[i] for i in shuffle_order]
    return shuffled_words, shuffle_order

def unshuffle_words(shuffled_words, shuffle_order):
    N = len(shuffle_order)
    original_words = [None] * N
    for i, idx in enumerate(shuffle_order):
        original_words[idx] = shuffled_words[i]
    return original_words

# Example usage:
words = ["the", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog"]

shuffled, order_shuffled_indices = shuffle_words(words)
print("Shuffled words:", shuffled)
print("Shuffle order:", order_shuffled_indices)

unshuffled = unshuffle_words(shuffled, order_shuffled_indices)
print("Unshuffled back:", unshuffled)

"""
Shuffled words: ['quick', 'lazy', 'brown', 'the', 'dog', 'over', 'the', 'fox', 'jumps']
Shuffle order: [1, 7, 2, 6, 8, 5, 0, 3, 4]
Unshuffled back: ['the', 'quick', 'brown', 'fox', 'jumps', 'over', 'the', 'lazy', 'dog']
"""
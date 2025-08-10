import numpy as np
import matplotlib.pyplot as plt

def entropy(p):
    if p == 0 or p == 1:
        return 0
    return -p * np.log2(p) - (1 - p) * np.log2(1 - p)

prob_head = np.arange(0.1, 1.0, 0.1)
entropies = [entropy(p) for p in prob_head]

for p, e in zip(prob_head, entropies):
    print(f"P(H) = {p:.1f}, P(T) = {1 - p:.1f}, Entropy = {e:.4f}")
plt.plot(prob_head, entropies, marker='o')
plt.title("Entropy of a Biased Coin")
plt.xlabel("Probability of Head (P(H))")
plt.ylabel("Entropy")
plt.grid(True)
plt.show()

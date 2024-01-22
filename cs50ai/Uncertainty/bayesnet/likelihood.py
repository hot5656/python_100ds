from model import model

# Calculate probability for a given observation
probability = model.probability([["none", "no", "on time", "attend"]])
probability_miss = model.probability([["none", "no", "on time", "miss"]])

print("normal attend ", probability)
print("normal miss ", probability_miss)
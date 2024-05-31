# 子集(subset), 宇集(superset) and 補集(屬於A, 但不在B)

# 子集(subset)
A2 = {1, 2, 3}
B2 = set()
# B 屬於 A
print(f"B2 為 A2 之 subset:{B2 <= A2}")
# B 是 A 的 subset
print(f"B2 為 A2 之 subset:{B2.issubset(A2)}")
print(f"A2 為 A2 之 subset:{A2 <= A2}")
# ========================
A = {1, 2, 3, 4, 5, 6}
B = {1, 3, 5}
# B2 屬於 A2
print(f"B 為 A 之 subset:{B <= A}")
# B 是 A 的 subset
print(f"B 為 A 之 subset:{B.issubset(A)}")
# B2 為 A2 之 subset:True
# B2 為 A2 之 subset:True
# A2 為 A2 之 subset:True
# B 為 A 之 subset:True
# B 為 A 之 subset:True

# 宇集(superset)
# A 是 B2 的 superset
print(f"B 為 A 之 superset:{A >= B}")
# A 是 B2 的 superset
print(f"B 為 A 之 superset:{A.issuperset(B)}")
# B 為 A 之 superset:True
# B 為 A 之 superset:True

# 補集(屬於A, 但不在B)
print(A-B)
# {1, 2, 3}
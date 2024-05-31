# 集合操作
# & 交集 intersection
# | 聯集 union
# - 差集 difference
# ^ 對稱差集 symmetric_difference
math = {"Kevin", "Peter", "Eric"}
physics = {"Peter", "Nelson", "Tom"}
print(f"聯    集1: {math|physics}")
print(f"交    集1: {math&physics}")
print(f"差    集1: {math-physics}")
print(f"對稱差集1: {math^physics}")

print(f"聯    集2: {math.union(physics)}")
print(f"交    集2: {math.intersection(physics)}")
print(f"差    集2: {math.difference(physics)}")
print(f"對稱差集2: {math.symmetric_difference(physics)}")
# 聯    集1: {'Eric', 'Tom', 'Nelson', 'Kevin', 'Peter'}
# 交    集1: {'Peter'}
# 差    集1: {'Eric', 'Kevin'}
# 對稱差集1: {'Eric', 'Tom', 'Kevin', 'Nelson'}
#
# 聯    集2: {'Eric', 'Tom', 'Nelson', 'Kevin', 'Peter'}
# 交    集2: {'Peter'}
# 差    集2: {'Eric', 'Kevin'}
# 對稱差集2: {'Eric', 'Tom', 'Kevin', 'Nelson'}

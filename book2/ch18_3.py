# 判斷句子相似度
import numpy as np

def consine_similarity(va, vb):
    norm_a = np.linalg.norm(va)
    norm_b = np.linalg.norm(vb)
    dot_ab = np.dot(va, vb)
    return dot_ab/(norm_a * norm_b )

a = np.array([2, 1, 1, 1, 0, 0, 0, 0])
b = np.array([1, 1, 0, 0, 1, 1, 1, 0])
c = np.array([1, 1, 0, 0, 1, 1, 0, 1])
print(f" a 和 b 的相似度 : {consine_similarity(a, b)}")
print(f" a 和 c 的相似度 : {consine_similarity(a, c)}")
print(f" b 和 c 的相似度 : {consine_similarity(b, c)}")
#  a 和 b 的相似度 : 0.5070925528371099
#  a 和 c 的相似度 : 0.5070925528371099
#  b 和 c 的相似度 : 0.7999999999999998




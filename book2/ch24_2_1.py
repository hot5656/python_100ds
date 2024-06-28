from math import exp
def non_softmax(input_vector):
    molecular = [j for j in input_vector]
    p = [round(i/sum(molecular),3) for i in input_vector]
    return p

def softmax(input_vector):
    # 計算分子
    exponents = [exp(j) for j in input_vector]
    # 先加總分母
    # 分子除以分母
    p = [round(exp(i)/sum(exponents), 3) for i in input_vector]
    return p

print(f"一般公式    : {non_softmax([1, 3, 6])}")
print(f"softmax公式: {softmax([1, 3, 6])}")

# 一般公式    : [0.1, 0.3, 0.6]
# softmax公式: [0.006, 0.047, 0.946]
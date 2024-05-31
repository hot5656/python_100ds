# 集合新增刪除
# add() 新增
# remove() 刪除
# pop() 隨機刪除並回傳
# clear() 清除所有元素
A ={1, 2, 5}
A.add(3)
print(A)
A.remove(2)
print(A)
ret = A.pop()
print(f"pop {ret}")
print(A)
A.clear()
print(A)
# {1, 2, 3, 5}
# {1, 3, 5}
# pop 1
# {3, 5}
# set() : 表空集合
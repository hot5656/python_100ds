# random
import numpy as np

# rand() 依維度 0~1 隨機浮點數
# randn() 依維度 -1~1 常態分佈隨機浮點
# randint() 依維度 隨機整數
# random(3)/random_sample(3)/sample(3) 產生數個 0~1 隨機浮點數: 無差異
# choice(list) 隨機挑選數值
print('產生 2*3 0~1 隨機浮點數\n', np.random.rand(2,3))
print('產生 2*3 -1~1 常態分佈隨機浮點數\n', np.random.randn(2,3))
print('產生 0~4(不含5) 隨機整數\n', np.random.randint(5))
print('產生 6個 2~4(不含5) 隨機整數(不含5) \n', np.random.randint(2,5,[6]))
print('產生 3個 0~1 隨機浮點數\n',
                  np.random.random(3),
                  np.random.random_sample(3),
                  np.random.sample(3))
print('隨機挑選數值', np.random.choice([1,2,3,4,5,6]))
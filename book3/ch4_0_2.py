# 繪製蠟燭圖(call function)
from Data import getData
from BackTest import ChartCandle

data = getData('0050', '2024-05-01', '2024-10-02')
ChartCandle(data)
# read csv
import numpy as np
# UnicodeDecodeError: 'cp950' codec can't decode byte 0xbf in position 2: illegal multibyte sequence
# encoding="utf-8"
# field is numpy.float64(default)
na = np.genfromtxt('scores.csv', delimiter=',', skip_header=1, encoding="utf-8")
# nan:not a number
print(type(na), na.shape, na)
print(type(na[0][0]), type(na[0][1]))
# <class 'numpy.ndarray'> (4, 6) [[nan 65. 92. 78. 83. 70.]
#  [nan 90. 72. 76. 93. 56.]
#  [nan 81. 85. 91. 89. 77.]
#  [nan 79. 53. 47. 94. 80.]]
# <class 'numpy.float64'> <class 'numpy.float64'>


# Load data from CSV file
# dtype=str field is string
na2 = np.genfromtxt('scores.csv', delimiter=',', dtype=str, skip_header=1, encoding="utf-8")
print(type(na2), na2.shape, na2)
print(type(na2[0][0]), type(na2[0][1]))
# <class 'numpy.ndarray'> (4, 6) [['王小明' '65' '92' '78' '83' '70']
#  ['李小美' '90' '72' '76' '93' '56']
#  ['陳大同' '81' '85' '91' '89' '77']
#  ['林小玉' '79' '53' '47' '94' '80']]
# <class 'numpy.str_'> <class 'numpy.str_'>

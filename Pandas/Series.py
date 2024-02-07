

import numpy  as np
import pandas as pd


labels = ['a','b','c']
my_data = [10,20,30]

arr = np.array(my_data)

d = {'a':10,'b':20,'c':30} # tạo dictinary gồm key và value

pd.Series(data = my_data)
# Output:
# 0    a
# 1    b
# 2    c
# 3    d
# dtype: object

pd.Series(data = my_data ,index = labels)
# Output:
# a    10
# b    20
# c    30
# dtype: int64

pd.Series(arr) 
# Output:
# 0    10
# 1    20
# 2    30
# dtype: int64

pd.Series(d)
# Output:
# a    10
# b    20
# c    30
# dtype: int64

pd.Series(data = labels)
# Output:
# 0    a
# 1    b
# 2    c
# dtype: object

# thực hành
sr1 = pd.Series([1,4,5],['VN','KR',"CN"])
sr2 = pd.Series([2,3,4],['VN','HQ','CN'])

print(sr1 + sr2)

# kết quả sẽ gộp thành 4 nước, và nước nào có 1 thì + với nan sẽ ra nan
# CN    9.0
# HQ    NaN
# KR    NaN
# VN    3.0
# dtype: float64


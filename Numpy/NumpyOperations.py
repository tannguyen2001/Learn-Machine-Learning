# các phép tính cơ bản

import numpy as np

arr = np.arange(0,11) # array([0,1,2,3,4,5,6,7,8,9,10])

arr2 = arr + arr # array([0,2,4,6,8,10,12,14,16,18,20])

arr3 = arr * arr # array -> mỗi phần tử * với các phần tử 

arr4 = arr + 100 # mỗi phần tử + 100

arr5 = arr/arr # 0/0 sẽ đưa thành 'nan' trong phần tử của mảng

arr6 = 1/arr # 1/0 sẽ đưa thành vô hạn 'inf' trong phần tử của mảng

arr7 = np.exp(arr) # e mũ từng phần tử mảng

arr8 =  np.log(arr) # logarit cơ số e từng phần tử

arr9 = np.log10(arr) # logarit cơ số 10 từng phần tử

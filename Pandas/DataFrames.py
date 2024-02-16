
import numpy as np
import pandas as pd

from numpy.random import randn

np.random.seed(101)

df = pd.DataFrame(randn(5,4),['A','B','C','D','E'],['W','X','Y','Z']) # tạo ra dữ liệu giống datatable có hàng và cột

# dữ liệu khác với series. trong series thì dữ liệu theo dạng từng hàng. còn trong dataframe thì dữ liệu theo cả hàng và cột, giống matrix

### cách dùng với cột
df['X'] # lấy ra cột X
df[['X','Y']] # lấy ra cả cột X và Y
df['G'] = df['X'] + df['Y'] #tạo cột mới trong dataframe

# xoá cột hoặc hàng trong dataframe và trả ra dataframe mới chứ không xoá trong dataframe hiện tại
df.drop('X',axis=1) # axis = 1 để xoá cột
df.drop('A',axis=0) # axis = 0 để xoá hàng

# xoá cột hoặc hàng trong dataframe hiện tại
df.drop('X',axis=1,inplace=True) # axis = 1 để xoá cột
df.drop('A',axis=0,inplace=True) # axis = 0 để xoá hàng

# cũng có thể xoá nhiểu cột hoặc nhiều hàng, ví dụ
df.drop(['A','B','C'],axis=0,inplace=True)

df.shape # trả ra số hàng và cột, ví dụ: (5,4)

### cách dùng với hàng

# lẫy cả hàng
df.loc('A') # trả về dữ liệu của hàng A theo từng cột giống với Series
df.iloc(0) # trả về dữ liệu của hàng A, vì hàng A có index =0

#lấy 1 cell (1 ô)
df.loc('A','X') #trả về ô [A,X], có thể làm tương tự với index

#lấy cắt
df.loc(['A','B'],['X','Y']) #lấy giao 2 hàng A,B và X,Y

#so sánh
print(df > 0) # trả ra 1 dữ liệu True/False theo dạng bảng

print(df[df > 0]) # rả ra bảng các dữ liệu > 0. còn <=0 thì nan

df['W'] > 0 # rả ra cột W dữ liệu True/False

df[df['W'] < 0] # trả ra các hàng mà cột W < 0
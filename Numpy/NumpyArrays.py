
#thư viện numpy => hỗ trợ tạo ra các mảng số, ma trận,... hỗ trợ cho việc tìm nghiệm trong machine learning
import numpy as np

my_list = [1,2,3] # đây là list

arr = np.array(my_list) # array([1, 2, 3])

my_mat = [[1,2,3],[4,5,6],[7,8,9]]

np.array(my_mat) # ma tran 2 chieu 3 * 3


np.arange(0,10) # mang tu 0 -> 9

np.arange(0,11,2) # mang tu 0 -> 10 cach nhau buoc nhay 2 don vi


np.zeros(3) # mang co 3 phan tu full 0

np.zeros((2,3)) # ma tran 2*3 full 0

np.linspace(0,5,100) # mang 100 phan tu co do lon cach deu nhau tu 0->5

np.eye(4) # tạo ra ma trận đơn vị

# #array([[1., 0., 0., 0.],
#        [0., 1., 0., 0.],
#        [0., 0., 1., 0.],
#        [0., 0., 0., 1.]])


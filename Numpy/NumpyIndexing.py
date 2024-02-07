#NumpyIndexing

import numpy as np

arr = np.arange(0,11,1) # -> mang tu 0 den 10

arr[:] # -> mang tu 0 -> 10: [0,1,2,3,4,5,6,7,8,9,10]

arr[4:6] # -> mang tu index 4-> 5 : [4,5]

arr [4:] # mang tu index 4 -> het : [4,5,6,7,8,9,10]

arr [:4] # mang tu dau toi index thu 3 : [0,1,2,3]
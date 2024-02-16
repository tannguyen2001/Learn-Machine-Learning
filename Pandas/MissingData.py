

import pandas as pd
import numpy as np

d = {'A':[1,2,np.nan],'B':[5,np.nan,np.nan],'C':[1,2,3]}

df = pd.DataFrame(d)

df.dropna() # loại bỏ nan trong DataFrame

# dataframe.dropna(axis=0, inplace=False, subset=None, thresh=None)

# axis: Trục để xóa. 0 để xóa hàng, 1 để xóa cột.
# inplace: Boolean. True để thực hiện thay đổi trực tiếp trên DataFrame, False để trả về một DataFrame mới với thay đổi.
# subset: Danh sách các cột để kiểm tra giá trị bị thiếu. Nếu None, tất cả các cột sẽ được kiểm tra.
# thresh: Số lượng giá trị không bị thiếu tối thiểu để giữ lại một hàng hoặc cột.

df.fillna() # thay đổi nan trong DataFrame
# dataframe.fillna(value=None, method=None, axis=None, inplace=False, limit=None, downcast=None)

# value: Giá trị để thay thế các giá trị bị thiếu. Có thể là một giá trị đơn lẻ, một dictionary hoặc một hàm.
# method: Phương pháp thay thế giá trị bị thiếu. Có thể là ffill (điền giá trị phía trước), bfill (điền giá trị phía sau) hoặc interpolate (nội suy).
# axis: Trục để thay thế. 0 để thay thế trên các hàng, 1 để thay thế trên các cột.
# inplace: Boolean. True để thực hiện thay đổi trực tiếp trên DataFrame, False để trả về một DataFrame mới với thay đổi.
# limit: Số lượng giá trị bị thiếu liên tiếp tối đa để thay thế.
# downcast: Boolean. True để tự động chuyển đổi kiểu dữ liệu của giá trị thay thế sang kiểu dữ liệu của cột.
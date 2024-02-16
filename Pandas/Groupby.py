
#Hàm DataFrame.groupby được sử dụng để chia DataFrame 
# thành các nhóm dựa trên một hoặc nhiều cột. 
# Sau đó, bạn có thể áp dụng các hàm tổng hợp (như tính trung bình, tổng, v.v.) cho từng nhóm.

import pandas as pd


df = pd.DataFrame(None)

df.groupby(by=None, axis=0, level=None, as_index=False, sort=True, dropna=True, observed=False) # cú pháp

#Tham số:

# by: Cột hoặc danh sách các cột để nhóm.
# axis: Trục để nhóm. 0 để nhóm theo hàng, 1 để nhóm theo cột.
# level: Cấp độ của MultiIndex để nhóm.
# as_index: Boolean. True để sử dụng các nhãn nhóm làm chỉ mục của DataFrame kết quả, False để giữ nguyên chỉ mục ban đầu.
# sort: Boolean. True để sắp xếp các nhóm theo giá trị của cột nhóm.
# dropna: Boolean. True để bỏ qua các giá trị bị thiếu trong cột nhóm.
# observed: Boolean. True để chỉ bao gồm các nhóm có ít nhất một quan sát.
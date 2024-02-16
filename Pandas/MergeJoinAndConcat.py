
###Concat
#Hàm concat được sử dụng để nối các DataFrame với nhau. Nối có thể được thực hiện theo chiều dọc (ghép các hàng) hoặc chiều ngang (ghép các cột).

# pd.concat(objs, axis=0, ignore_index=False, keys=None, levels=None, names=None, verify_integrity=False, sort=False)

# objs: Danh sách các DataFrame để nối.
# axis: Trục để nối. 0 để nối theo chiều dọc, 1 để nối theo chiều ngang.
# ignore_index: Boolean. True để bỏ qua chỉ mục của DataFrame khi nối, False để giữ nguyên chỉ mục.
# keys: Danh sách các tên để sử dụng cho các DataFrame được nối.
# levels: Danh sách các cấp độ của MultiIndex để nối.
# names: Danh sách các tên để sử dụng cho các cột được nối.
# verify_integrity: Boolean. True để kiểm tra tính toàn vẹn của dữ liệu khi nối, False để bỏ qua kiểm tra.
# sort: Boolean. True để sắp xếp các DataFrame theo chỉ mục trước khi nối, False để giữ nguyên thứ tự.

###Megre
#Hàm merge được sử dụng để hợp nhất hai DataFrame dựa trên các cột chung.

#pd.merge(left, right, how='inner', on=None, left_on=None, right_on=None, left_index=False, right_index=False, sort=False, suffixes=('_x', '_y'), copy=True, indicator=False, validate=None)

# left: DataFrame bên trái.
# right: DataFrame bên phải.
# how: Loại hợp nhất. inner (hợp nhất bên trong), left (hợp nhất bên trái), right (hợp nhất bên phải), outer (hợp nhất bên ngoài).
# on: Tên cột chung để hợp nhất.
# left_on: Tên cột trong DataFrame bên trái để hợp nhất.
# right_on: Tên cột trong DataFrame bên phải để hợp nhất.
# left_index: Boolean. True để sử dụng chỉ mục của DataFrame bên trái làm khóa hợp nhất, False để sử dụng cột.
# right_index: Boolean. True để sử dụng chỉ mục của DataFrame bên phải làm khóa hợp nhất, False để sử dụng cột.
# sort: Boolean. True để sắp xếp các DataFrame theo khóa hợp nhất trước khi hợp nhất, False để giữ nguyên thứ tự.
# suffixes: Tuple of strings. Suffixes to add to overlapping column names.
# copy: Boolean. True để tạo một bản sao của DataFrame kết quả, False để sửa đổi DataFrame ban đầu.
# indicator: Boolean. True để thêm một cột chỉ báo vào DataFrame kết quả, False để bỏ qua.
# validate: None, '1:m', or 'm:1'. If None, do not check if merge is 1:m or m:1. Otherwise, check if the merge is one-to-many or many-to-one and raise an error if it is not.

###Join
#Hàm join được sử dụng để hợp nhất hai DataFrame dựa trên các cột chung. Cú pháp và chức năng của join rất giống với merge.

#tuy nhiên join là hàm của DataFrame, còn concat là hàm của pandas, join giá giống join trong sql

#dataframe.join(other, on=None, how='inner', lsuffix='', rsuffix='', sort=False, copy=True, indicator=False, validate=None)

# dataframe: DataFrame bên trái.
# other: DataFrame bên phải.
# on: Tên cột chung để hợp nhất.
# how: Loại hợp nhất. inner (hợp nhất bên trong), left (hợp nhất bên trái), right (hợp nhất bên phải), outer (hợp nhất bên ngoài).
# lsuffix: Suffix to add to overlapping column names in the left DataFrame.
# rsuffix: Suffix to add to overlapping column names in the right DataFrame.
# sort: Boolean. True để sắp xếp các DataFrame theo khóa hợp nhất trước khi hợp nhất, False để giữ nguyên thứ tự.
# copy: Boolean. True để tạo một bản sao của DataFrame kết quả, False để sửa đổi DataFrame ban đầu.
# indicator: Boolean. True để thêm một cột chỉ báo vào DataFrame kết quả, False để bỏ qua.
# validate: None, '1:m', or 'm:1'. If None, do not check if merge is 1:m or m:1. Otherwise, check if the merge is one-to-many or many-to-one and raise an error if it is not.


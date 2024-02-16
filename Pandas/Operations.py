
# Pandas cung cấp một loạt các phép toán cho phép bạn thao tác và phân tích dữ liệu trong DataFrame. Dưới đây là một số phép toán phổ biến nhất:

# 1. Phép toán toán học:

# Cộng, trừ, nhân, chia: +, -, *, /
# Lũy thừa: **
# Lấy căn bậc hai: sqrt()
# Lấy logarit: log()
# Lấy giá trị tuyệt đối: abs()
# Làm tròn số: round()
# 2. Phép toán thống kê:

# Tính trung bình: mean()
# Tính trung vị: median()
# Tính tổng: sum()
# Tính độ lệch chuẩn: std()
# Tính phương sai: var()
# Tính tứ phân vị: quantile()
# 3. Phép toán so sánh:

# Lớn hơn: >
# Nhỏ hơn: <
# Lớn hơn hoặc bằng: >=
# Nhỏ hơn hoặc bằng: <=
# Bằng nhau: ==
# Không bằng nhau: !=
# 4. Phép toán logic:

# AND: &
# OR: |
# NOT: ~
# 5. Lọc dữ liệu:

# Lọc theo giá trị: df[df['column'] == value]
# Lọc theo nhiều điều kiện: df[(df['column1'] == value1) & (df['column2'] == value2)]
# Lọc theo vị trí: df.iloc[start:stop]
# Lọc theo nhãn: df.loc[start:stop]
# 6. Sắp xếp dữ liệu:

# Sắp xếp theo một cột: df.sort_values('column')
# Sắp xếp theo nhiều cột: df.sort_values(['column1', 'column2'])
# Sắp xếp theo thứ tự tăng dần: df.sort_values('column', ascending=True)
# Sắp xếp theo thứ tự giảm dần: df.sort_values('column', ascending=False)
# 7. Nhóm dữ liệu:

# Nhóm theo một cột: df.groupby('column')
# Nhóm theo nhiều cột: df.groupby(['column1', 'column2'])
# Tính trung bình theo nhóm: df.groupby('column').mean()
# Tính tổng theo nhóm: df.groupby('column').sum()
# 8. Thêm cột mới:

# Thêm cột mới bằng cách sử dụng một biểu thức: df['new_column'] = df['column1'] + df['column2']
# Thêm cột mới bằng cách sử dụng một giá trị: df['new_column'] = value
# 9. Xóa cột:

# Xóa cột bằng cách sử dụng tên cột: del df['column']
# Xóa cột bằng vị trí: del df.iloc[:, index]
# 10. Thay đổi giá trị:

# Thay đổi giá trị bằng cách sử dụng vị trí: df.iloc[row, column] = value
# Thay đổi giá trị bằng cách sử dụng nhãn: df.loc[row, column] = value
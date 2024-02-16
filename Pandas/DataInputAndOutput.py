import pandas as pd
from sqlalchemy import create_engine


pd.read_csv('example.csv') # đọc dữ liệu file csv => thành dạng bảng giống DataFrame

###csv
df = pd.read_csv('example.csv')

df.to_csv('My_output',index=False) # xuất thành file My_output.csv và không thêm index


###excel
df = pd.read_excel('Excel_Sample.xlsx',sheet_name='Sheet1') # đọc dữ liệu file excel với Sheet1 => thành dạng bảng giống DataFrame

df.to_excel('GG.xlsx',sheet_name='NewSheet') # xuất thành file GG.xlsx và có sheet = NewSheet

###html

data = pd.read_html('https://www.blogger.com/about/?hl=vi') #đọc data 1 link htmk


###sql
engine = create_engine('sqlite:///:memory:') #tạo sql lite trong bộ nhớ ram

df.to_sql('my_table',engine) # đưa data vào sql 

sqldf= pd.read_sql('my_table',con=engine) # lấy data từ sql
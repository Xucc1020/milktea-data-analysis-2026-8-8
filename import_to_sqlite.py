import pandas as pd
import sqlite3

# 读取 CSV
df = pd.read_csv('milktea_sales.csv')

# 连接 SQLite 数据库（自动创建 milktea.db 文件）
conn = sqlite3.connect('milktea.db')

# 把数据导入数据库（表名：milktea_sales）
df.to_sql('milktea_sales', conn, if_exists='replace', index=False)

print("数据已导入 SQLite！共", len(df), "条记录")

# 验证一下
cursor = conn.cursor()
cursor.execute("SELECT * FROM milktea_sales LIMIT 5")
for row in cursor.fetchall():
    print(row)

conn.close()
import pandas as pd
import sqlite3
import matplotlib.pyplot as plt

# 设置中文字体（防止乱码）
plt.rcParams['font.sans-serif'] = ['SimHei', 'DejaVu Sans']
plt.rcParams['axes.unicode_minus'] = False

# 连接数据库
conn = sqlite3.connect('milktea.db')

print("========== 查询1：查看前5条数据 ==========")
df1 = pd.read_sql_query("SELECT * FROM milktea_sales LIMIT 5", conn)
print(df1)
print()

print("========== 查询2：总销售额、总销量 ==========")
df2 = pd.read_sql_query("""
    SELECT 
        SUM(销售额) AS 总销售额,
        SUM(销量) AS 总销量,
        COUNT(*) AS 订单数
    FROM milktea_sales
""", conn)
print(df2)
print()

print("========== 查询3：哪个品类卖得最好 ==========")
df3 = pd.read_sql_query("""
    SELECT 
        品类,
        SUM(销量) AS 总销量,
        SUM(销售额) AS 总销售额
    FROM milktea_sales
    GROUP BY 品类
    ORDER BY 总销售额 DESC
""", conn)
print(df3)
print()

print("========== 查询4：哪个门店最赚钱 ==========")
df4 = pd.read_sql_query("""
    SELECT 
        门店,
        SUM(销售额) AS 总销售额,
        AVG(销售额) AS 平均订单金额
    FROM milktea_sales
    GROUP BY 门店
    ORDER BY 总销售额 DESC
""", conn)
print(df4)
print()

print("========== 查询5：会员和非会员谁花得多 ==========")
df5 = pd.read_sql_query("""
    SELECT 
        是否会员,
        COUNT(*) AS 订单数,
        SUM(销售额) AS 总销售额,
        AVG(销售额) AS 客单价
    FROM milktea_sales
    GROUP BY 是否会员
""", conn)
print(df5)
print()

print("========== 查询6：周末和工作日哪个销量高 ==========")
df6 = pd.read_sql_query("""
    SELECT 
        CASE 
            WHEN strftime('%w', 日期) IN ('0', '6') THEN '周末' 
            ELSE '工作日' 
        END AS 时段,
        SUM(销量) AS 总销量,
        SUM(销售额) AS 总销售额
    FROM milktea_sales
    GROUP BY 时段
""", conn)
print(df6)
print()

# ========== 可视化 ==========
print("正在生成图表...")

# 图1：各品类销售额占比（饼图）
plt.figure(figsize=(6, 6))
df3_pie = df3.set_index('品类')['总销售额']
plt.pie(df3_pie, labels=df3_pie.index, autopct='%1.1f%%', startangle=90)
plt.title('各品类销售额占比')
plt.tight_layout()
plt.savefig('chart1_pie.png', dpi=150)
plt.show()
print("图表已保存：chart1_pie.png")

# 图2：各门店销售额对比（柱状图）
plt.figure(figsize=(8, 5))
df4_bar = df4.set_index('门店')['总销售额']
df4_bar.plot(kind='bar', color=['#FF6B6B', '#4ECDC4', '#45B7D1'])
plt.title('各门店销售额对比')
plt.ylabel('销售额（元）')
plt.xticks(rotation=15)
plt.tight_layout()
plt.savefig('chart2_bar.png', dpi=150)
plt.show()
print("图表已保存：chart2_bar.png")

# 图3：会员 vs 非会员客单价对比
plt.figure(figsize=(6, 5))
df5_bar = df5.set_index('是否会员')['客单价']
df5_bar.plot(kind='bar', color=['#96CEB4', '#FFEAA7'])
plt.title('会员 vs 非会员平均客单价')
plt.ylabel('平均订单金额（元）')
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig('chart3_member.png', dpi=150)
plt.show()
print("图表已保存：chart3_member.png")

conn.close()
print("分析完成！")
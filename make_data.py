import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random

random.seed(42)
np.random.seed(42)

dates = pd.date_range(start='2026-07-01', end='2026-07-31', freq='D')
categories = ['珍珠奶茶', '果茶', '纯茶', '奶盖茶']
sizes = ['中杯', '大杯']
stores = ['A店-大学城', 'B店-商业街', 'C店-写字楼']

data = []
order_id = 1001

for _ in range(200):
    date = random.choice(dates)
    cat = random.choice(categories)
    size = random.choice(sizes)
    store = random.choice(stores)
    
    base_price = {'珍珠奶茶': 12, '果茶': 14, '纯茶': 10, '奶盖茶': 16}[cat]
    size_add = 3 if size == '大杯' else 0
    price = base_price + size_add
    
    qty = random.randint(1, 5)
    if date.weekday() >= 5:
        qty += random.randint(1, 3)
    
    is_member = random.choice(['是', '否'])
    
    data.append({
        '订单ID': f'ORD{order_id}',
        '日期': date.strftime('%Y-%m-%d'),
        '品类': cat,
        '杯型': size,
        '单价': price,
        '销量': qty,
        '门店': store,
        '是否会员': is_member
    })
    order_id += 1

df = pd.DataFrame(data)
df['销售额'] = df['单价'] * df['销量']
df.to_csv('milktea_sales.csv', index=False, encoding='utf-8-sig')
print("数据已生成！共", len(df), "条记录")
print(df.head(10))
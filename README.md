# 奶茶店销售数据分析

## 项目简介
基于某奶茶品牌 3 家门店的 200 条销售订单，使用 Python + SQLite 进行数据分析与可视化，为运营决策提供数据支持。

## 技术栈
- Python 3.12
- SQLite（内置数据库，零配置）
- pandas、matplotlib

## 分析内容
1. 各品类销售额占比分析
2. 门店销售表现对比
3. 会员与非会员消费行为分析
4. 工作日 vs 周末销量对比

## 核心结论
- 奶盖茶贡献 **34.1%** 销售额，是主力盈利品类
- B店-商业街销售额最高（3859元），平均客单价 55.1 元
- 工作日销量是周末的 **2.3 倍**

## 文件说明
| 文件 | 说明 |
|------|------|
| `make_data.py` | 生成虚拟销售数据 |
| `import_to_sqlite.py` | 数据导入 SQLite |
| `analysis.py` | SQL 查询 + 可视化分析 |
| `milktea_sales.csv` | 原始数据（200条） |
| `milktea.db` | SQLite 数据库 |
| `chart1_pie.png` | 各品类销售额占比图 |
| `chart2_bar.png` | 各门店销售额对比图 |
| `chart3_member.png` | 会员 vs 非会员客单价图 |

## 运行方式
```bash
python make_data.py
python import_to_sqlite.py
python analysis.py

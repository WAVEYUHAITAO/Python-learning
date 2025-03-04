---
Topic:
    - 房地产

Ext:
    - .csv

DatasetUsage:
    - 38448

FolderName:
    - /home/mw/input/boston_housing/
---

## **背景介绍**

波士顿房地产市场竞争激烈，而你想成为该地区最好的房地产经纪人。为了更好地与同行竞争，你决定运用机器学习的一些基本概念，帮助客户为自己的房产定下最佳售价。幸运的是，你找到了波士顿房价的数据集，里面聚合了波士顿郊区包含多个特征维度的房价数据。你的任务是用可用的工具进行统计分析，并基于分析建立优化模型。这个模型将用来为你的客户评估房产的最佳售价。

## **如何在线使用数据集**

创建项目后：
Python用户，输入`ls ../input/boston_housing/`  查看数据路径
R用户，输入`list.files("../input/boston_housing/") `查看数据路径
使用相关包读取数据


## **数据说明**
- 文件列表
该数据集包含1个文件：
	- housing.csv

- 数据集的整体特征

数据集名称 |  数据类型 | 特征数 | 实例数 | 值缺失 | 相关任务
-------------| ------- |-----------| ---------| ---------|----------|--------
波士顿房价数据集 | 数值型或类别型 |  13 | 506 |  无 | 描述性分析（可视化）、预测性分析（建模）、


- 属性描述
	**文件housing.csv中包含14个字段，具体信息如下：**

No| 属性 | 数据类型 | 字段描述 
---|---|---|---
1| CRIM | Float |城镇人均犯罪率
2 | ZN | Float | 占地面积超过2.5万平方英尺的住宅用地比例
3 |INDUS  | Float | 城镇非零售业务地区的比例
4 |CHAS | Integer  |   查尔斯河虚拟变量 (= 1 如果土地在河边；否则是0)
5 | NOX | Float |一氧化氮浓度（每1000万份）
6 | RM  | Float | 平均每居民房数
7 | AGE  | Float |在1940年之前建成的所有者占用单位的比例
8| DIS  | Float | 与五个波士顿就业中心的加权距离
9 |RAD  | Integer  |   辐射状公路的可达性指数
10 |TAX | Float |  每10,000美元的全额物业税率
11 | PTRATIO | Float | 城镇师生比例
12 | B | Float |  1000（Bk - 0.63）^ 2其中Bk是城镇黑人的比例
13 | LSTAT| Float | 人口中地位较低人群的百分数
14 | MEDV | Float |  （目标变量/类别属性）以1000美元计算的自有住房的中位数


## **数据来源**
这里提供的数据集及对应学习材料来自[优达学城纳米学位机器学习进阶](http://cn.udacity.com/course/machine-learning-engineer-nanodegree--nd009-cn-advanced)实战项目。

>原数据集创建者是Harrison, D. 和 Rubinfeld, D.L.：Hedonic prices and the demand for clean air’, J. Environ. Economics & Management, vol.5, 81-102, 1978。这也被使用在 Belsley, Kuh & Welsch 的 ‘Regression diagnostics …’, Wiley, 1980。 注释：许多变化已经被应用在后者第244-261页的表中。[[1]](http://sklearn.apachecn.org/cn/0.19.0/sklearn/datasets/descr/boston_house_prices.html)

UCI ML(欧文加利福尼亚大学 机器学习库) 波士顿房价数据集的副本详情请参考：[UCI Machine Learning Repository](https://archive.ics.uci.edu/ml/machine-learning-databases/housing/) 。 


## **数据集可探索、研究的方向**
波士顿房价数据已被用于许多涉及回归问题的机器学习论文中

更多有趣的问题等你来探索！

## **引用格式**
```
@misc{boston_housing,
    title = { 波士顿房价数据集 },
    author = { 小鲸 },
    howpublished = { \url{https://www.heywhale.com/mw/dataset/590bd595812ede32b73f55f2} },
    year = { 2017 },
}
```
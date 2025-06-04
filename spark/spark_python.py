from pyspark import SparkConf, SparkContext


def main():
    # 创建SparkConf配置对象
    conf = SparkConf().setAppName("App")
    # 创建SparkContext
    sc = SparkContext(conf=conf)
    # 创建一个简单的RDD
    rdd = sc.parallelize(range(1, 11))
    # 应用map转换操作
    squares = rdd.map(lambda num: num * num)
    # 应用filter转换操作
    even_squares = squares.filter(lambda num: num % 2 == 0)
    # 执行行动操作collect，收集结果到驱动程序
    even_squares_collected = even_squares.collect()
    # 打印结果
    for num in even_squares_collected:
        print(num)
    # 停止SparkContext
    sc.stop()


if __name__ == "__main__":
    main()

books=["西游记","红楼梦", "三国演义", "水浒传"]
print(books)

countries=["中国","美国","英国","俄罗斯","日本"]
print(countries)
#使用两种方法获取列表的第四个元素
print(countries[3])  # 使用索引获取
print(countries[-2])  # 使用负索引获取
#切片 结果包含起始索引的元素，但不包含结束索引对应的数据
#print(countries[1:3])  # 获取索引1到3的元素
#即使使用反向索引，切片的起始索引和结束索引仍然是正向的
#print("===",countries[-3:-1])  # 获取索引-1到-3的元素
print(countries[:])  # 获取所有元素
print(countries[:3])  #["中国", "美国", "英国"]  # 获取前三个元素
#获取列表长度
print(len(countries))  # 获取列表长度
for book in books:
    print(book)  # 遍历列表，输出每个元素
for c in countries:
    print(c)

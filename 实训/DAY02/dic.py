#字典
book={
    'bookname':'三国演义',
    'author':'罗贯中',
    'price': 89,
}
#创建字典，保存一个电视剧的名字、演员、类型
tv_show = {
    'name': '甄嬛传',
    'actors': ['孙俪', '陈建斌', '蔡少芬'],
    'genre': '古装剧'
}
#获取电视的演员
print(tv_show['actors'])  # 输出演员列表
tv_show['price']=99
print(tv_show)
tv_show['mtype']
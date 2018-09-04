#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
#__author:Administrator
#2018/9/3

# dic1 = {"name":"alex"}
# dic1["age"] = 18
#
# #k如果存在，则不修改v，返回k原来的值
# print(dic1.setdefault("age",34))
# # k如果不存在，则在字典中追加相应的KV，并返回KV对。
# print(dic1.setdefault("hobby","girl"))
#
# print(dic1)

# 通过KV对来查找

# dic3 = {'age':18,'name':'alex','hobby':'girl'}
# print(dic3['name'])
#
# print(list(dic3.keys()))
# print(list(dic3.values()))
# print(list(dic3.items()))

# 改

# dic4 = {'age':18,'name':'alex','hobby':'girl'}
# dic4['age'] = 12
# print(dic4)

# dic5 = {'age':18,'name':'alex','hobby':'girl'}
# dic6 = {'1':'111','2':'222'}
# # 类似列表的extend方法，如果有则更新，如果没有则添加
# dic5.update(dic6)
# print(dic5)


# 删除
# dic7 = {'age':18,'name':'alex','hobby':'girl'}
# # popitem随机删除字典的键值对，并返回值
# a - dic7.popitem()
# print(a,dic7)
#
# dic7.pop('age') #删除指定的键值对，并返回值
#
# del dic7['name'] #删除指定的键值对
# print(dic7)
#
# dic7.clear() #清空字典，
# print(dic7)
#
# del dic7 #删除整个字典


dic8 = dict.fromkeys(['host1','host2','host3'],'test1')

print(dic8)
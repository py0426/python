#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
#__author:Administrator
#2018/9/1


name = "Alex peng"
age = 29
job = "IT"
salary = 8000
if salary.isdigit(): #判断salary是否长得像数字。
    salary = int(salary)
else:
    print("must input digit")
    exit("must input digit")

msg = '''
=============================info for %s=======================
Name:%s
Age:%d
Job:%s
Salary:%.2f
'''%(name,name,age,job,salary)
print(msg)
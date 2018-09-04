#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
#__author:Administrator
#2018/9/2

exit_flag = False

for i in range(10):
    if i < 5:
        continue
    print("i=",i)
    for j in range(10):
        print("j=", j)
        if j == 6:

            exit_flag = True
            break
    if exit_flag:
        break
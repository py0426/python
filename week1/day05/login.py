#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
#__author:Administrator
#2018/9/2

_user = "Alex"
_passwd = "abc123"

for i in range(3):
    username = input("Username:")
    password = input("Password:")

    if username == _user and password == _passwd:

        print("Welcome %s login ..."%(username))
        break #跳出中断，break for后就不会执行后面的else语句。
    else:
        print("Invalid username or password !")

else: #只要上面的for循环正常执行完毕，中间没被打断，就会执行else语句。
    print("SB,超过次数了。")
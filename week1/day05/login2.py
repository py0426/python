#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
#__author:Administrator
#2018/9/2

_user = "Alex"
_passwd = "abc123"
counter = 0
while counter < 3:  #当while条件成立（为真）时，执行循环体。
    username = input("Username:")
    password = input("Password:")

    if username == _user and password == _passwd:

        print("Welcome %s login ..."%(username))
        break #跳出中断，break for后就不会执行后面的else语句。
    else:
        print("Invalid username or password !")
    counter += 1
    if counter == 3:
        going_choose_login = input("还想玩吗[y/n]:")
        if going_choose_login == "y":
            counter = 0
else: #只要上面的for循环正常执行完毕，中间没被打断，就会执行else语句。
    print("SB,超过次数了。")
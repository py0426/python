#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
#__author:Administrator
#2018/9/2



# 输入金额

while True:
    salary = input("请输入您能花费的金额：")
    if salary.isdigit():
        salary = int(salary)
        break
    else:
        print("请输入数字!")

product_list = [["iphone6s",5800],["mac book",9000],["coffee",32],["python book",80],["bicyle",1500]]



# 商品展示

product_index_len = len(product_list)
for product_index in range(0,product_index_len):
    id = product_index + 1

    print("%d.\t%s\t%-d"%(id,product_list[product_index][0],product_list[product_index][1]))

# 商品购买
shoping_car = []

while True:
    choice = input('选择购买商品编号[退出：q]：') # 输入金额
    if choice.isdigit():   # 判断输入是否是数字
        choice = int(choice)
        if 0 < choice <= 5:
            if salary >= int(product_list[choice - 1][1]):
                salary -= int(product_list[choice - 1][1])
                shoping_car.append(product_list[choice - 1])
                print("%s已经加入到购物车,当前余额%d"%(product_list[choice - 1][0],salary))

            else:
                print("当前余额：",salary,"不足以购买",end=" ")
                continue
        else:
            choice = input("无此商品,请选择其他商品编号或者按q退出:")

    elif choice == "q":
        print("您已购买以下商品：")
        for shoping_car_product in range(0,len(shoping_car)):
           print("商品:",shoping_car[shoping_car_product][0],"单价:",shoping_car[shoping_car_product][1])
        print("您的余额:%d元."%(salary))
        print("欢迎下次光临！")
        break

    else:
        print("您的输入不符合要求,",end=" ")

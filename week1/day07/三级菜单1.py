#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
#__author:Administrator
#2018/9/9
#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
#__author:Administrator
#2018/9/9


menu = {
    '北京':{
        '朝阳':{
            '国贸':{
                'CICC':{},
                'HP':{},
                'CCTV':{},
            },
            '望京':{
                '陌陌':{},
                '奔驰':{},
                '360':{},
            },
            '三里屯':{
                '优衣库':{},
                'apple':{},
            },
        },
        '昌平':{
            '沙河':{
                '老男孩':{},
                '阿泰包子':{},
            },
            '天通苑':{
                '链家':{},
                '我爱我家':{},
            },
            '回龙观':{},
        },
        '海淀':{
            '五道口':{
                '谷歌':{},
                '网易':{},
                'sohu':{},
                'sogo':{},
                '快手':{},
            },
            '中关村':{
                'youku':{},
                'Iqiyi': {},
                '汽车之家': {},
                '新东方': {},
                'QQ': {},
            },


        },
    },
    '上海':{
        '浦东':{
            '陆家嘴':{
                'CICC':{},
                '高盛': {},
                '摩根': {},
            },
        },
        '闵行': {},
        '外滩': {},
    },
    '广东':{
        '广州':{
            '白云区':{
                '白云机场':{},
            },
            '花都': {},
            '增城区': {},
        },
        '深圳': {
            '南山区':{
                '腾讯':{},
                'pingan': {},
            },
        },
        '东莞': {
            '虎门':{},
        },
    },
}

current_layer = menu
parent_layers = []
while True:
    for key in current_layer:
        print(key)
    choice = input(">>>:").strip()
    if len(choice) == 0:continue
    if choice in current_layer:
        parent_layers.append(current_layer)
        current_layer = current_layer[choice]
    elif choice =="b":
        current_layer = parent_layers.pop()
    else:
        print("无此项")
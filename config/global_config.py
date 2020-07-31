# coding = utf-8

"""
@author: baiwen1979

@file: global_config.py

@time: 2018/9/22 16:55

@desc: 跨所有模块的全局变量字典方法,目的是为了将配置信息的初始化统一

"""


# 初始化
def _init():
    global _global_dict
    _global_dict = {}


def set_value(key, value):
    """ 定义一个全局变量 """
    _global_dict[key] = value


def get_value(key, defValue=None):
    """ 获得一个全局变量,不存在则返回默认值 """
    try:
        return _global_dict[key]
    except KeyError:
        return defValue

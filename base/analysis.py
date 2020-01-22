# -*- coding: utf-8 -*-
# @Time    : 2019/12/27 15:54
import inspect

import yaml


def getData(funcname):

    fileInfo = inspect.stack()[1]
    fileName = fileInfo.filename
    dotIndex = fileName.rfind(".")
    underlineIndex = fileName.rfind("_")
    fileName = fileName[underlineIndex:dotIndex]

    with open('./data/data'+fileName+'.yml', 'r', encoding="utf8") as f:
        data = yaml.load(f, Loader=yaml.FullLoader)

    # 1 先将我们获取到的所有数据都存放在一个变量当中
    tmpdata = data[funcname]

    # 2 所以此时我们需要使用循环走进它的内心。
    res_arr = list()
    for value in tmpdata.values():
        tmp_arr = list()
        for j in value.values():
            tmp_arr.append(j)

        res_arr.append(tmp_arr)

    return res_arr

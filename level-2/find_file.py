#!/usr/bin/python3

import os
import re


path = 'E:\BaiduNetdiskDownload\Movie_update'

dirs = os.listdir(path)
dir_list = []
bigs = []
smalls = []
infos = []
result_list = []

def split_list():
    for root,dirs,files in os.walk(path):
        for name in files:
            big = r'(_big.jpg)'
            small = r'(_small.jpg)'
            info = r'(_info.txt)'
            if re.findall(big,name):
                bigs.append(os.path.join(root,name))
                # print(bigs)
            if re.findall(small, name):
                smalls.append(os.path.join(root,name))
                # print(smalls)
            if re.findall(info,name):
                infos.append(os.path.join(root,name))
                # print(infos)
    return bigs,smalls,infos


if __name__ == '__main__':
    big_list,small_list,info_list = split_list()

    for file in dirs:
        # print("{}\{}".format(path,file))
        file_name = os.path.join(file)
        print(file + "写入MYSQL")
        for big,small,info in zip(big_list,small_list,info_list):
            if re.search(file_name,big):
                # result_list.append(big)
                # print('{}'.format(big))
                pass
            if re.search(file_name,small):
                # result_list.append(small)
                # print('{}'.format(small))
                pass
            if re.search(file_name,info):
                # result_list.append(info)
                # print('{}'.format(info))
                # with open(info, "r", encoding="utf-8") as f:
                #     lines = f.readlines()
                    # print(lines)
                # print(file,lines[0],small,big,lines[2],lines[3],lines[4],lines[5],lines[6])
                print(file,small,big,info)

# print(result_list[0])

#删除文本关键字所在的行
# name = ['類別','演員']
#
# for i in name:
#     with open(path,"r",encoding="utf-8") as f:
#         lines = f.readlines()
#         #print(lines)
#     with open(path,"w",encoding="utf-8") as f_w:
#         for line in lines:
#             if i in line:
#                 continue
#             f_w.write(line)
# txt_path = os.path.join(root,name)
#             print("正在修改:"+txt_path)
#             name = ['類別','演員']
#             for i in name:
#                 with open(txt_path,"r",encoding="utf-8") as f:
#                     lines = f.readlines()
#                     #print(lines)
#                 with open(txt_path,"w",encoding="utf-8") as f_w:
#                     for line in lines:
#                         if i in line:
#                             continue
#                         f_w.write(line)
#             print("完后")


        # dir_list.append(os.path.join(root,name))
# print(dir_list)
# print(max(dir_list))
    # for name in dirs:
    #     print(os.path.join(root,name))

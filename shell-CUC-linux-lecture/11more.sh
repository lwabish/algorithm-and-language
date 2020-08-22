#!/usr/bin/env bash

#特殊变量
# $0 # 当前文件名
# $n # 第n个参数
# $# # 参数个数
# $@ # 参数数组
# $* # 参数字符串
# $? # 退出状态
# $$ # 当前pid
# $! # 上一个后台pid

# 文件读写
# 清空file
# > file

echo -n -e " 123 \x0a456" >file
# IFS设为空，然后读入，然后判断是否存在
while IFS= read -r line || [[ -n "$line" ]]; do
    echo "$line" | xxd -p
done

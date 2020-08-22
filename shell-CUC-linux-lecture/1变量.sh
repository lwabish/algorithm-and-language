#!/usr/bin/env bash

echo "hello world"

# 区分大小写，等号两边不能有空格
PRICE_PER_APPLE=5
MyFirstLetters=ABC
# 单引号纯字符，双引号可解释
greeting='Hello         World'

echo "price is \$$PRICE_PER_APPLE"
echo 'price is \$$PRICE_PER_APPLE'

# 空格字符保留
echo $greeting
echo "$greeting"

# 设置变量解析头尾
echo "${MyFirstLetters}hahaha"

# 子命令替换
FILELIST=$(ls) # ``
FileWithTS=/tmp/file_$(/bin/date +%Y-%m-%d).txt
echo $FILELIST
echo $FileWithTS

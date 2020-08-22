#!/usr/bin/env bash

# bash -x xxx.sh 全局调试模式

# 片段调试模式
set -x
w
set +x

# 不存在的变量只输出换行符
echo -e "$msg" >>/tmp/debug.log

# 打印不可见字符，\x01是ascii码01
msg="hello world \x01\x02"
# echo -n 不输出换行符
echo -n -e "$msg" | xxd -p >/tmp/debug.log
cat /tmp/debug.log

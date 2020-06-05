#!/usr/bin/env bash

# 逻辑表达式符号：
# [[]] 不符合posix，但是更实用，推荐使用
# [] 不推荐用，读到明白即可

# 恒假：空串，未定义变量
# !取反，&&逻辑与，||逻辑或

if [[ 0 ]]; then
    printf "%d" 0
elif [[ 1 ]]; then
    printf "123"
else
    printf "36"
fi

# 数学表达式判断写法
# [[$a -lt $b]]
# lt 小于
# le 小于等于
# gt ge 大于，大于等于
# eq等于
# ne不等于

# 字符串判断
# "a" == "b"
# "a" != "b"
# -z "$a"  是否为空串

case "$item" in
1)
    echo "case 1"
    ;;
2 | 3)
    echo "case 2 or 3"
    ;;
*)
    echo "default"
    ;;
esac

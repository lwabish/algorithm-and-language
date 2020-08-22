#!/usr/bin/env bash

# for循环
NAMES=(A B C D)
for N in ${NAMES[@]}; do
    echo "name is $N"
done

# 默认遍历数组时拆分会包含空格，这里修改为只有换行符
IFS=$'\n'
for f in $(ps -eo command); do
    echo "$f"
done

# while循环
COUNT=4
while [ $COUNT -gt 0 ]; do
    echo $COUNT
    COUNT=$(($COUNT - 1))
done

# 只有bash有的：until循环
COUNT=1
until [ $COUNT -gt 5 ]; do
    echo "$COUNT"
    COUNT=$(($COUNT + 1))
done

# break continue照旧

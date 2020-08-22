#!/usr/bin/env bash

# 声明索引数组
declare -a indexed_arr
# 声明关联数组（类似于字典）
declare -A associative_arr

# 索引数组字面量
my_array=(apple banana "F A" orange)

associative_arr['hello']="world"

# 稀疏索引数组
new_array[2]=hahaha

# 长度
echo ${#my_array[@]}

# 取元素
echo ${my_array[2]}

echo "---"
# 索引数组遍历
for item in ${my_array[@]}; do
    echo "$item"
done

echo "---"
# 关联数组遍历
for key in ${!associative_arr[@]}; do
    echo "$key|${associative_arr[$key]}"
done

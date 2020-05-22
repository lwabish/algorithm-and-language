#!/usr/bin/env bash

# 字符串操作关键注意：字符集要求

M_STRING="中文"
# 按utf8编码
export LC_ALL=en_US.utf-8
echo ${#M_STRING}
# 按字节
export LC_ALL=C
echo ${#M_STRING}

# 字符串截图、替换等，用到现查

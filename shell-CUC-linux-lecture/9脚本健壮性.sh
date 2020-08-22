#!/usr/bin/env bash

# 有错就退出
set -e
# 关闭-e
set +e

set -o pipefail
# 增加对管道命令的完整检查
set -eo pipefail

# shellcheck，静态检查语法

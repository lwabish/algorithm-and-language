package main

import (
	"fmt"
	"sort"
)

// prereqs记录了每个课程的前置课程
var prereqs = map[string][]string{"algorithms": {"data structures"}, "calculus": {"linear algebra"}, "compilers": {"data structures", "formal languages", "computer organization"}, "data structures": {"discrete math"}, "databases": {"data structures"}, "discrete math": {"intro to programming"}, "formal languages": {"discrete math"}, "networks": {"operating systems"}, "operating systems": {"data structures", "computer organization"}, "programming languages": {"data structures", "computer organization"}}

// 拓扑排序
// 深度优先搜索dfs
func main() {
	for i, course := range topoSort(prereqs) {
		fmt.Printf("%d:\t%s\n", i+1, course)
	}
}

// 因为采用了深度优先，递归地找前置课程，所以前置课程一定会在前面
// 同时又因为for遍历了所有课程，并且用seen标记了是否已经处理过，所以可以不重不漏
// 综上即可满足要求
func topoSort(m map[string][]string) []string {
	var order []string
	seen := make(map[string]bool)

	var visitAll func(items []string)
	visitAll = func(items []string) {

		// 7. 继续迭代，对于已经在seen中标记过的，直接跳过，继续发掘新课程，及其前置课程。直到迭代结束。
		for _, item := range items {
			if !seen[item] {
				// 3. 新课，在seen中标记已出现
				seen[item] = true
				// 4. 对该课的前置课程递归重复之前的操作
				fmt.Printf("即将调用visitAll(%v)\n", m[item])
				// 5. 直到遇到没有前置课程的课程，visitAll([])会直接返回，什么也不做
				visitAll(m[item])
				// 6. 按照调用栈的出栈顺序，加入结果切片中
				fmt.Printf("即将把%s加入结果\n", item)
				order = append(order, item)
			}
		}
	}

	// 1. 取map的所有key，排序
	var keys []string
	for key := range m {
		keys = append(keys, key)
	}
	sort.Strings(keys)

	// 2. 开始迭代所有的key
	visitAll(keys)
	return order
}

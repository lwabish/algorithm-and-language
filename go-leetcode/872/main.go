package main

import (
	"fmt"
	tree "github.com/lwabish/go-snippets/pkg/algorithm"
)

func main() {
	var t1 = tree.NewTree("3 5 1 6 7 4 2 n n n n n n 9 11 n n 8 10")
	var t2 = tree.NewTree("3 5 1 6 2 9 8 n n 7 4")
	t1.Draw()
	t2.Draw()
	fmt.Println(leafSimilar(t1, t2))
}

func leafSimilar(root1 *tree.TreeNode, root2 *tree.TreeNode) bool {
	var result1, result2 = &[]int{}, &[]int{}
	parseTreeLeaves(root1, result1)
	parseTreeLeaves(root2, result2)

	fmt.Println(result1, result2)
	if len(*result1) != len(*result2) {
		return false
	}

	for i := 0; i < len(*result1); i++ {
		if (*result1)[i] != (*result2)[i] {
			return false
		}
	}
	return true
}

func parseTreeLeaves(node *tree.TreeNode, result *[]int) {
	// 叶节点
	if node.Left == nil && node.Right == nil {
		*result = append(*result, node.Val)
	}

	// 左子树
	if node.Left != nil {
		parseTreeLeaves(node.Left, result)
	}

	// 右子树
	if node.Right != nil {
		parseTreeLeaves(node.Right, result)
	}

}

package tree

import "fmt"

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

// NewTreeByLevel 由层次遍历结果生成一颗二叉树
func NewTreeByLevel(l []int) (t *TreeNode) {
	var workQuene []*TreeNode
	for _, i := range l {
		if len(workQuene) == 0 {
			workQuene = append(workQuene, &TreeNode{Val: i})
			continue
		}
		t = workQuene[0]

		if workQuene[0].Left == nil {
			workQuene[0].Left = &TreeNode{Val: i}
			workQuene = append(workQuene, workQuene[0].Left)
			continue
		}

		if workQuene[0].Right == nil {
			workQuene[0].Right = &TreeNode{Val: i}
			workQuene = workQuene[1:]
			continue
		}

		return t
	}
	return nil
}

// Draw 画出二叉树的图形结构
func (t *TreeNode) Draw() {
	t.draw("", true)
}

func (t *TreeNode)draw(prefix string, isLeft bool){
	if !t{
		return
	}

	if t.Right{
		if isLeft{
			prefix=prefix+"│   "
		}else{
			prefix=prefix+"    "
		}
		t.Right.draw(prefix, false)
	}

	fmt.Print()
}

// LevelOrder 层次遍历
func (t *TreeNode) LevelOrder() []int {
	return []int{}
}

func (t *TreeNode) (){

}

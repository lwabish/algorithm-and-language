package main

func main() {

}

func findDiagonalOrder(matrix [][]int) []int {
	var result []int
	// 行
	var m = len(matrix)
	// 列
	var n = len(matrix[0])
	i, j := 0, 0
	var direc = 1
	for {
		result = append(result, matrix[i][j])
		if i == m-1 && j == n-1 {
			return result
		}
		// 到了右上的尽头
		if i == 0 && direc == 1 {
			if j+1 <= m {

			}
		}

	}
}

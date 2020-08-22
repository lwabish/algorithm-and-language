package main

func main() {
	res := 0
	resP := &res
	multiply(3, 4, resP)
	println(res)
}

func multiply(a, b int, res *int) {
	*res = a * b
}

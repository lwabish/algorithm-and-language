package main

func main() {
	// println(a())
	println(b())
}

// 顺序：正常语句（同时初始化defer），(声明返回值变量)，return为返回值变量赋值，defer，拿到返回值。
// 函数声明时如果没有给返回值命名，defer初始化时就无法使用返回值变量。
// 相反，defer初始化就可以使用返回值变量
func a() int {
	var i int
	defer func() {
		i++
		println("defer2:", i)
	}()
	defer func() {
		i++
		println("defer1:", i)
	}()
	return i
}

// 函数定义里的变量名，在函数中可以直接用，不需要再定义
func b() (i int) {
	// var i int  这里无法重定义i，因为函数签名里已经初始化了i变量
	defer func() {
		i++
		println("defer2:", i)
	}()
	defer func() {
		i++
		println("defer1:", i)
	}()
	return i
}

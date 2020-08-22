package main

func main() {
	// 创建map
	dict1 := make(map[string]string)
	dict2 := map[string]string{"red": "2", "blue": "1"}
	// 创建nil map 不能赋值
	var emptyDict map[string]string
	println(emptyDict)
	//增
	dict1["a"] = "aaaa"
	dict1["b"] = "bbbb"
	// 查
	value, exists := dict2["red"]
	if exists {
		println(value)
	}
	// 遍历
	for k, v := range dict1 {
		println(k, v)
	}
	// 删
	delete(dict2, "red")
	// 作为参数传递（传引用）
	testParam()
}

func testParam() {
	colors := map[string]string{
		"a": "A",
		"b": "B",
	}
	for k, v := range colors {
		println(k, v)
	}
	removeColor(colors, "a")
	for k, v := range colors {
		println(k, v)
	}
}
func removeColor(colors map[string]string, key string) {
	delete(colors, key)
}

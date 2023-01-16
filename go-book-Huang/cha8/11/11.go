package main

type TwoInts struct {
	a int
	b int
}

func main() {
	two1 := new(TwoInts)
	two1.a = 12
	two1.b = 10

	println(two1.AddThem())
	println(two1.AddToParam(20))

	two2 := TwoInts{3, 4}
	println(two2.AddThem())
}

func (tn *TwoInts) AddThem() int {
	return tn.a + tn.b
}
func (tn *TwoInts) AddToParam(param int) int {
	return tn.a + tn.b + param
}

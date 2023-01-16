package main

type IntVector []int

func main() {
	println(IntVector{1, 2, 3}.Sum())
}
func (self IntVector) Sum() (s int) {
	for _, x := range self {
		s += x
	}
	return
}

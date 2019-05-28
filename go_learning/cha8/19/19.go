package main

type Camara struct {
}
type Phone struct {
}
type CameraPhone struct {
	Camara
	Phone
}

func (c *Camara) TakeAPicture() string {
	return "pic"
}
func (p *Phone) Call() string {
	return "响铃"
}
func main() {
	cp := new(CameraPhone)
	println(cp.Call())
	println(cp.TakeAPicture())
}

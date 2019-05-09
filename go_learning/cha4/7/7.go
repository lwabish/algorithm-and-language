package main

func main() {
	var i = 0
	for {
		println(i)
		i++
		if i > 2 {
			goto BREAK
		}
	}
BREAK:
	println("done")
}

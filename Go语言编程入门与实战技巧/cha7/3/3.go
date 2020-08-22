package main

import (
	"fmt"
	"html/template"

	rice "github.com/GeertJohan/go.rice"
)

func main() {
	box, err := rice.FindBox("theme/default")
	if err != nil {
		println(err.Error())
		return
	}
	str, err := box.String("post.html")
	if err != nil {
		println(err.Error())
		return
	}
	t, err := template.New("tpl").Parse(str)
	fmt.Println(t, err)
}

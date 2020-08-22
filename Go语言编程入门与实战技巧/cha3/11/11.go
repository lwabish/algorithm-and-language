package main

import (
	"fmt"
	"strings"
	"unicode/utf8"
)

func main() {
	str := "this is an example of a string"
	fmt.Println(strings.HasPrefix(str, "thi"))
	fmt.Println(strings.HasSuffix(str, "string"))
	fmt.Println(strings.Contains(str, "examp"))
	fmt.Println(strings.ContainsAny(str, "abcdefg"))

	// 包含判断对空串不同，any-false，contains-true
	fmt.Println(strings.ContainsAny("abc", ""))
	fmt.Println(strings.ContainsAny("", ""))
	fmt.Println(strings.Contains("abc", ""))
	fmt.Println(strings.Contains("", ""))

	str1 := "Hi, I'm Job,Hi"
	fmt.Println(strings.Index(str1, "Job"))
	fmt.Println(strings.Index(str1, "Hi"))
	fmt.Println(strings.LastIndex(str1, "Hi"))
	fmt.Println(strings.Index(str1, "bugre"))

	str2 := "我是你爸"
	fmt.Println(strings.IndexRune(str2, '你'))

	fmt.Println(strings.Replace(str2, "我", "我吧", -1))

	fmt.Println(strings.Count(str2, "我"))

	fmt.Println(len([]rune(str2)))
	fmt.Println(utf8.RuneCountInString(str2))

	str3 := " !!! Golang !!! "
	//trim，特别注意多个目标时
	fmt.Println(strings.Trim(str3, "! "))
	fmt.Println(strings.Trim(str3, " ! "))
	fmt.Println(strings.Trim(str3, "!"))

	fmt.Println(strings.TrimLeft(str3, "! "))
	fmt.Println(strings.TrimLeft(str3, " ! "))
	fmt.Println(strings.TrimLeft(str3, "!"))

	fmt.Println(strings.TrimSpace(" \t\n这是\t一句话\n\t\r"))

	// 分隔为切片
	fmt.Println(strings.Split("a,b,c", ","))
	fmt.Println(strings.Split("a boy a girl a dog", "a "))
	fmt.Println(strings.Split("abcd ", ""))

}

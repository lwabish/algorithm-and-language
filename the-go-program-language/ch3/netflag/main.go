package main

import "fmt"

type Flags uint

const (
	FlagUp Flags = 1 << iota
	FlagBroadCast
	FlagLoopback
	FlagPointToPoint
	FlagMulticast
)

// 1024进制的单位常量
const (
	_ = 1 << (10 * iota)
	KiB
	MiB
	// ...more
)

// 由于没有幂运算符，所以不能直接写出类似上面的1000进制单位常量

func IsUp(v Flags) bool     { return v&FlagUp == FlagUp }
func TurnDown(v *Flags)     { *v &^= FlagUp }
func SetBroadCast(v *Flags) { *v |= FlagBroadCast }
func IsCast(v Flags) bool   { return v&(FlagBroadCast|FlagMulticast) != 0 }

func main() {
	var v Flags = FlagMulticast | FlagUp
	fmt.Printf("%b %t \n", v, IsUp(v))
	TurnDown(&v)
	fmt.Printf("%b %t \n", v, IsUp(v))
	SetBroadCast(&v)
	fmt.Printf("%b %t\n", v, IsUp(v))
	fmt.Printf("%b %t\n", v, IsCast(v))

}

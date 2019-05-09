package main

import (
	"fmt"
)

func main() {
	a := 10
	aP := &a
	aPP := &aP

	fmt.Printf("%d\n", a)
	fmt.Printf("%d\n", *aP)
	fmt.Printf("%d\n", **aPP)

	fmt.Printf("%x\n", aP)   //&a
	fmt.Printf("%x\n", aPP)  //&aP
	fmt.Printf("%x\n", *aPP) //&a

}

package main

import (
	"fmt"
	"math"
	"time"
)

func main() {
	println(countPrimes(18))
}

func countPrimes(n int) int {
	startTime := time.Now()
	var finalTime time.Time
	defer func() {
		fmt.Println(finalTime.Sub(startTime))
	}()
	if n < 3 {
		return 0
	}
	counter := 0
	if n == 3 {
		return 1
	}
	for i := 3; i < n; i += 2 {
		if checkPrime(i) == true {
			counter++
		}
	}
	counter++
	finalTime = time.Now()
	return counter
}
func checkPrime(n int) bool {
	nSquare := int(math.Sqrt(float64(n)))
	for i := 2; i <= nSquare; i++ {
		if n%i == 0 {
			return false
		}
	}
	return true
}

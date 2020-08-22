package main

import "testing"
import "time"

// TestPrint1 ...测试非并发
func TestPrint1(t *testing.T) {
	print1()
}

// TestPrint2 ...测试并发goruntine
func TestPrint2(t *testing.T) {
	goPrint1()
	time.Sleep(1 * time.Millisecond)
}
func TestGoPrint2(t *testing.T) {
	goPrint2()
	time.Sleep(1 * time.Millisecond)
}
func BenchmarkPrint1(b *testing.B) {
	for i := 0; i < b.N; i++ {
		print1()
	}
}
func BenchmarkGoPrint1(b *testing.B) {
	for i := 0; i < b.N; i++ {
		goPrint1()
	}
}
func BenchmarkPrint2(b *testing.B) {
	for i := 0; i < b.N; i++ {
		print2()
	}
}
func BenchmarkGoPrint2(b *testing.B) {
	for i := 0; i < b.N; i++ {
		goPrint2()
	}
}

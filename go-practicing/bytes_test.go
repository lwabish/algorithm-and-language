package go_practicing

import "testing"

var slices = [][]byte{
	[]byte("my first slice"),
	[]byte("second slice"),
	[]byte("third slice"),
	[]byte("fourth slice"),
	[]byte("fifth slice"),
}

func BenchmarkBytesMerge1(b *testing.B) {
	for i := 0; i < b.N; i++ {
		BytesMerge1(slices)
	}
}

func BenchmarkBytesMerge2(b *testing.B) {
	for i := 0; i < b.N; i++ {
		BytesMerge2(slices)
	}
}

func BenchmarkBytesMerge3(b *testing.B) {
	for i := 0; i < b.N; i++ {
		BytesMerge3(slices)
	}
}

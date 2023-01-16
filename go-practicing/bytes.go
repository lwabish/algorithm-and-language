package go_practicing

import "bytes"

func BytesMerge1(slices [][]byte) []byte {
	return bytes.Join(slices, []byte{})
}
func BytesMerge2(slices [][]byte) []byte {
	var totalLen int
	for _, s := range slices {
		totalLen += len(s)
	}
	tmp := make([]byte, totalLen)
	var i int
	for _, s := range slices {
		i += copy(tmp[i:], s)
	}
	return tmp
}
func BytesMerge3(slices [][]byte) []byte {
	var tmp []byte
	for _, s := range slices {
		tmp = append(tmp, s...)
	}
	return tmp
}

package main

import (
	"fmt"
	"io/ioutil"
	"net"
	"os"
)

func main() {
	if len(os.Args) != 2 {
		fmt.Println("需要加参数")
		os.Exit(1)
	}
	service := os.Args[1]
	tcpAddr, err := net.ResolveTCPAddr("tcp4", service)
	checkError(err)

	conn, err := net.DialTCP("tcp", nil, tcpAddr)
	checkError(err)

	_, err = conn.Write(
		[]byte("HEAD / HTTP/1.0\r\n\r\n"),
	)
	checkError(err)

	result, err := ioutil.ReadAll(conn)
	checkError(err)
	fmt.Println(string(result))
	os.Exit(0)
}
func checkError(err error) {
	if err != nil {
		fmt.Println(err)
		os.Exit(1)
	}
}

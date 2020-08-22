package main

import (
	"fmt"
)

type HttpResponse struct{ status_code int }

func (self *HttpResponse) validResponse() {
	self.status_code = 200
}
func (self HttpResponse) updateStatus() string {
	return fmt.Sprint(self)
}
func main() {
	var r1 HttpResponse
	r1.validResponse()
	println(r1.updateStatus())

	r2 := new(HttpResponse)
	r2.validResponse()
	println(r2.updateStatus())
}

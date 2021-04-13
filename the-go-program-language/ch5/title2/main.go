package main

import "net/http"

func title(url string) error {
	resp, err := http.Get(url)
	if err != nil {
		return err
	}
	// defer语句
	defer resp.Body.Close()
	return nil
}

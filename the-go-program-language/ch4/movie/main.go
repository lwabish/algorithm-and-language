package main

import (
	"encoding/json"
	"fmt"
	"log"
)

type Movie struct {
	Title  string
	Year   int  `json:"released"`
	Color  bool `json:"color,omitempty"`
	Actors []string
}

var movies = []Movie{
	{Title: "A", Year: 1942, Color: false, Actors: []string{"a", "b"}},
	{Title: "B", Year: 1942, Color: false, Actors: []string{"a", "b"}},
}

func main() {
	data, err := json.Marshal(movies)
	if err != nil {
		log.Fatalf("json marshaling failed: %s", err)
	}
	fmt.Printf("%s\n", data)

	data, err = json.MarshalIndent(movies, "", "    ")
	if err != nil {
		log.Fatalf("json marshaling indent failed: %s", err)
	}
	fmt.Printf("%s\n", data)

	var titles []struct {
		Title string
	}
	if err = json.Unmarshal(data, &titles); err != nil {
		log.Fatalf("unmarshal data failed: %s", err)
	}
	fmt.Println(titles)
}

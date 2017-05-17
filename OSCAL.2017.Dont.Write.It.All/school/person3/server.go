package main

// Adapted from https://gist.github.com/superbrothers/0a8b6390c6315916aeb8

import (
	"fmt"
	"io/ioutil"
	"log"
	"net/http"
)

func rootHandler(w http.ResponseWriter, r *http.Request) {
	w.Header().Set("Content-Type", "text/html")
	w.WriteHeader(http.StatusOK)

    var filename string
    if r.URL.Path == "/" {
        filename = "index.html"
    } else {
        filename = r.URL.Path[1:]
    }

    data, err := ioutil.ReadFile(filename)
	if err != nil {
		panic(err)
	}
	w.Header().Set("Content-Length", fmt.Sprint(len(data)))
	fmt.Fprint(w, string(data))
}

func main() {
	http.HandleFunc("/", rootHandler)
	log.Fatal(http.ListenAndServe(":8080", nil))
}

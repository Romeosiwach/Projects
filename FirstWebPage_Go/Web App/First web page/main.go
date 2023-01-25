package main

import (
	"fmt"
	"net/http"
)

func main() {
	http.HandleFunc("/", handlerfunction)
	http.ListenAndServe(":8080", nil)
}
func handlerfunction(w http.ResponseWriter, r *http.Request) {
	fmt.Fprintf(w, "Romeo's first web page %s", r.URL.Path)

}

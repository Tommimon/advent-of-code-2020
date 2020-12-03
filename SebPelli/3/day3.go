package main

import (
	"fmt"
	"io/ioutil"
	"strings"
)

type vettore struct {
	x int
	y int
}

func main() {
	input, _ := ioutil.ReadFile("/Users/sebastianpelli/Desktop/Advent/mondocane.txt")
	fmt.Println(Parte1(string(input), 3, 1))
	fmt.Println(Parte2(string(input)))
}




func Parte1(inputStr string, x int, y int) int {
	input := strings.Split(inputStr, "\n")
	posizione := vettore{0, 0}
	var contaAlberi = 0
	for posizione.y+1 < len(input) {
		posizione.x += x
		posizione.y += y
		if posizione.x >= 31 {
			posizione.x -= 31
		}
		if string(input[posizione.y][posizione.x]) == "#" {
			contaAlberi++
		}
	}
	return contaAlberi
}

func Parte2(input string) int {
	var (
		primo = Parte1(input, 1, 1)
	)
	var (
		secondo = Parte1(input, 3, 1)
	)
	var (
		terzo = Parte1(input, 5, 1)
	)
	var (
		quarto = Parte1(input, 7, 1)
	)
	var (
		quinto = Parte1(input, 1, 2)
	)
	return primo * secondo * terzo * quarto * quinto
}


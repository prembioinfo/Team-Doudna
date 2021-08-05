package main

import (
	"bytes"
	"fmt"
)
func Hamming(txt1, txt2 []byte) float64 {
	switch bytes.Compare(txt1, txt2) {
	case 0: // txt1 == txt2
	case 1: // txt1 > txt2
		temp := make([]byte, len(txt1))
		copy(temp, txt2)
		txt2 = temp
	case -1: // txt1 < txt2
		temp := make([]byte, len(txt2))
		copy(temp, txt1)
		txt1 = temp
	}
	if len(txt1) != len(txt2) {
		panic("Undefined for sequences of unequal length")
	}
	count := 0
	for idx, b1 := range txt1 {
		b2 := txt2[idx]
		xor := b1 ^ b2 
		
		for x := xor; x > 0; x >>= 1 {
			
			if int(x&1) == 1 {
				count++
			}
		}
	}
	if count == 0 {
		
		return 1
	}
	return float64(1) / float64(count)
}

func main() {
	fmt.Println(Hamming([]byte("devika"), []byte("devpoo"))) 
	fmt.Println("Name: Devika")
	fmt.Println("Email: devikakaliana94@gmail.comm")
	fmt.Println("Slack Username: Devika")
	fmt.Println("Biostack: Genomics")
	fmt.Println("Twitter Handel:DevPoo") 
	
}

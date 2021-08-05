package main
import "fmt"
func hamdist(s1 string,s2 string)int{
  str1 := []rune(s1)
  str2 := []rune(s2)
  var count int
  for i := range str1 {
    if str1[i] != str2[i] {
      count++
		}
	}
	return count
}
func main() {
    var (
        name="Shalini"
        email="shalinigupta0299@gmail.com"
        slack="@Shalini"
        biostack="Data analysts and vaccine informatics"
        twitter="@Shashaa")
    fmt.Println("Name: ",name,"\nEmai: ",email,"\nSlack Id: ",slack,"\nBiostack: ",biostack,"\nTwitter Handle: ",twitter)
    fmt.Println("Hamming Distance: ",hamdist(slack,twitter))
}

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
        biostack="Data analytics and vaccine informatics"
        twitter="@Shashaa")
    fmt.Println("\n",name,"\n",email,"\n",slack,"\n",biostack,"\n",twitter)
    fmt.Println(hamdist(slack,twitter))
}

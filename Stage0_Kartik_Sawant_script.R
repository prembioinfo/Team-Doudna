name<- "Kartik Sawant"
email<- "kartikatulsawant14@gmail.com"
slack<- "@kartik"
biostack<- "Genomics"
twitter<- "kartic"

hamming_distance<- sum(slack != twitter)

cat(name,",",email,",",slack,",",biostack,",",twitter,",",hamming_distance)

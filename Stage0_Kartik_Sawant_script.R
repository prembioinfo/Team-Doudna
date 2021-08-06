vara<- "Kartik Atul Sawant"

varb<- "kartikatulsawant14@gmail.com"

varc<- "@Kartik"

vard<- "Genomics"

vare<- "@Kartic"


varg<- "@Kartik"
varh<- "@Kartic"


HD <- function(str1, str2){
  
  str1 <- as.character(str1)
  str2 <- as.character(str2)
  
  length.str1 <- nchar(str1)
  length.str2 <- nchar(str2)
  
  string.temp1 <- c()
  for (i in 1:length.str1){
    string.temp1[i] = substr(str1, start=i, stop=i)
  }
  string.temp2 <- c()
  for (i in 1:length.str2){
    string.temp2[i] = substr(str2, start=i, stop=i)
  }
  return(sum(string.temp1 != string.temp2))
}

hamming <- HD(varg,varh)

# sum(as.vector(varh) != as.vector(varg))

varl<- c(vara,varb,varc,vard,vare,hamming)

cat(paste(varl, collapse = ','))

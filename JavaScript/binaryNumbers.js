// Write code below 💖

let myNumber = 3
let binary = ("")

for (i = myNumber;i >= 1; Math.floor(i/2)){
  if (i % 2 == 0){
    binary = "0" + binary
  }
  else 
    binary = "1" + binary
}
console.log(binary)
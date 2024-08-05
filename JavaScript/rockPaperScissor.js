
let player = 1
let computer = Math.floor(Math.random() * 3)+1;
console.log(computer);
if (player == 3 && computer == 1){
  console.log("Computer won!")
}
else if (player == 1 && computer == 2 ){
  console.log("Computer won!")
}
else if (player == 2 && computer == 3){
  console.log("Computer won!")
}
else if (computer == 1 && player == 2){
  console.log("Player won!")
}
else if (computer == 2 && player == 3){
  console.log("Player won!")
}
else if (computer == 3 && player == 1){
  console.log("Player won!")
}
else{
  console.log("Unentschieden")
}

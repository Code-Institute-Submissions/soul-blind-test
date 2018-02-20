setTimeout(function(){
  document.getElementById('submitGuess').click();
}, 33000);


let x = setInterval(function() {
  let currentSecs = $("#seconds").text();
  console.log(currentSecs);
  let newSecs = Number(currentSecs) - 1; 
  console.log(newSecs);
  $("#seconds").text(newSecs.toString());
  
}, 1000)

if(Number($("#seconds").text()) === 0){
  clearInterval(x);
}

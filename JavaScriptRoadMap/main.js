// this is one of the many javascript snippets 
// in order to keep improving my skills




const credValidator = (credential) =>{
  
  if (credential.length != 10){
    return false;
  }
  let another = credential.split("").map(function(item){
    return parseInt(item, 10);
  });

  const thirdDigit = another.slice(2, 3);
  const validator = another.slice(9, 10);

  if (thirdDigit >=6 ){
    return false;
  }
  
  let finalNumber = 0;
  for (let x = 0; x < credential.length-1; x++){
    if (x%2 == 0){
      console.log(x, another[x] * 2);
      if (another[x] * 2 >=10){
        finalNumber += (another[x] * 2-9);
        console.log(x, another[x] * 2 -9);
      }else{
        finalNumber += (another[x] * 2);
      }
    }else{
      console.log(x, another[x]);
      finalNumber += another[x];
    }
  }
  console.log(finalNumber)
  return 10 - (finalNumber % 10) == validator;
}



const word = document.getElementById("word");
const button = document.getElementById("buttonclick");


button.addEventListener("click", (event)=>{
  
  if (word.value.length === 0){
    alert("hey!!! You must to input in the textbox");
  }else{
    if (credValidator(word.value)){
      console.log("credential correct");
    }else{
      alert("the credentials is incorrect");
    }
  }
})

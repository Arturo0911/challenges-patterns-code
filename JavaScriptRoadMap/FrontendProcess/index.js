$(document).ready(function(){

  /*$('#word').change(function(){
    console.log($('#word').val());
  });*/

  let word = $('#word')
  word.keypress(function(){
    console.log(word.val());
  })

});

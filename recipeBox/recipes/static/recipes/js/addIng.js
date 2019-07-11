var currentCount = 2;
function counter(){
    return function(){
        return currentCount++;
    }
}

$(function() {
  $('#addIng').click(function() {
      /*var count = counter();
      var res = count();
      $('.ingElem').html('<span id="count"></span>. {{form.nameOfIngrediants}} : <span class="kols">{{form.countOfIngrediants}}</span> грамм.<br>')
      console.log('Count');
      console.log(res);*/
      var countF = counter()
      var count = countF()
      if(count==11){
          $(this).html('Max')
      }else{
          $('#ingElem'+count).css('display','block');
      }
  });
})
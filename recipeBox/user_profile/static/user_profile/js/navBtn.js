$(function() {
  //1
  $('#myRecipes').click(function() {
    $('.recipes').css('display','block')
    $('.folovers').css('display','none')
    $('.subscriptions').css('display','none')
    $('.about').css('display','none')
    
    $(this).css('background-color','#3F4EA6')
      
    $('#myfolovers').css('background-color','#273440')
    $('#mySubscriptions').css('background-color','#273440')
    $('#aboutMe').css('background-color','#273440')
  });
    
  //2
  $('#myfolovers').click(function() {
    $('.recipes').css('display','none')
    $('.folovers').css('display','block')
    $('.subscriptions').css('display','none')
    $('.about').css('display','none')
      
    $(this).css('background-color','#3F4EA6')
      
    $('#myRecipes').css('background-color','#273440')
    $('#mySubscriptions').css('background-color','#273440')
    $('#aboutMe').css('background-color','#273440')
  });
    
  //3
  $('#mySubscriptions').click(function() {
    $('.recipes').css('display','none')
    $('.folovers').css('display','none')
    $('.subscriptions').css('display','block')
    $('.about').css('display','none')
    
    $(this).css('background-color','#3F4EA6')
      
    $('#myRecipes').css('background-color','#273440')
    $('#myfolovers').css('background-color','#273440')
    $('#aboutMe').css('background-color','#273440')
  });
    
  //4
  $('#aboutMe').click(function() {
    $('.recipes').css('display','none')
    $('.folovers').css('display','none')
    $('.subscriptions').css('display','none')
    $('.about').css('display','block')
    
    $(this).css('background-color','#3F4EA6')
      
    $('#myRecipes').css('background-color','#273440')
    $('#myfolovers').css('background-color','#273440')
    $('#mySubscriptions').css('background-color','#273440')
  });
    
})
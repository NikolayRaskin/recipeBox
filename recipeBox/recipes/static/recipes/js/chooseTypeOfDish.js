$(function() {
  $('input[name=typeOfDish]').change(function() {
    if(this.value == 'Мясное'){
        $('#kindOfMeat').css('display','block')
        $('#kindOfFish').css('display','none')
    }else{
        if(this.value == 'Рыбное'){
            $('#kindOfFish').css('display','block')
            $('#kindOfMeat').css('display','none')
        }else{
            $('#kindOfFish').css('display','none')
            $('#kindOfMeat').css('display','none')
        }
    }
  });
})
$(function() {
  $('.intro').addClass('go');

  $('.reload').click(function() {
    $('.intro').removeClass('go').delay(300).queue(function(next) {
      $('.intro').addClass('go');
      next();
    });

  });
})
$(document).ready(function() {

  $('.user img').on('click', function() {
    $(this).toggleClass('active').end();
    $(this).next().slideToggle();
  });

  $('body').on('click', '[data-confirm]', function() {
    if (confirm($(this).data('confirm'))) {
      return true;
    } else {
      return false;
    }
  });

  $('body').on('click', 'span.prepend, span.append', function() {
    $(this).siblings('input').focus();
  });

});
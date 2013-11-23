$(document).ready(function() {

  $('.user img').on('click', function() {
    $(this).toggleClass('active').end();
    return $(this).next().slideToggle();
  });

  $('body').on('click', '[data-confirm]', function() {
    if (confirm($(this).data('confirm'))) {
      return true;
    } else {
      return false;
    }
  });

  $('body').on('click', 'span.prepend, span.append', function() {
    return $(this).siblings('input').focus();
  });

  $('body').on('click', 'ul.categories li', function() {
    $(this).siblings('.active').removeClass('active');
    $(this).addClass('active');
    $(this).parents('ul').next().val($(this).data('value'));
  });

  $('body').on('click', '.image-upload', function() {
    $(this).next().click();
  });

  $('body').on('change', '.image-upload-field', function() {
    alert('ok');
    $(this).prev().addClass('selected');
    $(this).prev().html('DEU');
    $(this).next().click();
  });
});
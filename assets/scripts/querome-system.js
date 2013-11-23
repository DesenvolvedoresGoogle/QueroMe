$(document).ready(function() {

  $('body').on('click', '[data-confirm]', function() {
    if (confirm($(this).data('confirm'))) {
      return true;
    } else {
      return false;
    }
  });

});
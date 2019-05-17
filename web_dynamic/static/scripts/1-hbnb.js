$('document').ready(function () {
  let amenities = {};
  $("INPUT").on('click', function () {
    if ($(this).is(':checked')) {
      amenities[$(this).attr('data-id')] = $(this).attr('data-name');
    } else {
      delete amenities[$(this).attr('data-id')];
    }
    $('.AMENITIES H4').text(Object.values(amenities).join(', '));
  });
});

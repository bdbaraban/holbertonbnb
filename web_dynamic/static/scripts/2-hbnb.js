$('document').ready(function () {
  $.get('http://172.28.128.4:5001/api/v1/status/', function (response) {
    if (response.status === 'OK') {
      $('DIV#api_status').css('background-color', '#ff545f');
    } else {
      $('DIV#api_status').css('background-color', '#ccc');
    }
  });

  let amenities = {};
  $('INPUT[type="checkbox"]').change(function () {
    if ($(this).is(':checked')) {
      amenities[$(this).attr('data-id')] = $(this).attr('data-name');
    } else {
      delete amenities[$(this).attr('data-id')];
    }
    if (Object.values(amenities).length === 0) {
      $('.amenities H4').html('&nbsp;');
    } else {
      $('.amenities H4').text(Object.values(amenities).join(', '));
    }
  });
});

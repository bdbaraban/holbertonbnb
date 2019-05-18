$('document').ready(function () {
  const url = 'http://' + window.location.hostname + ':5001/api/v1/status/';
  $.get(url, function (response) {
    if (response.status === 'OK') {
      $('DIV#api_status').addClass('available');
    } else {
      $('DIV#api_status').removeClass('available');
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
  $.ajax({
    url: 'http://192.168.1.24:5001/api/v1/places_search/',
    type: 'POST',
    dataType: 'json',
    contentType: 'application/json',
    data: '{}'
  })
    .done(function (data) {
      for (let item of data) {
        $('section.places').append(`
            <article>
              <div class="title">
                <h2>${item.name}</h2>
                <div class="price_by_night">
                  ${item.price_by_night}
                </div>
              </div>
              <div class="information">
                <div class="max_guest">
                  <i class="fa fa-users fa-3x" aria-hidden="true"></i>
                  </br>
                  ${item.max_guest} Guests
                </div>
                <div class="number_rooms">
                  <i class="fa fa-bed fa-3x" aria-hidden="true"></i>
                  </br>
                  ${item.number_rooms} Bedrooms
                </div>
                <div class="number_bathrooms">
                  <i class="fa fa-bath fa-3x" aria-hidden="true"></i>
                  </br>
                  ${item.number_bathrooms} Bathrooms
                </div>
              </div>
              <div class="description">
                ${item.description}
              </div>
            </article>
          `);
      }
    });
});

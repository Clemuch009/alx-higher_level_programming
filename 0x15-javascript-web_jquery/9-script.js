$(document).ready(function () {
  var originalUrl = 'https://hellosalut.stefanbohacek.dev/?lang=fr';
  var proxyUrl = 'https://api.allorigins.win/raw?url=' + encodeURIComponent(originalUrl);
  
  $.ajax({
    url: proxyUrl,
    type: 'GET',
    dataType: 'json',
    success: function (data) {
      $('#hello').html(data.hello);
    },
    error: function (xhr, status, error) {
      console.error('Error fetching hello:', status, error);
      $('#hello').html('Failed to load greeting');
    }
  });
});

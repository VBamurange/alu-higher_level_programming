#!/usr/bin/node

$.ajax({
  url: 'https://fourtonfish.com/hellosalut/?lang=fr',
  type: 'GET',
  dataType: 'json',
  success: (json) => {
    $('Div#hello').text(json);
  }
});

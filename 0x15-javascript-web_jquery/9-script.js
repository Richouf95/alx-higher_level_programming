// JavaScript script that fetches
// from https://hellosalut.stefanbohacek.dev/?lang=fr 
// and displays the value of hello from that fetch 
// in the HTML tag DIV#hello.
$(document).ready(() => {
  $.get('https://fourtonfish.com/hellosalut/?lang=fr', (data) => {
    $('div#hello').text(data.hello);
  });
});

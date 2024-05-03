// JavaScript script that adds a 
// <li> element to a list when 
// the user clicks on the tag DIV#add_item:
$('#add_item').on('click', () => {
    $('.my_list').append('<li>Item</li>');
});

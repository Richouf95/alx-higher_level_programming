// JavaScript script that fetches 
// and prints how to say “Hello” 
// depending on the language

const translate = () => {
    const url = 'https://www.fourtonfish.com/hellosalut/?';
    $.get(url + $.param({ lang: $('#language_code').val() }), (data) => {
        $('#hello').html(data.hello);
    });
}

$(document).ready(() => {
    $('#btn_translate').click(translate);
    $('#language_code').focus(() => {
        $(this).keydown((e) => {
            if (e.keyCode === 13) {
                translate();
            }
        });
    });
});

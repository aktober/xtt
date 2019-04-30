$(document).ready(function () {

    $('form#form-id').submit(function (event) {
        event.preventDefault();

        var currency = $('input#currency').val();
        var number = $('input#number').val();
        if (number === '') {
            number = 0;
        }

        $.ajax({
            type: 'GET',
            url: 'http://0.0.0.0:5000/api/v1/last',
            data: {
                currency: currency,
                number: number
            },
            success: function (data) {
                $('textarea#results').text(JSON.stringify(data, undefined, 4));
            }
        });
    });
});
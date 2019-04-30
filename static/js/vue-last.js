var app = new Vue({
    delimiters: ['[[', ']]'],
    el: '#app',

    data: {
        currency: null,
        number: null,
        info: ''
    },

    methods: {
        processForm: function (e) {
            e.preventDefault();
            console.log('currency', app.currency);
            console.log('number', app.number);

            axios.get('/api/v1/last', {
                    params: {
                        currency: app.currency,
                        number: app.number
                    }
                })
                .then(function (response) {
                    console.log(response.data);
                    app.info = response.data;
                });
        }
    }
});
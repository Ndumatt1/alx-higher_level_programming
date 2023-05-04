$.ajax({
    url: 'https://swapi-api.alx-tools.com/api/films/?format=json',
    method: 'GET',
    success: (body) => {
        console.log(body.title);
        $.each(body.results, (index, value) => {
            $('UL#list_movies').append('<li>'+ value.title + '</li>');
        });
    }
});
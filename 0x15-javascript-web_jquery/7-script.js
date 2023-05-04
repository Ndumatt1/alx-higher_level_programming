const url = 'https://swapi-api.alx-tools.com/api/people/5/?format=json';

$.ajax({
    url: url,
    method: 'GET',
    success: (body) => {
        $('#character').text(body.name);
    }
});

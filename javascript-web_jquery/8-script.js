$.get("https://swapi-api.hbtn.io/api/films/?format=json", function (data) {
    const movies = data["results"]
    for (title in movies) {
        $("#list_movies").append($("<li>").text(movies[title]["title"]));
    }
});
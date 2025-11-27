fetchMovies();

async function fetchMovies () {
  const NAME_URL = 'https://swapi-api.hbtn.io/api/films/?format=json';
  const moviesList = document.querySelector('#list_movies');
  try {
    const response = await fetch(NAME_URL);
    if (!response.ok) {
      throw new Error(`HTTP error: ${response.status}`);
    }
    const data = await response.json();

    data.forEach(movie => {
      const liMovie = document.createElement('li');
      liMovie.textContent = movie.title;
      moviesList.appendChild(liMovie);
    });
  } catch (e) {
    console.error('Error: ', e);
  }
}

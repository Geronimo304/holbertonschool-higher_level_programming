fetchName();

async function fetchName () {
  const NAME_URL = 'https://swapi-api.hbtn.io/api/people/5/?format=json';
  const characterTag = document.querySelector('#character');
  try {
    const response = await fetch(NAME_URL);
    if (!response.ok) {
      throw new Error(`HTTP error: ${response.status}`);
    }
    const data = await response.json();

    characterTag.textContent = data.name;
  } catch (e) {
    console.error('Error: ', e);
  }
}

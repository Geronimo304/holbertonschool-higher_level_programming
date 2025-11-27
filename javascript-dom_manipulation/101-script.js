document.addEventListener('DOMContentLoaded', () => {
  const fetchBtn = document.querySelector('#btn_translate');
  const languageBox = document.querySelector('#language_code');

  fetchBtn.addEventListener('click', () => {
    const language = languageBox.value;
    const helloURL = `https://hellosalut.stefanbohacek.com/?lang=${language}`;

    if (!language) {
      alert('Please, select a language from the box');
      return;
    }

    fetchHello(helloURL);
  });
});

async function fetchHello (URL) {
  const NAME_URL = URL;
  const helloBox = document.querySelector('#hello');
  try {
    const response = await fetch(NAME_URL);
    if (!response.ok) {
      throw new Error(`HTTP error: ${response.status}`);
    }
    const data = await response.json();
    helloBox.textContent = data.hello;
  } catch (e) {
    console.error('Error: ', e);
  }
}

const tagButton = document.querySelector('#red_header');
tagButton.addEventListener('click', () => {
  const header = document.querySelector('header');
  header.classList.add('red');
});

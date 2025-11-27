const updateHeader = document.querySelector('#update_header');

updateHeader.addEventListener('click', () => {
  const headerElement = document.querySelector('header');
  headerElement.textContent = 'New Header!!!';
});

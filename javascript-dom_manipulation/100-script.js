document.addEventListener('DOMContentLoaded', () => {
  const btnAddItem = document.querySelector('#add_item');
  const btnRemoveItem = document.querySelector('#remove_item');
  const btnClear = document.querySelector('#clear_list');
  const myList = document.querySelector('#my_list');

  btnAddItem.addEventListener('click', () => {
    const newElement = document.createElement('li');

    newElement.textContent = 'Item';
    myList.appendChild(newElement);
  });

  btnRemoveItem.addEventListener('click', () => {
    if (myList.lastElementChild) {
      myList.removeChild(myList.lastElementChild);
    }
  });

  btnClear.addEventListener('click', () => {
    myList.innerHTML = '';
  });
});

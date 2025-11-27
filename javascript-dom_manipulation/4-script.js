const addItemBtn = document.querySelector('#add_item');
addItemBtn.addEventListener('click', () => {
  const ulList = document.querySelector('.my_list');
  const newElement = document.createElement('li');
  newElement.innerText = 'Item';
  ulList.appendChild(newElement);
});

const mapReal = (list, func) => {
  const newList = [];

  for(let i = 0; i < list.length;i++){
    newList.push(func(list[i]));
  }

  return newList
}

const map = (list) => {
  const newList = [];

  for(let i = 0; i < list.length;i++){
    newList.push(list[i] * 2);
  }

  return newList
}

const list = [1, 2 ,3 ,4, 5, 6];

const new_list = mapReal(list, (item) => {
  return item * 4;
})

console.log(new_list);
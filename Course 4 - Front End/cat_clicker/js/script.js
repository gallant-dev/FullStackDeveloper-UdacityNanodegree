var cats = [{
    name: 'Grumpy Cat',
    clicks: 0
  },{
    name: 'Fat Cat',
    clicks: 0
  },{
    name: 'Ugly Kitten',
    clicks: 0
  },{
    name: 'Warrior Cat',
    clicks: 0
  },{
    name: 'Polite Kitty',
    clicks: 0
  },{
    name: 'Two-Face Cat',
    clicks: 0
  }]

var currentCat = 0;

var catDisplay = document.getElementById('cat-display');
var catList = document.getElementById('cat-list');
var catImage = document.createElement('img');
catImage.classList.add('pic');
catImage.id = 'cat-image';
catImage.src = 'cat'+currentCat+'.jpg'

var clickElem = document.createElement('div');
clickElem.classList.add('cat-clicks');
var clickText = document.createElement('text');
clickText.id = 'click-text';
clickText.textContent = "Click A Cat!";
clickElem.appendChild(clickText);
catDisplay.appendChild(clickElem);


catDisplay.appendChild(catImage);

for (var i = 0; i < cats.length; i++) {
  var catName = cats[i].name;
  var catNum = i;

  var nameElem = document.createElement('div');
  nameElem.classList.add('menu-item');
  nameElem.id = 'menu-item-' + i;

  var nameText = document.createElement('text');
  nameText.classList.add('name-text');
  nameElem.appendChild(nameText);

  nameText.textContent = catName;

  nameElem.addEventListener('click', (function(catCopy) {
      return function() {
          document.getElementById('menu-item-'+currentCat).style.backgroundColor = 'orange';
          document.getElementById('cat-image').src = "cat"+ catCopy + ".jpg";
          document.getElementById('menu-item-'+catCopy).style.backgroundColor = 'red';
          clickText.textContent = cats[catCopy].clicks;
          currentCat = catCopy;
      };
  })(catNum));

  catList.appendChild(nameElem);
}

catImage.addEventListener('click', function(){
  cats[currentCat].clicks += 1;
  clickText.textContent = cats[currentCat].clicks;
});
